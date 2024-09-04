# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 8:33 PM
@Author: binkuolo
@Des: views home
"""
from fastapi import Request


async def home(request: Request, id: str):
    # 从request中获取templates（即request.app.state.views）；调用渲染函数
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})