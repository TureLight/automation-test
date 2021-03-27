import schemas
import datetime
from bson import ObjectId, Int64
from loguru import logger


class CrudTestManage:

    mdb = 'automation_data'
    collection = 'test_manage_data'

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
        elif data.module_name and data.file_name and data.author:
            query_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'file_name': data.file_name,
                 'author': data.author,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('id', order)]]).skip(offset_num).limit(limit_num)
        elif data.module_name and data.file_name:
            query_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'file_name': data.file_name,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('id', order)]]).skip(offset_num).limit(limit_num)
        elif data.module_name:
            query_res = db[self.mdb][self.collection].find(
                {'module_name': data.module_name,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
        elif data.file_name and data.author and data.status:
            query_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'author': data.author,
                 'status': data.status,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
        elif data.file_name and data.author:
            query_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'author': data.author,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
        elif data.file_name:
            query_res = db[self.mdb][self.collection].find(
                {'file_name': data.file_name,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
        elif data.author and data.status:
            query_res = db[self.mdb][self.collection].find(
                {'author': data.author,
                 'status': data.status,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
        elif data.author:
            query_res = db[self.mdb][self.collection].find(
                {'author': data.author,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
        elif data.status:
            query_res = db[self.mdb][self.collection].find(
                {'status': data.status,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
        else:
            query_res = db.test_manage.find({'is_delete': False}, {'_id': 0}).sort([('id', order)]).skip(offset_num).limit(limit_num)
        if not query_res:
            return False
        res_list = [x for x in query_res]
        count_num = len(res_list)
        return [res_list, count_num]

    async def create_case(self, db, data: schemas.UpdateCaseInfo):
        last_id = db.test_manage.find_one(sort=[('id', -1)])
        logger.debug(last_id)
        if not last_id:
            return False
        res = db.test_manage.insert_one({'id': last_id['id'] + 1,
                                         'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
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
        return True

    async def update_case_info(self, db, data: schemas.UpdateCaseInfo):
        res = db.test_manage.update_one({'id': data.id},
                                        {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                  'module_name': data.module_name,
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


test_manage = CrudTestManage()
