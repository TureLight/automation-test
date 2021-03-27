/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const taskManageRouter = {
  path: '/task_management',
  component: Layout,
  redirect: '/management/case_management',
  name: 'TaskManagement',
  meta: {
    title: '任务管理',
    icon: 'kuaisugaoxiao'
  },
  children: [
    {
      path: 'test_execution',
      component: () => import('@/views/task_management/test_execution'),
      name: 'TestExecution',
      meta: { title: '测试执行' }
    },
    {
      path: 'task_scheduling',
      component: () => import('@/views/task_management/task_scheduling'),
      name: 'TaskScheduling',
      meta: { title: '任务调度' }
    }
  ]
}
export default taskManageRouter
