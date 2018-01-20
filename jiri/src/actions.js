import {HTTP} from './http-common'

export const actions = {
    login({commit}, user) {
        return new Promise((resolve, reject) => {
            HTTP.post('authenticate/', {
                username: user.email,
                password: user.password
            })
                .then((response) => {
                    commit('saveToken', response.data.token)
                    commit('saveUserId', response.data.id)
                    resolve(response);
                })
                .catch((error) => {
                    commit('saveErrors', error.response.data)
                    reject(error);
                })
        })
    },

    logout(context) {
        context.commit('clearStoreAndState')
    },

    getUserInfo(context, id) {
        return new Promise((resolve, reject) => {
            HTTP.get('users/' + id + '/', {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    context.commit('saveUserInfo', response.data)
                    resolve(response)
                })
                .catch((error) => {
                    context.commit('saveErrors', error.response.data)
                    reject(error)
                })
        })
    },

    // fetches events from api, find the one with the closest exam_date, store its info in the state
    fetchClosestEvent(context) {
        return new Promise((resolve, reject) => {
            HTTP.get('events/', {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    // date sorting ( to put in a different function )
                    let currentDate = Date.now()
                    let eventDate = {index: undefined, difference: undefined}

                    response.data.results.forEach((event, index) => {
                        let date = new Date(event.exam_date)
                        let difference = Math.abs(currentDate - date)
  
                        if(eventDate.difference == undefined || difference < eventDate.difference) {
                            eventDate.difference = difference
                            eventDate.index = index
                            if(eventDate.difference == 0) return true
                        } 
                    });
                    context.commit('saveCurrentEvent', response.data.results[eventDate.index])
                    resolve(response.data.results[eventDate.index])
                })
                .catch((error) => {
                    console.log(error)
                    context.commit('saveErrors', error.message)
                    reject(error)
                })
        })
    },

    fetchCurrentEventStudentsList(context, eventId) {
        return new Promise((resolve, reject) => {
            HTTP.get('students/event/?event=' + eventId, {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    context.commit('currentEventStudentsList', response.data)
                    resolve(true)
                })
                .catch((error) => {
                    reject(error)
                })
        })
    },

    fetchPastMeetings(context) {
        //console.log(context.state.currentEvent)
        return new Promise((resolve, reject) => {
            HTTP.get('meetings/user/?event=' + context.state.currentEvent.id, {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    context.commit('pastMeetings', response.data)
                    resolve(response)
                })
                .catch((error) => {
                    reject(error)
                })

        })
    },

    getStudentsFromPastMeetings(context, pastMeetings) {
        let studentsFromPastMeetings = Array()
        pastMeetings.forEach((meeting) => {
            studentsFromPastMeetings.push(context.state.currentEventStudentsList.find((student) => {
                return student.id == meeting.student
            }))
        })
        context.commit('studentsFromPastMeetings', studentsFromPastMeetings)
    },

    startMeeting(context, selectedStudentId) {
        if(context.state.pastMeetings.find((meeting) => meeting.student == selectedStudentId)) {
            context.commit('saveErrors', 'Vous avez déjà rencontré l\'étudiant sélectionné')
            return false;
        }
        let data = {
            user: context.state.user.id,
            student: selectedStudentId,
            event: context.state.currentEvent.id,
        }
        let config = {
            headers: {
                'Authorization': 'Token ' + context.state.token,
            },
        }
        return new Promise((resolve, reject) => {
            HTTP.post('meetings/', data, config )
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => {
                    reject(error)
                })
        })
    },

    changeCurrentMeeting(context, data) {
        context.commit('setCurrentMeeting', data)
    }
}