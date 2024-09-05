# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: 中间件
"""

import time
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request
from core.Helper import random_str


class Middleware:
    """
    Middleware
    """

    def __init__(
            self,
            app: ASGIApp,
    ) -> None:
        self.app = app

    # 中间件就是对发起的请求进行拦截，拦截后进行处理，再放行
    # scope一个包含请求信息的字典， receive（一个用于接收事件（如请求体）的异步可调用对象），和send（一个用于发送响应的异步可调用对象）。
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        # --------对请求进行预处理
        # 类型不是http或者websocket的，不处理
        if scope["type"] not in ("http", "websocket"): # pragma: no cover
            # 调用self.app（即原始应用程序）来处理请求，并返回
            await self.app(scope, receive, send)
            return
        start_time = time.time()
        # 请求头中设置session
        req = Request(scope, receive, send)
        # 如果请求中带有session字段，SessionMiddleware中间件会对session对应的值通过盐进行加密
        if not req.session.get("session"):  # 如果请求头中没有session
            req.session.setdefault("session", random_str())  # 添加一个唯一值到session字段中

        # --------对响应进行预处理
        async def send_wrapper(message: Message) -> None:
            """对原始的send函数进行包装"""
            process_time = time.time() - start_time
            # print("message", message)
            # http.response.start 消息标志着HTTP响应的开始，并包含状态码和响应头信息。
            # http.response.body 消息用于发送HTTP响应的体部分，可以发送一个或多个这样的消息来传递完整的响应体。
            # 这里是把处理事件加入到响应头中
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append("X-Process-Time", str(process_time))
            await send(message)
        await self.app(scope, receive, send_wrapper)