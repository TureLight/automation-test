/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const testReportRouter = {
  path: '/test_report',
  component: Layout,
  redirect: '/test_report/complex_report',
  name: 'TestReport',
  meta: {
    title: '测试报告',
    icon: 'bug'
  },
  children: [
    {
      path: 'complex_report',
      component: () => import('@/views/test_report/complex_report'),
      name: 'ComplexReport',
      meta: { title: '自定义报告' }
    },
    {
      path: 'allure_report',
      component: () => import('@/views/test_report/allure_report'),
      name: 'AllureReport',
      meta: { title: 'allure报告' }
    },
    {
      path: 'pytest_report',
      component: () => import('@/views/test_report/pytest_report'),
      name: 'PytestReport',
      meta: { title: 'pytest报告' }
    }
  ]
}
export default testReportRouter
