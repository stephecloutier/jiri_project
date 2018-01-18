<template>
    <div>
        <input type="email" v-model="user.email">
        <input type="password" v-model="user.password" @keyup.enter="login">
        <input type="submit" value="Se connecter" v-on:click="login">

        <div class="errors">
            <span v-for="error in getErrors" :key="error.index">{{ error }}</span>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import router from '../router'

    export default {
        name: 'login',
        data() {
            return {
                user: {email: '', password: ''}
            }
        },
        computed: {
            ...mapGetters([
                'getErrors',
            ]),
        },
        methods: {
            login() {
                this.$store.dispatch('login', this.user).then(() => {
                    this.$router.replace('home')
                }).catch((error) => {
                    console.log(error)
                })
                this.user = {email: '', password: ''}
            }
        }
    }
    
</script>


