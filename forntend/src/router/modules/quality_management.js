/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const qualityManageRouter = {
  path: '/quality_management',
  component: Layout,
  redirect: '/quality_management/version_management',
  name: 'QualityManagement',
  meta: {
    title: '质量管理',
    icon: 'star'
  },
  children: [
    {
      path: 'version_management',
      component: () => import('@/views/quality_management/version_management'),
      name: 'VersionManagement',
      meta: { title: '版本管理' }
    },
    {
      path: 'production_accident',
      component: () => import('@/views/quality_management/production_accident'),
      name: 'ProductionAccident',
      meta: { title: '生产事故' }
    }
  ]
}
export default qualityManageRouter
