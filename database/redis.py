# -*- coding:utf-8 -*-
"""
@Time : 2022/4/25 2:09 PM
@Author: binkuolo
@Des: redis 用于缓存从mysql查询到的数据，快速查询；缓解对mysql的压力，提供好的用户体验
验证码的过期时间，可以设置在redis
redis安装：https://blog.csdn.net/weixin_44893902/article/details/123087435
"""

import aioredis
import os
from aioredis import Redis


async def sys_cache() -> Redis:
    """
    系统缓存
    :return: cache 连接池
    """
    # 从URL方式创建redis连接池
    sys_cache_pool = aioredis.ConnectionPool.from_url(
        f"redis://{os.getenv('CACHE_HOST', '127.0.0.1')}:{os.getenv('CACHE_PORT', 6379)}",
        db=os.getenv('CACHE_DB', 0),
        encoding='utf-8',
        decode_responses=True
    )
    return Redis(connection_pool=sys_cache_pool)