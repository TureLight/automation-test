/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const systemManageRouter = {
  path: '/system_management',
  component: Layout,
  redirect: '/system_management/user_management',
  name: 'SystemManagement',
  meta: {
    title: '系统管理',
    icon: 'jiekoupeizhi'
  },
  children: [
    {
      path: 'user_management',
      component: () => import('@/views/system_management/user_management'),
      name: 'UserManagement',
      meta: { title: '用户管理' }
    }
  ]
}
export default systemManageRouter
