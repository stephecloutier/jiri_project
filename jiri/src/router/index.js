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
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
    {
      path: '/students',
      name: 'students',
      component: Students,
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
    {
      path: '/projects',
      name: 'projects',
      component: Projects,
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
    {
      path: '/users',
      name: 'users',
      component: Users,
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
    {
      path: '/events',
      name: 'events',
      component: Events,
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
    {
      path: '/events/add',
      component: CreateEvent,
      children: [
        {
          path: '',
          name: 'event-info',
          component: EventInfo
        },
        {
          path: 'projects',
          name: 'event-projects',
          component: EventProjects
        },
        {
          path: 'students',
          name: 'event-students',
          component: EventStudents
        },
        {
          path: 'users',
          name: 'event-users',
          component: EventUsers
        },
        {
          path: 'recap',
          name: 'event-recap',
          component: EventRecap
        },
      ],
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
    {
      path: '/students/add',
      name: 'create-student',
      component: CreateStudent,
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
    {
      path: '/projects/add',
      name: 'create-project',
      component: CreateProject,
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
    {
      path: '/users/add',
      name: 'create-user',
      component: CreateUser,
      beforeEnter: (to, from, next) => {
        if(store.state.user.is_admin) {
          next()
        } else {
          next(false)
        }
      }
    },
  ]
})

router.beforeEach((to, from, next) => {
  if(!store.state.token && to.name != 'login') {
    next({name: 'login'})
  } else {
    next()
  }
})