# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
from conf.settings import *
from model.db_operator import save_data
from model.data_model import LawyerInfo_gd
from conf.settings import get_proxies_id

def get_data(data_id):
    times = 0
    while times < 3:
        try:
            r = requests.get(url=url_gdsf %data_id, timeout=10)
            if r.status_code != 200:
                print('ERROR_RSP', r.status_code)
                times += 1
                time.sleep(1)
                continue
            else:
                break
        except Exception as e:
            print('ERROR_RSP', e)
            times += 1
            time.sleep(1)

    html_data = r.text
    soup = BeautifulSoup(html_data, "lxml")
    lawer_tbody = soup.table.tbody
    tr = lawer_tbody.find_all("tr")

    ret = {}
    key, value = [], []
    for i in tr:
        if not i.td:
            continue
        tds = i.find_all("td")
        for td in tds:
            if td.label:
                key.append(td.label.string)
            else:
                print(td.string)
                value.append(td.string.strip())
    for k,v in zip(key,value):
        ret[k] = v
    return ret

def format_data(data):
    ret = {}
    for k,v in data.items():
        if "姓名" in k:
            ret["name"] = v
        if "性别" in k:
            ret["gender"] = v
        if "民族" in k:
            ret["nationality"] = v
        if "学历" in k:
            ret["degree"] = v
        if "执业证号" in k:
            ret["licensed_no"] = v
        if "资格证号" in k:
            ret["qualification_no"] = v
        if "执业证取得日期" in k:
            ret["licensed_date"] = v
        if "资格证取得日期" in k:
            ret["qualification_date"] = v
        if "执业状态" in k:
            ret["licensed_status"] = v
        if "考核结果" in k:
            ret["examination_result"] = v
        if "所在事务所" in k:
            ret["law_firm"] = v
    if not ret["licensed_no"] or not ret["qualification_no"]:
        return None
    return ret


if __name__ == '__main__':
    for data_id in range(48188, 50000):
        data = get_data(data_id)
        print(data_id, ': ',data)
        data_map = format_data(data)
        if not data_map:
            continue
        save_data(data_table=LawyerInfo_gd, data_map=data_map)
        time.sleep(1)

