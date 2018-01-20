import Vue from 'vue'
import Vuex from 'vuex'

import {getters} from './getters.js'
import {mutations} from './mutations.js'
import {actions} from './actions.js'

import initialState from './initial-state'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        token: '',
        user: {},
        errors: [],
        students: [],
        projects: [],
        users: [],
        events: [],
        currentEvent: {},
        currentEventStudentsList: [],
        pastMeetings: [],
        studentsFromPastMeetings: [],
        currentMeeting: {},
        currentStudent: {},
        currentStudentImplementations: [],
    },
    getters,
    mutations,
    actions,
})
