<template>
    <div>
        <h2>Travaux de {{ this.getCurrentStudent.first_name }} {{ this.getCurrentStudent.last_name }}</h2>
        <div class="loading" v-if="loading">
            Loading...
        </div>
        <div v-else>
            <ul>
                <li v-for="implementation in getCurrentStudentImplementations" :key="implementation.id">
                    {{ implementation.project }}
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
            }
        },
        computed: {
            ...mapGetters([
                'getCurrentMeeting',
                'getCurrentStudent',
                'getCurrentStudentImplementations',
                'getState',
            ]),
        },
        methods: {
            fetchData() {
                this.loading = true
                this.$store.dispatch('fetchStudentImplementations', this.getCurrentStudent.id)
                    .then((response) => {
                        console.log(response)
                        this.loading = false
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            }
        },
        created() {
            this.fetchData()
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

