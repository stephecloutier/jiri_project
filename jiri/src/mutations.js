export const mutations = {
    saveToken(state, token) {
        state.token = token
    },
    saveErrors(state, data) {
        state.errors = data.non_field_errors
    }
}


// HTTP.get('users/', {
//     headers: {
//         'Authorization': 'Token ' + this.token
//     }
// })
//     .then((response) => {
//         console.log(response)
//         //localStorage.setItem('token', response.data.token)
//     })
//     .catch((error) => {
//         console.log(error)
//     })