<template>
    <div>
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <div class="main-content" v-else>
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
        <div class="errors" v-if="getErrors">
            <span v-for="error in getErrors" :key="error.index">{{ error }}</span>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import router from '../router'

    export default {
        name: 'meetings',
        data() {
            return {
                loading: false,
                selectedStudentId: null,
            }
        },
        computed: {
            ...mapGetters([
                'getErrors',
                'getCurrentEventStudentsList',
                'getPastMeetings',
                'getStudentsFromPastMeetings',
            ]),
        },
        created () {
            this.fetchData()
        },
        methods: {
            fetchData() {
                this.loading = true
                this.$store.dispatch('fetchClosestEvent')
                    .then((response) => {
                        this.$store.dispatch('fetchCurrentEventStudentsList')
                            .then((response) => {
                                this.selectedStudentId = this.getCurrentEventStudentsList[0].id
                                this.loading = false
                            }).catch((error) => {
                                console.log(error)
                            })
                    }).catch((error) => {
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
                console.log($event)
            },
            startMeeting() {
                this.$store.dispatch('startMeeting', this.selectedStudentId)
                    .then((response) => {
                        if(response) {
                            router.push(response.data.id + '/')
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
                router.push(studentMeeting.id + '/')
            }
        }
    }
</script>
