#-*- coding: utf-8 -*-
__all__ = ['LawyerInfo_gd', 'db']

from datetime import datetime
from pony.orm import *
from model import db


class LawyerInfo_gd(db.Entity):
    name = Optional(str)  # 姓名
    gender = Optional(str)  # 性别
    nationality = Optional(str)  # 民族
    degree = Optional(str)  # 学历
    licensed_no = Optional(str)  # 执业证号
    qualification_no = Optional(str)  # 资格证号
    licensed_date = Optional(datetime)  # 执业证取得日期
    qualification_date = Optional(datetime)  # 资格证取得日期
    licensed_status = Optional(str)  # 执业状态
    examination_result = Optional(str)  # 考核结果
    law_firm = Optional(str)  # 所在律师事务所
