/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const systemStateRouter = {
  path: '/system_state',
  component: Layout,
  redirect: '/system_state/timed_task',
  name: 'SystemState',
  meta: {
    title: '系统状态',
    icon: 'fuwuqi'
  },
  children: [
    {
      path: 'timed_task',
      component: () => import('@/views/system_state/timed_task'),
      name: 'TimedTask',
      meta: { title: '定时任务' }
    }
  ]
}
export default systemStateRouter
