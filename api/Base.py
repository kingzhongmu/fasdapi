# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: api路由【总】
"""
from fastapi import APIRouter, Security
from core.Auth import check_permissions
from api.user import user_info, user_add, user_del, account_login, user_list
from schemas.user import CurrentUser, UserLogin
from api.test import test_oath2

ApiRouter = APIRouter(prefix="/api/v1")
AdminRouter = APIRouter(prefix="/admin")
# 非装饰器的方式添加路由【tags 用于对路由进行分类； summary用于对路由进行注释】
ApiRouter.post("/test/oath2", tags=["测试oath2授权"])(test_oath2)

# UserLogin 响应模型
AdminRouter.post("/account/login", response_model=UserLogin, tags=["管理员登陆"], summary="用户登陆")(account_login)

# 请求走到这个路由，会先走Security 中的check_permissions回调；scopes 指定路由所需要的作用域权限，如果是list，用户拥有list中的任一权限即可访问路由
AdminRouter.get("/user/info",
                tags=["用户管理"],
                summary="获取当前管理员信息",
                dependencies=[Security(check_permissions)],
                response_model=CurrentUser
                )(user_info)

AdminRouter.get("/user/list",
                tags=["用户管理"],
                summary="获取管理员列表",
                dependencies=[Security(check_permissions, scopes=["user_list"])],
                # response_model=CurrentUser
                )(user_list)


AdminRouter.delete("/user/del",
                   tags=["用户管理"],
                   summary="管理员删除",
                   dependencies=[Security(check_permissions, scopes=["user_delete"])]
                   )(user_del)

AdminRouter.post("/user/add",
                 tags=["用户管理"],
                 summary="管理员添加",
                 dependencies=[Security(check_permissions, scopes=["user_add"])]
                 )(user_add)

ApiRouter.include_router(AdminRouter)