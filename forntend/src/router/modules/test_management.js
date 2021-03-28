/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const testManageRouter = {
  path: '/test_management',
  component: Layout,
  redirect: '/test_management/case_management',
  name: 'TestManagement',
  meta: {
    title: '测试管理',
    icon: 'clipboard'
  },
  children: [
    {
      path: 'case_management',
      component: () => import('@/views/test_management/case_management'),
      name: 'CaseManagement',
      meta: { title: '用例管理' }
    },
    {
      path: 'test_project',
      component: () => import('@/views/test_management/test_project'),
      name: 'TestProject',
      meta: { title: '测试计划' }
    },
    {
      path: 'common_params',
      component: () => import('@/views/test_management/common_params'),
      name: 'CommonParams',
      meta: { title: '公共参数' }
    }
  ]
}
export default testManageRouter
