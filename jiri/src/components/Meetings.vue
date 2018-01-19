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
            <!--
            <div class="past-meetings" v-if="pastMeetings">
                <h2>Étudiants déjà rencontrés</h2>
                <ul>
                    <li v-for="meeting in pastMeetings" :key="meeting.id" @click.prevent="getMeeting">
                        {{ meeting.student.first_name + meeting.student.last_name }}
                    </li>
                </ul>
            </div>-->
        </div>

        <!-- to handle later
        <div class="errors" v-if="getErrors">
            <span v-for="error in getErrors" :key="error.index">{{ error }}</span>
        </div>-->
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
                'pastMeetings',
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
                        console.log(response)
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
                    console.log(response)
                    router.push('meetings/' + response.data.id)
                })
                .catch((error) => {
                    console.log(error)
                })
            }
        }
    }
</script>
