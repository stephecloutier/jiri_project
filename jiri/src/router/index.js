import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Meetings from '@/components/Meetings'
import SingleMeeting from '@/components/SingleMeeting.vue'
import Dashboard from '@/components/Dashboard'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/meetings',
      name: 'meetings',
      component: Meetings
    },
    {
      path: '/meetings/:id',
      name: 'single-meeting',
      component: SingleMeeting
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    }
  ]
})
