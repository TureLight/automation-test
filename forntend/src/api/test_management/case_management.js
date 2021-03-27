import request from '@/utils/request'

export function fetchList(data) {
  return request({
    url: '/test_management/case_list',
    method: 'post',
    data
  })
}

export function updateCaseStatus(data) {
  return request({
    url: '/test_management/update_case_status',
    method: 'post',
    data
  })
}

export function deleteCase(id) {
  return request({
    url: '/test_management/delete_case_info',
    method: 'delete',
    params: { id }
  })
}

export function createCaseInfo(data) {
  return request({
    url: '/test_management/create_case_info',
    method: 'post',
    data
  })
}

export function updateCaseInfo(data) {
  return request({
    url: '/test_management/update_case_info',
    method: 'post',
    data
  })
}
