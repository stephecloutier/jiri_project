import Vue from 'vue'
import {router} from './router'
import initialState from './initial-state'

export const mutations = {
    setInitialValueOfState(state, data) {
        Object.assign(state, data)
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
    saveAllStudents(state, data) {
        state.students = data
    },
    saveAllProjects(state, data) {
        state.projects = data
    },
    saveAllUsers(state, data) {
        state.users = data
    },
    saveAllEvents(state, data) {
        state.events = data
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
    setCurrentMeeting(state, data) {
        state.currentMeeting = data
    },
    setCurrentStudent(state, data) {
        state.currentStudent = data
    },

    clearStoreAndState(state) {
        Object.assign(state, initialState)
        localStorage.setItem('store', JSON.stringify(state))
        router.push('/')
    },

    currentStudentImplementations(state, data) {
        state.currentStudentImplementations = data
    },

    currentImplementation(state, data) {
        state.currentImplementation = data
    },

    changeCurrentEvent(state, data) {
        state.currentEvent = data
    },

    saveCurrentScore(state, data) {
        state.currentScore = data
    },

    saveCurrentMeetings(state, data) {
        state.currentMeetings = data
    },

    saveAllImplementations(state, data) {
        state.implementations = data
    },

    saveAllScores(state, data) {
        state.scores = data
    }
}


