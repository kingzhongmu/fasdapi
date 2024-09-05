# -*- coding:utf-8 -*-
"""
@Created on : 2024/9/4
@Author: vaconzhang
@Des: 基本路由
"""
from fastapi import APIRouter
from api.login import index, login
from api.test_redis import test_my_redis, test_my_redis_depends

# 这里的tags为所有使用ApiRouter的路由进行分类
ApiRouter = APIRouter(prefix="/v1", tags=["api路由"])


ApiRouter.get("/test/my/redis", tags=["api路由"], summary="fastapi的state方式")(test_my_redis)
ApiRouter.get("/test/my/redis/depends", tags=["api路由"], summary="依赖注入方式")(test_my_redis_depends)

# 非装饰器的方式添加路由【tags 用于对路由进行分类； summary用于对路由进行注释】
ApiRouter.get("/index", tags=["api路由"], summary="注册接口")(index)
ApiRouter.post("/login", tags=["api路由"], summary="登陆接口")(login)


@ApiRouter.get('/input')
async def home(num: int):
    # fastapi返回的字典，正好对应的是web前段对应的json
    return {"num": num, "data": [{"num": num, "data": []}, {"num": num, "data": []}]}
