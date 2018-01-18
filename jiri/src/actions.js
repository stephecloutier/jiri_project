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
        //console.log(context)
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
                    resolve(response)
                })
                .catch((error) => {
                    console.log(error)
                    context.commit('saveErrors', error.message)
                    reject(error)
                })
        })
    },

    fetchCurrentEventStudentsList(context) {
        return new Promise((resolve, reject) => {
            //console.log(context.state.token)

            HTTP.get('students/', {
                headers: {
                    'Authorization': 'Token ' + context.state.token
                }
            })
                .then((response) => {
                    let currentEventStudents = response.data.results.filter((student) => {
                        return (context.state.currentEvent.students.find((id) => {return student.id == id})) == undefined ? false : true 
                    })
                    context.commit('currentEventStudentsList', currentEventStudents)
                    resolve(true)
                })
                .catch((error) => {
                    reject(error)
                })
        })
    }
}