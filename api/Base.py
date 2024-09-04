# -*- coding:utf-8 -*-
"""
@Created on : 2024/9/4
@Author: vaconzhang
@Des: 基本路由
"""
from fastapi import APIRouter
router = APIRouter()


@router.get('/')
async def home(num: int):
    # num为必填参数
    return num
