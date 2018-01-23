export const getters = {
    getState(state) {
        return state
    },
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
    },
    getStudents(state) {
        return state.students
    },
    getProjects(state) {
        return state.projects
    },
    getUsers(state) {
        return state.users
    },
    getEvents(state) {
        return state.events
    },
    getCurrentEvent(state) {
        return state.currentEvent
    },
    getCurrentEventStudentsList(state) {
        return state.currentEventStudentsList
    },
    getPastMeetings(state) {
        return state.pastMeetings
    },
    getStudentsFromPastMeetings(state) {
        return state.studentsFromPastMeetings
    },
    getCurrentMeeting(state) {
        return state.currentMeeting
    },
    getCurrentStudent(state) {
        return state.currentStudent
    },
    getCurrentStudentImplementations(state) {
        return state.currentStudentImplementations
    },
    getCurrentImplementation(state) {
        return state.currentImplementation
    },
    getCurrentScore(state) {
        return state.currentScore
    },
}