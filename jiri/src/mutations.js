import Vue from 'vue'
import router from './router'
import {initialState} from './initial-state'

export const mutations = {
    setInitialValueOfState(state, data) {
        state.token = data.token
        state.user = data.user,
        state.errors = data.errors,
        state.currentEvent = data.currentEvent,
        state.currentEventStudentsList = data.currentEventStudentsList,
        state.pastMeetings = data.pastMeetings
        state.studentsFromPastMeetings = data.studentsFromPastMeetings
               
    },
    saveToken(state, token) {
        state.token = token
    },
    saveUserId(state, id) {
        state.user = {...state.user, id: id}
    },
    saveUserInfo(state, data) {
        state.user = {
            ...state.user, 
            first_name: data.first_name,
            last_name: data.last_name,
            is_admin: data.is_admin,
            profile_pic: data.profile_pic,
            email: data.username,
            meetings: data.meetings
         }
    },
    saveErrors(state, data) {
        state.errors = data.non_field_errors
    },
    saveCurrentEvent(state, data) {
        state.currentEvent = data
    },
    currentEventStudentsList(state, data) {
        state.currentEventStudentsList = data
    },
    pastMeetings(state, data) {
        state.pastMeetings = data
    },
    studentsFromPastMeetings(state, data) {
        state.studentsFromPastMeetings = data
    },
    clearStoreAndState(state) {
        //Object.assign(state, initialState())
        //console.log(state)
        //localStorage.setItem("datas", JSON.stringify(state))
        //state = initialState()
        state.token = ''
        state.user = {}
        state.errors = []
        // state.currentEvent = {}
        // state.currentEventStudentsList = []
        // state.pastMeetings = []
        // state.studentsFromPastMeetings = []
        // localStorage.setItem('token', state.token)
        // localStorage.setItem('user', state.user)
        // localStorage.setItem('errors', state.errors)
        // localStorage.setItem('currentEvent', state.currentEvent)
        // localStorage.setItem('currentEventStudentsList', state.currentEventStudentsList)
        // localStorage.setItem('pastMeetings', state.pastMeetings)
        // localStorage.setItem('studentsFromPastMeetings', state.studentsFromPastMeetings)
        router.push('/')
    }
}


