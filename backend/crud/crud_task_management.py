import schemas
import datetime
from bson import Int64
from loguru import logger


class CrudTaskSchedule:

    async def task_list(self, db, data: schemas.QueryTask):

        order = -1 if data.sort == '-id' else 1
        limit_num = data.limit
        offset_num = (data.page - 1) * data.limit

        if data.task_name:
            query_res = db.task_schedule.find(
                {'task_name': data.task_name,
                 'is_delete': False
                 },
                {'_id': 0}
            ).sort([[('id', order)]]).skip(offset_num).limit(limit_num)
            total_res = db.task_schedule.find(
                {'task_name': data.task_name,
                 'is_delete': False
                 },
                {'_id': 1}
            ).count()
        else:
            query_res = db.task_schedule.find({'is_delete': False},
                                            {'_id': 0}
                                            ).sort([('id', order)]).skip(offset_num).limit(limit_num)
            total_res = db.task_schedule.find({'is_delete': False},
                                            {'_id': 1}
                                            ).count()
        if not query_res:
            return False
        res_list = [x for x in query_res]
        return [res_list, total_res]

    async def create_task(self, db, data: schemas.UpdateTask):
        # id自增可能会失败吧,先用着
        last_id = db.task_schedule.find_one(sort=[('id', -1)])
        if not last_id:
            return False
        get_suite = db.test_suite.find_one({'p_key': data.suite_name})
        res = db.task_schedule.insert_one({'id': Int64(last_id['id'] + 1),
                                         'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                         'total': Int64(get_suite['total']),
                                         'task_name': data.task_name,
                                         'suite_name': get_suite['suite_name'],
                                         'operator': data.operator,
                                         'version': data.version,
                                         'status': 'idle',
                                         'f_key': data.suite_name,
                                         'is_delete': False
                                         })
        if not res:
            return False
        p_key = str(res.inserted_id)
        update = db.task_schedule.update_one({'_id': res.inserted_id},
                                           {'$set': {'p_key': p_key}}
                                           )
        if update.modified_count != 1:
            return False
        return True

    async def update_task(self, db, data: schemas.UpdateTask):
        get_suite = db.test_suite.find_one({'p_key': data.suite_name})
        res = db.task_schedule.update_one({'id': data.id},
                                        {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                  'total': Int64(get_suite['total']),
                                                  'task_name': data.task_name,
                                                  'suite_name': get_suite['suite_name'],
                                                  'operator': data.operator,
                                                  'version': data.version,
                                                  'status': data.status,
                                                  'f_key': data.suite_name,
                                                  'is_delete': False
                                                  }
                                         }
                                        )
        if res.modified_count != 1:
            return False
        return True

    async def operator_task(self, db, data: schemas.OperatorTask):
        res = db.task_schedule.update_one({'id': data.id},
                                          {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                    'status': data.status
                                                    }
                                           }
                                          )
        if res.modified_count != 1:
            return False
        return True

    async def delete_task(self, db, row: int):
        res = db.test_manage.update_one({'id': row},
                                        {'$set': {'update_time': datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),
                                                  'is_delete': True
                                                  }
                                         }
                                        )
        if res.modified_count != 1:
            return False
        return True

    async def get_suite(self, db):
        res = db.test_suite.find({'is_delete': False}, {'_id': 0})
        if not res:
            return False
        res_list = [{'id': x['id'], 'name': x['suite_name'], 'p_key': x['p_key']} for x in res]
        return res_list


task_schedule = CrudTaskSchedule()
