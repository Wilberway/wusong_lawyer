#-*- coding: utf-8 -*-

import traceback
from pony.orm import db_session, commit
from model.data_model import db,db_session

db_host = 'rm-8vb4yxswwu7qimokso.mysql.zhangbei.rds.aliyuncs.com'
db_user = 'user_law'
db_password = 'Abc1234%'
db_name = 'data_wenshu'

db.bind('mysql', host=db_host, user=db_user, passwd=db_password, db=db_name)
db.generate_mapping(create_tables=True)

@db_session
def save_data(data_table, data_map):
    # table_attrs = [i for i in data_table.__dict__.keys() if i[0] != '_']
    # if 'id' in table_attrs:
    #     table_attrs.remove('id')
    try:
        old_data = data_table.get(**{'licensed_no':data_map['licensed_no'],'qualification_no':data_map['qualification_no']})
        if old_data:
            print('[WARNING] Data already existed, licensed_no: %s, qualification_no: %s' %(data_map['licensed_no'], data_map['qualification_no']))
            for k, v in data_map.items():
                if v != getattr(old_data, k):
                    setattr(old_data, k, v)
        else:
            data_table(**data_map)
            return 0
    except Exception as e:
        traceback.print_exc()
        print('[ERROR] Data save failed, err: %s, licensed_no: %s' % (str(e), data_map['licensed_no']))
        return -1
    return 0
