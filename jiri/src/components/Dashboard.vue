<template>
    <div>
        <h2>État du jury</h2>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    //import {router} from '../router'

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