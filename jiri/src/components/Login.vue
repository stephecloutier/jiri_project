<template>
    <div>
        <input type="email" v-model="currentUser.email" @keyup.enter="login">
        <input type="password" v-model="currentUser.password" @keyup.enter="login">
        <input type="submit" value="Se connecter" v-on:click="login">
        <div class="errors" v-if="getErrors">
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
                currentUser: {email: '', password: ''},
            }
        },
        computed: {
            ...mapGetters([
                'getErrors',
                'getUserId',
                'getHomePageUrl',
            ]),
        },
        methods: {
            login() {
                this.$store.dispatch('login', this.currentUser)
                    .then((response) => {
                        this.currentUser = {email: '', password: ''}
                        this.$store.dispatch('getUserInfo', response.data.id)
                            .then((response) => {
                                router.push(this.getHomePageUrl)
                            }).catch((error) => {
                                console.log(error)
                            })
                    }).catch((error) => {
                        console.log(error)
                    })
            }
        },
    }
    
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->



