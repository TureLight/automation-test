import request from '@/utils/request'

export function searchUser(name) {
  return request({
    url: '/search/user',
    method: 'get',
    params: { name }
  })
}

export function panelGroupList() {
  return request({
    url: '/dashboard/read_panel_group_data',
    method: 'get',
    params: { 'query_params': 'panel_group_data' }
  })
}

export function pieChartList() {
  return request({
    url: '/dashboard/read_data',
    method: 'get',
    params: { 'query_params': 'pie_chart_data' }

  })
}

export function barChartList() {
  return request({
    url: '/dashboard/read_data',
    method: 'get',
    params: { 'query_params': 'bar_chart_data' }
  })
}

export function taskDataList() {
  return request({
    url: '/dashboard/read_data',
    method: 'get',
    params: { 'query_params': 'task_data_list' }
  })
}
