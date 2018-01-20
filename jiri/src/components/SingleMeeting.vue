<template>
    <div>
        <h2>Travaux de []</h2>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import router from '../router'

    export default {
        name: 'SingleMeeting',
        data() {
            return {
                //currentMeetingId: ''
            }
        },
        computed: {
            ...mapGetters([
                'getCurrentMeeting',
            ]),
        },
        methods: {
            fetchData() {
                //this.$store.dispatch('fetchStudentImplementation', )
            }
        },
        created() {
            //this.currentMeetingId = this.$store.state.currentMeetingId
            
        }
    }
</script>

