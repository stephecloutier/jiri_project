<template>
    <div>
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <div class="main-content" v-else>
            <div>
                <span class="h2-like">{{ this.getCurrentEvent.course_name + ' - ' + this.getCurrentEvent.exam_date }}</span>
                <br>
                <select id="event" v-model="selectedEventId">
                    <option v-for="event in this.getEvents" :key="event.id" :value="event.id">
                        {{ event.course_name + ' - ' + event.exam_date }}
                    </option>
                </select>
                <input type="submit" @click.prevent="changeCurrentEvent" value="Changer d'épreuve">
            </div>
            <div class="create-meeting">
                <h2>Rencontrer un étudiant</h2>
                <select name="students" v-model="selectedStudentId">
                    <option v-for="student in this.getCurrentEventStudentsList" :key="student.id" :value="student.id" selected>
                        {{ student.first_name + ' ' + student.last_name }}
                    </option>
                </select>
                <input type="submit" value="Débuter la rencontre" @click.prevent="startMeeting">
            </div>
            
            <div class="past-meetings">
                <h2>Étudiants déjà rencontrés</h2>
                <div v-if="getPastMeetings == false">
                        Vous n'avez encore rencontré aucun étudiant, débutez une rencontre&nbsp;!
                </div>
                <ul v-else>
                    <li v-for="student in this.getStudentsFromPastMeetings" :key="student.id" @click.prevent="getMeeting(student.id)">
                        {{ student.first_name + ' ' + student.last_name }}
                    </li>
                </ul>
            </div>
        </div>

        <!-- To handle later on -->
        <!-- <div class="errors" v-if="getErrors">
            <span v-for="error in getErrors" :key="error.index">{{ error }}</span>
        </div> -->
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import {router} from '../router'

    export default {
        name: 'meetings',
        data() {
            return {
                loading: false,
                selectedStudentId: null,
                selectedEventId: undefined,
            }
        },
        computed: {
            ...mapGetters([
                'getEvents',
                'getCurrentEvent',
                'getErrors',
                'getCurrentEventStudentsList',
                'getPastMeetings',
                'getStudentsFromPastMeetings',
                'getState',
            ]),
        },

        created() {
            this.fetchData()
        },
        methods: {
            fetchData() {
                this.$store.dispatch('fetchAllEvents')
                this.loading = true
                this.$store.dispatch('fetchClosestEvent')
                    .then((response) => {
                        this.$store.dispatch('fetchCurrentEventStudentsList', response.id)
                            .then((response) => {
                                this.loading = false
                            }).catch((error) => {
                                console.log(error)
                            })
                           this.$store.dispatch('fetchPastMeetings')
                                .then((response) => {
                                    this.$store.dispatch('getStudentsFromPastMeetings', this.getPastMeetings)
                                }).catch((error) => {
                                    console.log(error)
                                })
                    }).catch((error) => {
                        console.log(error)
                    })
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
                this.$store.dispatch('fetchCurrentEventStudentsList', newEvent.id)
                    .then((response) => {
                        this.loading = false
                    }).catch((error) => {
                        console.log(error)
                    })
                this.$store.dispatch('fetchPastMeetings')
                    .then((response) => {
                        this.$store.dispatch('getStudentsFromPastMeetings', this.getPastMeetings)
                    }).catch((error) => {
                        console.log(error)
                    })
            },
            changeSelectedStudent($event) {
                this.selectedStudent = $event
            },
            startMeeting() {
                if(this.selectedStudentId == undefined) {
                    console.log('Vous devez sélectionner un étudiant!')
                    return
                }
                this.$store.dispatch('startMeeting', this.selectedStudentId)
                    .then((response) => {
                        if(response) {
                            this.$store.dispatch('changeCurrentMeeting', response.data)
                            this.$store.dispatch('setCurrentStudent', this.selectedStudentId)
                            router.push({ path: `/meetings/${response.data.id}` })
                        }
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
            getMeeting(id) {
                let studentMeeting = this.getPastMeetings.find((meeting) => {
                    return meeting.student == id
                })
                this.$store.dispatch('changeCurrentMeeting', studentMeeting.id)
                this.$store.dispatch('setCurrentStudent', studentMeeting.student)
                router.push({ path: `/meetings/${studentMeeting.id}` })
            },
        },
        beforeRouteLeave (to, from, next) {
            if(to.meta.admin && !this.getState.user.is_admin) {
                next(false)
            } else {
                next()
            }
        }
    }
</script>
