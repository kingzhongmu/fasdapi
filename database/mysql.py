# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:15 AM
@Author: binkuolo
@Des: mysql数据库【创建】
models中的数据变更，或者需要删除数据库的表，重新创建表时，register_mysql中的generate_schemas设置为True
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os


# -----------------------数据库配置【可以配置多个数据库】-----------------------------------
DB_ORM_CONFIG = {
    # 创建一个数据库链接
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('BASE_HOST', '127.0.0.1'),   # 获取不到，使用后面的默认值
                'user': os.getenv('BASE_USER', 'root'),
                'password': os.getenv('BASE_PASSWORD', 'Vacon1234'),
                'port': int(os.getenv('BASE_PORT', 3306)),
                'database': os.getenv('BASE_DB', 'fasdapi'),
            }
        },
        # "db2": {
        #     'engine': 'tortoise.backends.mysql',
        #     "credentials": {
        #         'host': os.getenv('DB2_HOST', '127.0.0.1'),
        #         'user': os.getenv('DB2_USER', 'root'),
        #         'password': os.getenv('DB2_PASSWORD', '123456'),
        #         'port': int(os.getenv('DB2_PORT', 3306)),
        #         'database': os.getenv('DB2_DB', 'db2'),
        #     }
        # },
        # "db3": {
        #     'engine': 'tortoise.backends.mysql',
        #     "credentials": {
        #         'host': os.getenv('DB3_HOST', '127.0.0.1'),
        #         'user': os.getenv('DB3_USER', 'root'),
        #         'password': os.getenv('DB3_PASSWORD', '123456'),
        #         'port': int(os.getenv('DB3_PORT', 3306)),
        #         'database': os.getenv('DB3_DB', 'db3'),
        #     }
        # },

    },
    # 第一个"base"是配置的名字；"models.base"是models文件夹下的base文件；第二个"base"是上面定义的connections中的"base"
    # 定义了与特定数据库连接相关联的模型和应用。
    # 在这个例子中，只有一个名为base的应用，它指向上面定义的base数据库连接，并且从models.base模块中加载模型。

    # "models.base" 通常指的是Python中一个名为 models 的包（通常是一个包含 __init__.py 文件的目录），该包内部有一个名为 base.py 的文件。
    # base.py 文件应该包含Tortoise ORM的模型定义。
    "apps": {
        "base": {"models": ["models.base"], "default_connection": "base"},
        # "db2": {"models": ["models.db2"], "default_connection": "db2"},
        # "db3": {"models": ["models.db3"], "default_connection": "db3"}
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


async def register_mysql(app: FastAPI):
    # 注册数据库【在fastapi启动完毕后注册数据库，在core中的event中的startup中执行】
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=False,  # 如果为True的话（在数据库中创建表;如果已经有对应表了，则报一个错误）
        add_exception_handlers=True,  # mysql 开启了异常信息的处理
    )