# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 8:33 PM
@Author: binkuolo
@Des: views home
"""
from pydantic import Required
from fastapi import Request, Form, Cookie
from fastapi import Request, Form
from models.base import User
from typing import Optional


async def home(request: Request):
    """
    门户首页
    :param request:
    :return:
    """
    return request.app.state.views.TemplateResponse("index.html", {"request": request})


async def reg_page(req: Request):
    """
    注册页面
    :param req:
    :return: html
    """
    return req.app.state.views.TemplateResponse("reg_page.html", {"request": req})


# 定义表单参数， ... 说明这里是必传项目, 也可以用default=Required代替
async def result_page(req: Request, username: str = Form(...), password: str = Form(default=Required)):
    """
    注册结果页面
    :param password: str
    :param username: str
    :param req:
    :return: html
    """

    # 插入一条数据
    add_user = await User().create(username=username, password=password)
    print("插入的自增ID", add_user.pk)
    print("插入的用户名", add_user.username)

    # 查询User表中所有的数据
    user_list = await User().all().values()
    # 打印查询结果
    for user in user_list:
        print(f"用户:{user.get('username')}", user)

    # 获取当前创建的用户【get_or_none查询不到不会报错】
    get_user = await User().get_or_none(username=username)
    if not get_user:
        print("")
        return {"info": "没有查询到用户"}
    # 渲染返回结果网页
    return req.app.state.views.TemplateResponse(
        "reg_result.html", {"request": req, "username": get_user.username, "password": get_user.password})
