<template>
    <div>
        <h1>Bravo tu es connecté, administrateur !</h1>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    //import router from '../router'

    export default {
        name: 'Dashboard',
        computed: {
            ...mapGetters([
                // 'getToken',
            ]),
        },
        created () {
            //this.$store.dispatch('getHome')
        },
    }
</script>