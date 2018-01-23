<template>
    <div>
        <div v-if="this.loading">
            Loading...
        </div>
        <div v-else>
            <div v-if="this.loadingErrors != false">
                <p v-for="error in this.loadingErrors" :key="error.index">
                    {{ error }}
                </p>
                <a @click.prevent="navigate('events/add')">Créer une épreuve</a>
            </div>
            <div v-else-if="!this.todayEvent">
                <h2>Il n'y a pas d'épreuve prévue aujourd'hui.</h2>
                <p class="h2-like">Créez une épreuve ou sélectionnez-en une dans la liste</p>
                <a @click.prevent="navigate('events/add')">Créer une épreuve</a>
                <br>
                <select id="event" v-model="selectedEventId">
                    <option v-for="event in this.getEvents" :key="event.id" :value="event.id">
                        {{ event.course_name + ' - ' + event.exam_date }}
                    </option>
                </select>
                <input type="submit" @click.prevent="changeCurrentEvent" value="Changer d'épreuve">
            </div>
            <div v-else>
                <h2>État du jury {{ this.getCurrentEvent.course_name + ' - ' + this.getCurrentEvent.exam_date }}</h2>
                <select id="event" v-model="selectedEventId">
                    <option v-for="event in this.getEvents" :key="event.id" :value="event.id">
                        {{ event.course_name + ' - ' + event.exam_date }}
                    </option>
                </select>
                <input type="submit" @click.prevent="changeCurrentEvent" value="Changer d'épreuve">
                <div v-if="this.dashboardLoading"> 
                    Loading...
                </div>
                <div v-else>
                    <table class="dashboard">
                        <tr>
                            <th>Étudiants v - Jurés ></th>
                            <th v-for="user in users" :key="user.id">
                                {{ user.first_name + ' ' + user.last_name }}
                            </th>
                        </tr>
                        <tr v-for="student in students" :key="student.id">
                            <th>
                                {{ student.first_name + ' ' + student.last_name }}
                            </th>
                            <td v-for="user in users" :key="user.id">
                                {{ getScore(user.id, student.id) }}
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import {router} from '../router'

    export default {
        name: 'dashboard',
        data() {
            return {
                loadingErrors: [],
                todayEvent: false,
                selectedEventId: undefined,
                loading: false,
                dashboardLoading: false,
                users: [],
                students: [],
            }
        },
        computed: {
            ...mapGetters([
                'getEvents',
                'getCurrentEvent',
                'getErrors',
                'getState',
                'getCurrentMeetings',
                'getUsers',
                'getStudents',
                'getProjects',
                'getImplementations',
                'getScores',
            ]),
        },
        methods: {
            init() {
                this.loading = true
                this.dashboardLoading = true
                this.$store.dispatch('fetchAllEvents')
                    .then((response) => {
                        if(response.data == false) {
                            this.loading = false
                            this.loadingErrors.push('Il n\'y a aucune épreuve de prévue dans la base de données.')
                            return
                        }
                        this.$store.dispatch('fetchClosestEvent')
                            .then((response) => {
                                this.loading = false
                                this.getDashboard(response.data.id)
                            }).catch((error) => {
                                //console.log(error)
                        })

                }).catch((error) => {
                    console.log(error)
                })   
            },
            navigate(path) {
                router.push(path)
            },
            changeCurrentEvent() {
                if(this.selectedEventId == undefined) {
                    console.log('Vous devez sélectionner un évènement!')
                    return
                }
                this.loading = true
                let newEvent = this.getEvents.find((event) => {
                    return event.id == this.selectedEventId
                })
                this.$store.dispatch('changeCurrentEvent', newEvent)
                this.getDashboard(newEvent.id)
                this.todayEvent = true
            },
            getDashboard(eventId) {
                this.loading = false
                this.$store.dispatch('getCurrentMeetings', eventId)
                    .then((response) => {
                        this.fetchData()
                    }).catch((error) => {
                        console.log(error)
                    })
            },
            fetchData() {
                this.$store.dispatch('fetchAllUsers')
                    .then((response) => {
                        this.$store.dispatch('fetchAllStudents')
                            .then((response) => {
                                this.fillUsersAndStudents()
                                this.$store.dispatch('fetchAllProjects')
                                    .then((response) => {
                                        this.$store.dispatch('fetchAllImplementations')
                                            .then((response) => {
                                                this.$store.dispatch('fetchAllScores')
                                                    .then((response) => {
                                                        this.dashboardLoading = false
                                                    }).catch((error) => {
                                                        console.log(error)
                                                    })
                                            }).catch((error) => {
                                                console.log(error)
                                            })
                                    }).catch((error) => {
                                        console.log(error)
                                    })
                            }).catch((error) => {
                                console.log(error)
                            })
                    }).catch((error) => {
                        console.log(error)
                    })
            },
             fillUsersAndStudents() {
                this.getCurrentEvent.users.forEach((eventUser) => {
                    this.users.push(this.getUsers.find((user) => {
                        return user.id == eventUser
                    }))
                })
                this.getCurrentEvent.students.forEach((eventStudent) => {
                    this.students.push(this.getStudents.find((student) => {
                        return student.id == eventStudent
                    }))
                })
            },
            getScore(userId, studentId) {
                let meeting = this.findMeeting(userId, studentId)
                if(!meeting) return
                let globalEval = this.getProjects.find((project) => {
                    return project.is_default
                })
                let implementation = this.getImplementations.find((implementation) => {
                    return implementation.event == this.getCurrentEvent.id && implementation.student == studentId && implementation.project == globalEval.id
                })
                let score = this.getScores.find((score) => {
                    return score.meeting == meeting.id && score.implementation == implementation.id
                })
                return score.score
                
            },
            findMeeting(userId, studentId) {
                return this.getCurrentMeetings.find((meeting) => {
                    return meeting.student == studentId && meeting.user == userId
                })
            }
        },
        created () {
            this.init()
        },
    }
</script>

<style>
.dashboard {
    border-collapse: collapse;
}
.dashboard tr, .dashboard th, .dashboard td {
    padding: 1em;
    border: 2px solid black;
}

</style>
