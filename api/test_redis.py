# -*- coding:utf-8 -*-
"""
@Time : 2022/4/25 2:37 PM
@Author: binkuolo
@Des: test redis
"""

from core.Response import success
from fastapi import Depends, Request
from database.redis import sys_cache
from aioredis import Redis


# 通过
async def test_my_redis(req: Request):
    # 连接池放在request中【在core>Event>startup中】
    value = await req.app.state.cache.get("ex_today")

    return success(msg="test_my_redis", data=[value])


# 通过连接池依赖注入的方式，调用此函数对应路径时，会先执行sys_cache,他会返回一个Redis对象，这里保存为cache
async def test_my_redis_depends(today: int, cache: Redis = Depends(sys_cache)):
    # 连接池放在依赖注入
    # await cache.set(name="today", value=today)  # 不过期键值对
    # name相当于key（ex_today）
    await cache.set(name="ex_today", value=today)  # ex是过期时间，单位是秒；60s后在Redis库中就会删除掉
    # value = await cache.get("today")
    return success(msg=f"今天是{today}号", data=[])