# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: 基本配置文件
"""

import os.path
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    # 加载环境变量.env；覆盖模式，添加到系统环境变量中
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息【显示在docs文件中】
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "fastapi-demo"
    DESCRIPTION: str = 'fastapi项目demo'
    # 静态资源目录【os.getcwd() 获取工作目录， 同app.py目录】
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")
    # 跨域请求
    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']

    # session
    SECRET_KEY = "session"   # 这是一个加密盐，用于加密和解密session数据
    SESSION_COOKIE = "session_id"  # 这个是session在cookie中的保存的键值
    SESSION_MAX_AGE = 14 * 24 * 60 * 60


settings = Config()
