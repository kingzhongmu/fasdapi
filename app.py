# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: app运行时文件
"""
import uvicorn
import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from fastapi.staticfiles import StaticFiles
from core.Router import AllRouter
from core.Events import startup, stopping
from core.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, UnicornException
from core.Middleware import Middleware
from fastapi.templating import Jinja2Templates

# 创建app对象
application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME
    )


# 事件监听【FastApi 启动完成和 FastApi 停止事件】
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))


# 异常错误处理【针对三类异常的处理回调：http异常，请求验证异常，执行器异常】
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http422_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)

# 路由【api中的Base路由】
application.include_router(AllRouter)

# 处理请求时，中间件的调用顺序和添加顺序相反
# 处理响应时，中间件的调用顺序和添加顺序相同（均调用定义的 send_wrap）
# 中间件【添加中间件】
application.add_middleware(Middleware)
# 添加session中间件
application.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    session_cookie=settings.SESSION_COOKIE,
    max_age=settings.SESSION_MAX_AGE
)
# 添加跨域中间件
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# 静态资源目录
application.mount('/static', StaticFiles(directory=settings.STATIC_DIR), name="static")

# state可以往请求头中塞一些东西，这里把views塞进去，保存模板对象；后面的所有传入路径的request都有这个模板参数
application.state.views = Jinja2Templates(directory=settings.TEMPLATE_DIR)

app = application

if __name__ == '__main__':
    uvicorn.run(app)