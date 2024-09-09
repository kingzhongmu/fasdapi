# -*- coding:utf-8 -*-
"""
@Time : 2022/5/4 10:54 PM
@Author: binkuolo
@Des: 基础schemas【路由的入参pydantic和出参pydantic】
"""
from pydantic import BaseModel, Field


class BaseResp(BaseModel):
    code: int = Field(description="状态码")
    message: str = Field(description="信息")