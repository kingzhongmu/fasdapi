# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 11:43 AM
@Author: binkuolo
@Des: 路由聚合
"""
from api.Base import ApiRouter  # 基础API路由实例引入
from views.Base import ViewsRouter  # 视图路由实例引入
from fastapi import APIRouter


AllRouter = APIRouter()
# 视图路由【不断通过include_router 往下包含】
AllRouter.include_router(ViewsRouter)
# API路由
AllRouter.include_router(ApiRouter)


