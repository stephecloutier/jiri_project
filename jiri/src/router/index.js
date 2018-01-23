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
import CreateStudent from '@/components/CreateStudent'
import CreateProject from '@/components/CreateProject'
import CreateUser from '@/components/CreateUser'
import EventInfo from '@/components/EventInfo'
import EventProjects from '@/components/EventProjects'
import EventStudents from '@/components/EventStudents'
import EventUsers from '@/components/EventUsers'
import EventRecap from '@/components/EventRecap'
import SingleImplementation from '@/components/SingleImplementation'


import {store} from '../store'

Vue.use(Router)

export const router = new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login,
      beforeEnter: (to, from, next) => {
        if (store.state.token) {
          next(false)
        } else if (from.name != 'login') {
          next()
        }
      }
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
      path: '/meetings/:meetingId/:id',
      name: 'single-implementation',
      component: SingleImplementation
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      meta: { admin: true }
    },
    {
      path: '/students',
      name: 'students',
      component: Students,
      meta: { admin: true }
    },
    {
      path: '/projects',
      name: 'projects',
      component: Projects,
      meta: { admin: true }
    },
    {
      path: '/users',
      name: 'users',
      component: Users,
      meta: { admin: true }
    },
    {
      path: '/events',
      name: 'events',
      component: Events,
      meta: { admin: true }
    },
    {
      path: '/events/add',
      component: CreateEvent,
      children: [
        {
          path: '',
          name: 'event-info',
          component: EventInfo,
          meta: { admin: true }
        },
        {
          path: 'projects',
          name: 'event-projects',
          component: EventProjects,
          meta: { admin: true }
        },
        {
          path: 'students',
          name: 'event-students',
          component: EventStudents,
          meta: { admin: true }
        },
        {
          path: 'users',
          name: 'event-users',
          component: EventUsers,
          meta: { admin: true }
        },
        {
          path: 'recap',
          name: 'event-recap',
          component: EventRecap,
          meta: { admin: true }
        },
      ],
      meta: { admin: true }
    },
    {
      path: '/students/add',
      name: 'create-student',
      component: CreateStudent,
      meta: { admin: true }
    },
    {
      path: '/projects/add',
      name: 'create-project',
      component: CreateProject,
      meta: { admin: true }
    },
    {
      path: '/users/add',
      name: 'create-user',
      component: CreateUser,
      meta: { admin: true }
    },
  ]
})
