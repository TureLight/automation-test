import request from '@/utils/request'

export function searchUser(name) {
  return request({
    url: '/search/user',
    method: 'get',
    params: { name }
  })
}

export function taskDataList(query) {
  return request({
    url: '/task_data/data_list',
    method: 'get',
    params: query
  })
}
