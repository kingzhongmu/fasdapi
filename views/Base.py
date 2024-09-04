# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 11:46 AM
@Author: binkuolo
@Des: 视图路由
"""
from fastapi import APIRouter
from starlette.responses import HTMLResponse

from views.home import home

ViewsRouter = APIRouter(tags=["视图路由"])

# 【以下添加路由的方法，方便查看，管理所有路由】

# 添加home中的路由
ViewsRouter.get("/items/{id}", response_class=HTMLResponse)(home)


# @ViewsRouter.get("/items/{id｝",response_class=HTMLResponse)
# async def read_item():
#     # return templates.get_template("index.html").render({"request": request, "id": id})
#     # return templates.TemplateResponse("index.html",{"request":request,"id":id}) # 和上面等价
#     # print(request.app.state.views)
