<template>
    <!-- <form action="." method="POST"> -->
        <div>
            <input type="email">
            <input type="password">
            <input type="submit" value="Se connecter" v-on:click="login">
        </div>
    <!-- </form> -->
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import {HTTP} from '../http-common'
    import Cookies from 'js-cookie'

    export default {
        name: 'login',
        computed: {
            ...mapGetters([
                'getTest',
            ]),
        },
        methods: {
            login() {
                const token = ''
                //const csrftoken = Cookies.get('csrftoken')
                HTTP.post('get_auth_token/', {
                    username: 'user@mail.com',
                    password: 'motdepasse'
                })
                    .then((response) => {
                        this.token = response.data.token
                        console.log(this.token)
                        //localStorage.setItem('token', response.data.token)
                        HTTP.get('users/', {
                            headers: {
                                'Authorization': 'Token ' + this.token
                            }
                        })
                            .then((response) => {
                                console.log(response)
                                //localStorage.setItem('token', response.data.token)
                            })
                            .catch((error) => {
                                //console.log("Error login")
                                console.log(error)
                            })
                    })
                    .catch((error) => {
                        //console.log("Error login")
                        console.log(error)
                    })
            }
        }
    }

    
</script>
