import request from '@/utils/request'

export function searchUser(name) {
  return request({
    url: '/search/user',
    method: 'get',
    params: { name }
  })
}

export function panelGroupList(query) {
  return request({
    url: '/dashboard/panel_group_data',
    method: 'get',
    params: query
  })
}

export function pieChartList(query) {
  return request({
    url: '/dashboard/pie_chart_data',
    method: 'get',
    params: query
  })
}

export function barChartList(query) {
  return request({
    url: '/dashboard/bar_chart_data',
    method: 'get',
    params: query
  })
}

export function taskDataList(query) {
  return request({
    url: '/dashboard/task_data',
    method: 'get',
    params: query
  })
}
