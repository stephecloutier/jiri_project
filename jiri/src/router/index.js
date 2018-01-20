import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Meetings from '@/components/Meetings'
import SingleMeeting from '@/components/SingleMeeting.vue'
import Dashboard from '@/components/Dashboard'
import Students from '@/components/Students'
import Projects from '@/components/Projects'
import Users from '@/components/Users'
import Events from '@/components/Events'
import CreateEvent from '@/components/CreateEvent'


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
    },
    {
      path: '/students',
      name: 'students',
      component: Students
    },
    {
      path: '/projects',
      name: 'projects',
      component: Projects
    },
    {
      path: '/users',
      name: 'users',
      component: Users
    },
    {
      path: '/events',
      name: 'events',
      component: Events
    },
    {
      path: '/events/create',
      name: 'create-event',
      component: CreateEvent
    },
  ]
})
