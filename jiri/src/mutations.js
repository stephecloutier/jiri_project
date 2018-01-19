import Vue from 'vue'
import router from './router'
import initialState from './initial-state'

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
        // const initial = state
        // Object.keys(initial).forEach(key => {state[key] = initial[key]})
        //state = initialState.reader()
        //state = {}
        //localStorage.clear()
        Object.assign(state, initialState.reader())
        //localStorage.setItem("datas", JSON.stringify(state))
        router.push('/')
    }
}


