import request from '@/utils/request'

export function fetchList(data) {
  return request({
    url: '/task_schedule/task_list',
    method: 'post',
    data
  })
}

export function createTask(data) {
  return request({
    url: '/task_schedule/create_task',
    method: 'post',
    data
  })
}

export function operatorTask(data) {
  return request({
    url: '/task_schedule/operator_task',
    method: 'post',
    data
  })
}

export function updateTask(data) {
  return request({
    url: '/task_schedule/update_task',
    method: 'post',
    data
  })
}

export function deleteTask(id) {
  return request({
    url: '/task_schedule/delete_task',
    method: 'delete',
    params: { id }
  })
}

export function getSuite() {
  return request({
    url: '/task_schedule/get_suite',
    method: 'get'
  })
}
