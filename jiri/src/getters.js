export const getters = {
    getErrors(state) {
        return state.errors
    },
    getToken(state) {
        return state.token
    },
    getUserId(state) {
        return state.user.id
    },
    getHomePageUrl(state) {
        if(state.user.is_admin) {
            return 'dashboard';
        }
        return 'meetings';
    }
}