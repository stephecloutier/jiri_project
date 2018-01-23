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
    fetchAllStudents(context) {
        return new Promise((resolve, reject) => {
            HTTP.get('students/', {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    context.commit('saveAllStudents', response.data.results)
                    resolve(response)
                })
                .catch((error) => {
                    // context.commit('saveErrors', error.response.data)
                    reject(error)
                })
        })
    },

    fetchAllProjects(context) {
        return new Promise((resolve, reject) => {
            HTTP.get('projects/', {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    context.commit('saveAllProjects', response.data.results)
                    resolve(response)
                })
                .catch((error) => {
                    context.commit('saveErrors', error.response.data)
                    reject(error)
                })
        })
    },

    fetchAllUsers(context) {
        return new Promise((resolve, reject) => {
            HTTP.get('users/', {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    context.commit('saveAllUsers', response.data.results)
                    resolve(response)
                })
                .catch((error) => {
                    context.commit('saveErrors', error.response.data)
                    reject(error)
                })
        })
    },

    fetchAllEvents(context) {
        return new Promise((resolve, reject) => {
            HTTP.get('events/', {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    context.commit('saveAllEvents', response.data.results)
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

    changeCurrentEvent(context, event) {
        context.commit('changeCurrentEvent', event)
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

    changeCurrentMeeting(context, id) {
        context.commit('setCurrentMeeting', id)
    },

    setCurrentStudent(context, studentId) {
        let student = context.state.currentEventStudentsList.find((studentItem) => {
            return studentItem.id == studentId
        })
        context.commit('setCurrentStudent', student)
    },

    fetchStudentImplementations(context, studentId) {
        let event = context.state.currentEvent.id
        let config = {
            headers: {
                'Authorization': 'Token ' + context.state.token,
            },
        }
        return new Promise((resolve, reject) => {
            HTTP.get('implementations/student/?student=' + studentId + '&event=' + event, config )
                .then((response) => {
                    context.commit('currentStudentImplementations', response.data)
                    resolve(response)
                })
                .catch((error) => {
                    reject(error)
                })
        })
    },

    createStudent(context, data) {
        let student = {
            first_name: data.first_name,
            last_name: data.last_name,
        }
        let config = {
            headers: {
                'Authorization': 'Token ' + context.state.token,
            },
        }
        return new Promise((resolve, reject) => {
            HTTP.post('students/', student, config )
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => {
                    context.commit('saveErrors', error.response.data)
                    reject(error)
                })
        })
    },

    createProject(context, data) {
        let project = {
            name: data.title,
            description: data.description,
            default_weight: data.weight,
        }
        let config = {
            headers: {
                'Authorization': 'Token ' + context.state.token,
            },
        }
        return new Promise((resolve, reject) => {
            HTTP.post('projects/', project, config )
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => {
                    context.commit('saveErrors', error.response.data)
                    reject(error)
                })
        })
    },

    createUser(context, data) {
        let user = {
            first_name: data.first_name,
            last_name: data.last_name,
            username: data.email,
            password: data.password,
            is_admin: data.is_admin,
        }
        let config = {
            headers: {
                'Authorization': 'Token ' + context.state.token,
            },
        }
        return new Promise((resolve, reject) => {
            HTTP.post('users/', user, config )
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => {
                    context.commit('saveErrors', error.response.data)
                    reject(error)
                })
        })
    },

    createEvent(context, data) {
        let event = {
            course_name: data.course_name,
            exam_session: data.exam_session,
            exam_date: data.exam_date,
            projects: data.projects,
            students: data.students,
            users: data.users,
        }
        let config = {
            headers: {
                'Authorization': 'Token ' + context.state.token,
            },
        }
        return new Promise((resolve, reject) => {
            HTTP.post('events/', event, config )
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => {
                    context.commit('saveErrors', error.response.data)
                    reject(error)
                })
        })
    }
}