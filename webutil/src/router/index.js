import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: () => import('../views/index.vue')
  },
  {
    path: '/detail',
    name: 'detail',
    component: () => import('../views/detail.vue')
  },
  {
    path: '/createtable',
    name: 'tcreatetable',
    component: () => import('../views/creatable.vue')
  },
  {
    path: '/sql',
    name: 'sql',
    component: () => import('../views/sql.vue')
  },
  {
    path: '/submitsql',
    name: 'submitsql',
    component: () => import('../views/submitsql.vue')
  },
  {
    path: '/tabledetail',
    name: 'tabledetail',
    component: () => import('../views/detailtable.vue')
  }
]

const router = new VueRouter({
	
  mode: "history",
  routes
})

export default router
