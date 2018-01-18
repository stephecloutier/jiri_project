import {HTTP} from './http-common'

export const actions = {
    login({commit}, user) {
        HTTP.post('get_auth_token/', {
            username: user.email,
            password: user.password
        })
            .then((response) => {
                commit('saveToken', response.data.token)
            })
            .catch((error) => {
                commit('saveErrors', error.response.data)
            })
    }
}