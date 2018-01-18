<template>
    <div>
        <h1>Bravo tu es connecté</h1>
        <h2>{{ getToken }}</h2>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    //import router from '../router'

    export default {
        name: 'home',
        computed: {
            ...mapGetters([
                'getToken',
            ]),
        },
        created () {
            //this.$store.dispatch('getHome')
        },
    }
</script>
