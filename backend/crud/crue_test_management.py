import schemas
import datetime
from bson import Int64
from loguru import logger


class CrudTestManage:

    mdb = 'automation_data'
    collection = 'test_case'

    async def get_case_info_list(self, db, data: schemas.CaseQuery):

        order = -1 if data.sort == '-id' else 1
        limit_num = data.limit
        offset_num = (data.page - 1) * data.limit

        if data.module_name and data.file_name and data.author and data.status:
            query_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'file_name': data.file_name,
                 'author': data.author,
                 'status': data.status,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('id', order)]]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'file_name': data.file_name,
                 'author': data.author,
                 'status': data.status,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.module_name and data.file_name and data.author:
            query_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'file_name': data.file_name,
                 'author': data.author,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('id', order)]]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'file_name': data.file_name,
                 'author': data.author,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.module_name and data.file_name:
            query_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'file_name': data.file_name,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('id', order)]]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'file_name': data.file_name,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.module_name:
            query_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.file_name and data.author and data.status:
            query_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'author': data.author,
                 'status': data.status,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'author': data.author,
                 'status': data.status,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.file_name and data.author:
            query_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'author': data.author,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'author': data.author,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.file_name:
            query_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.author and data.status:
            query_res = db[self.mdb][self.collection].find(
                {'author': data.author,
                 'status': data.status,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'author': data.author,
                 'status': data.status,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.author:
            query_res = db[self.mdb][self.collection].find(
                {'author': data.author,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'author': data.author,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.status:
            query_res = db[self.mdb][self.collection].find(
                {'status': data.status,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db[self.mdb][self.collection].find(
                {'status': data.status,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        else:
            query_res = db.test_manage.find({'is_delete': False},
                                            {'_id': 0}
                                            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db.test_manage.find({'is_delete': False},
                                            {'_id': 1}
                                            ).count()
        if not query_res:
            return False
        res_list = [x for x in query_res]
        return [res_list, total_res]

    async def create_case(self, db, data: schemas.UpdateCaseInfo):
        # id自增可能会失败吧,先用着
        last_id = db.test_manage.find_one(sort=[('id', -1)])
        # logger.debug(last_id)
        if not last_id:
            return False
        res = db.test_manage.insert_one({'id': Int64(last_id['id'] + 1),
                                         'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                         'total': Int64(data.total),
                                         'module_name': data.module_name,
                                         'file_name': data.file_name,
                                         'file_path': data.file_path,
                                         'author': data.author,
                                         'version': data.version,
                                         'status': data.status,
                                         'is_delete': False
                                         })
        if not res:
            return False
        p_key = str(res.inserted_id)
        update = db.test_manage.update_one({'_id': res.inserted_id},
                                           {'$set': {'p_key': p_key}}
                                           )
        if update.modified_count != 1:
            return False
        return True

    async def update_case_info(self, db, data: schemas.UpdateCaseInfo):
        res = db.test_manage.update_one({'id': data.id},
                                        {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                  'module_name': data.module_name,
                                                  'total': Int64(data.total),
                                                  'file_name': data.file_name,
                                                  'file_path': data.file_path,
                                                  'author': data.author,
                                                  'version': data.version,
                                                  'status': data.status
                                                  }
                                         }
                                        )
        if res.modified_count != 1:
            return False
        return True

    async def update_case_status(self, db, data: schemas.UpdateCaseStatus):
        res = db.test_manage.update_one({'id': data.id},
                                        {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                  'status': data.status
                                                  }
                                         }
                                        )
        if res.modified_count != 1:
            return False
        return True

    async def delete_case_info(self, db, row: int):
        res = db.test_manage.update_one({'id': row},
                                        {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                  'is_delete': True
                                                  }
                                         }
                                        )
        if res.modified_count != 1:
            return False
        return True

    async def query_suite(self, db, data: schemas.SuiteQuery):
        order = -1 if data.sort == '-id' else 1
        limit_num = data.limit
        offset_num = (data.page - 1) * data.limit

        if data.suite_name and data.tester:
            query_res = db.test_suite.find(
                {'suite_name': data.suite_name,
                 'tester': data.tester,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('_id', order)]]).skip(offset_num).limit(limit_num)
            total = db.test_suite.find(
                {'suite_name': data.suite_name,
                 'tester': data.tester,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.suite_name:
            query_res = db.test_suite.find(
                {'suite_name': data.suite_name,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('_id', order)]]).skip(offset_num).limit(limit_num)
            total = db.test_suite.find(
                {'suite_name': data.suite_name,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        elif data.tester:
            query_res = db.test_suite.find(
                {'tester': data.tester,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('_id', order)]]).skip(offset_num).limit(limit_num)
            total = db.test_suite.find(
                {'tester': data.tester,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        else:
            query_res = db.test_suite.find({'is_delete': False},
                                           {'_id': 0}
                                           ).sort([('_id', order)]).skip(offset_num).limit(limit_num)
            total = db.test_suite.find({'is_delete': False},
                                       {'_id': 1}
                                       ).count()
        if not query_res:
            return False
        res_list = [x for x in query_res]
        return [res_list, total]

    async def create_suite(self, db, data: schemas.SuiteCreate):
        # id自增可能会失败吧,先用着
        last_id = db.test_suite.find_one(sort=[('id', -1)])
        # logger.debug(last_id)
        if not last_id:
            return False
        res = db.test_suite.insert_one({'id': Int64(last_id['id'] + 1),
                                        'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                        'suite_name': data.suite_name,
                                        'tester': data.tester,
                                        'version': data.version,
                                        'status': 'null',
                                        'case_keys': [],
                                        'is_delete': False
                                        })
        if not res:
            return False
        p_key = str(res.inserted_id)
        update = db.test_suite.update_one({'_id': res.inserted_id},
                                          {'$set': {'p_key': p_key}}
                                          )
        if update.modified_count != 1:
            return False
        return True

    async def update_suite(self, db, data: schemas.SuiteUpdate):
        res = db.test_suite.update_one({'p_key': data.p_key},
                                       {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                 'suite_name': data.suite_name,
                                                 'tester': data.tester,
                                                 'version': data.version,
                                                 }
                                        }
                                       )
        if res.modified_count != 1:
            return False
        return True

    # async def insert_suite_items(self, db, data: schemas.InsertSuiteItems):
    #     res = db.test_suite.update_one({'p_key': data.p_key},
    #                                    {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
    #                                              'case_keys': data.case_keys}}
    #                                    )
    #     if res.modified_count != 1:
    #         return False
    #     return True

    async def insert_suite_items(self, db, data: schemas.InsertSuiteItems):
        suite_items = db.test_manage.find({'id': {'$nin': data.case_keys}, 'is_delete': False}, {'_id': 0})
        key_list = [x['p_key'] for x in suite_items]
        pipeline = [{'$match': {'id': {'$nin': data.case_keys}, 'is_delete': False}},
                    {'$group': {'_id': {}, '_total': {'$sum': '$total'}}}
                    ]
        total = [x for x in db.test_manage.aggregate(pipeline)]
        res = db.test_suite.update_one({'p_key': data.p_key},
                                       {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                 'total': Int64(total[0]['_total']),
                                                 'case_keys': key_list}}
                                       )
        if res.modified_count != 1:
            return False
        return True

    async def get_suite_items(self, db, p_key):
        """
        获取对应已编制好的用例集
        :param db:
        :param p_key:
        :return:
        """
        try:
            res = db.test_suite.find_one({'p_key': p_key}, {'case_keys': 1})
            suite_items = db.test_manage.find({'p_key': {'$in': res['case_keys']}, 'is_delete': False}, {'_id': 0})
            # suite_items = [db.test_manage.find_one({'p_key': item}, {'_id': 0}) for item in res['case_keys']]
            res_list = [x for x in suite_items]
            if len(res_list) != len(res['case_keys']):
                return False
            return res_list
        except Exception as e:
            logger.error(e)
            return False

    async def get_diff_items(self, db, p_key):
        """
        获取对应已编制好的用例差集
        :param db:
        :param p_key:
        :return:
        """
        try:
            res = db.test_suite.find_one({'p_key': p_key}, {'case_keys': 1})
            logger.debug(res['case_keys'])
            suite_items = db.test_manage.find({'p_key': {'$nin': res['case_keys']}, 'is_delete': False}, {'_id': 0})
            # suite_items = [db.test_manage.find_one({'p_key': item}, {'_id': 0}) for item in res['case_keys']]
            res_list = [x['id'] for x in suite_items]
            logger.debug(res_list)
            return res_list
        except Exception as e:
            logger.error(e)
            return False

    async def get_case_items_for_insert(self, db, data: schemas.QueryNINPool):
        """
        生成待选用例池
        :param db:
        :param data:
        :return:
        """
        # logger.debug(data.nin_list)
        if data.nin_list:
            res = db.test_manage.find({'p_key': {'$nin': data.nin_list}, 'is_delete': False}, {'_id': 0})
        else:
            res = db.test_manage.find({'is_delete': False}, {'_id': 0})
        if not res:
            return False
        return [x for x in res]

    async def delete_suite(self, db, p_key: str):
        res = db.test_suite.update_one({'p_key': p_key},
                                       {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                 'is_delete': True
                                                 }
                                        }
                                       )
        if res.modified_count != 1:
            return False
        return True


test_manage = CrudTestManage()
