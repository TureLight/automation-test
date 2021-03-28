import request from '@/utils/request'

export function getSuite(data) {
  return request({
    url: '/test_project/suite_list',
    method: 'post',
    data
  })
}

export function createSuite(data) {
  return request({
    url: '/test_project/create_suite',
    method: 'post',
    data
  })
}

export function updateSuite(data) {
  return request({
    url: '/test_project/update_suite',
    method: 'post',
    data
  })
}

export function insertSuiteItems(data) {
  return request({
    url: '/test_project/insert_suite_items',
    method: 'post',
    data
  })
}

export function getDetails(p_key) {
  return request({
    url: '/test_project/get_items',
    method: 'get',
    params: { p_key }
  })
}

export function getItems(p_key) {
  return request({
    url: '/test_project/get_items',
    method: 'get',
    params: { p_key }
  })
}

export function getDiffItems(p_key) {
  return request({
    url: '/test_project/get_diff_items',
    method: 'get',
    params: { p_key }
  })
}
export function getPool(data) {
  return request({
    url: '/test_project/get_pool',
    method: 'post',
    data
  })
}

export function deleteSuite(p_key) {
  return request({
    url: '/test_project/delete_suite',
    method: 'delete',
    params: { p_key }
  })
}
