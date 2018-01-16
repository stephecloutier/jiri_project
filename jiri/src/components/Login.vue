<template>
    <form action="." method="POST">
        <input type="email">
        <input type="password">
        <input type="submit" value="Se connecter">
    </form>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    export default {
        name: 'login',
        computed: {
            ...mapGetters([
                'getTest',
            ]),
        },
    }
    
</script>
