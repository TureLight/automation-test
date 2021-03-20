import request from '@/utils/request'

export function login(data) {
  return request({
    url: 'login/access-token',
    method: 'post',
    data
  })
}

/** @method 注册
 * @param data: {object} {username: xx, password: xx, key: xx}
 * **/
export function register(data) {
  return request({
    url: '/login/register',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/login/user_info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/login/logout',
    method: 'post'
  })
}
