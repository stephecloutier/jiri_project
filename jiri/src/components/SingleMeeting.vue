<template>
    <div>
        <h2>Rencontre avec {{ this.getCurrentStudent.first_name }} {{ this.getCurrentStudent.last_name }}</h2>
        <span class="h2-like">Ses travaux</span>
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <div v-else>
            <ul>
                <li v-for="project in this.projects" :key="project.id" @click.prevent="getImplementation(project.id)">
                    {{ project.name }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import {router} from '../router'

    export default {
        name: 'SingleMeeting',
        data() {
            return {
                loading: true,
                projects: [],
            }
        },
        computed: {
            ...mapGetters([
                'getCurrentMeeting',
                'getCurrentStudent',
                'getCurrentStudentImplementations',
                'getState',
                'getProjects',
            ]),
        },
        methods: {
            fetchData() {
                this.loading = true
                this.$store.dispatch('fetchStudentImplementations', this.getCurrentStudent.id)
                    .then((response) => {
                        this.getProjectsInfo()
                        this.loading = false
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
            getProjectsInfo() {
                this.getCurrentStudentImplementations.forEach((implementation) => {
                    this.projects.push(this.getProjects.find((project) => {
                        return implementation.project == project.id
                    }))
                })
            },
            getImplementation(projectId) {
                let implementation = {
                    project: projectId,
                    student: this.getCurrentStudent.id,
                    event: this.getState.currentEvent.id
                }
                this.$store.dispatch('fetchSingleImplementation', implementation)
                    .then((response) => {
                        router.push({ path: `/meetings/${this.getCurrentMeeting.id}/${response.data.id}` })
                    }).catch((error) => {
                        console.log(error)
                    })
            }
        },
        created() {
            this.$store.dispatch('fetchAllProjects')
                .then((response) => {
                    this.fetchData()
                }).catch((error) => {
                    console.log(error)
                })
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

