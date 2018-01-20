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
      path: '/events/add',
      component: CreateEvent,
      children: [
        {
          // UserProfile will be rendered inside User's <router-view>
          // when /user/:id/profile is matched
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
      ]
    },
    {
      path: '/students/add',
      name: 'create-student',
      component: CreateStudent
    },
    {
      path: '/projects/add',
      name: 'create-project',
      component: CreateProject
    },
    {
      path: '/users/add',
      name: 'create-user',
      component: CreateUser
    },
  ]
})
