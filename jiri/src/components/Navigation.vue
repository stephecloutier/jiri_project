<template>
<div>
    <div class="main-nav">
        <a @click.prevent="goToHome">
            <svg version="1.1" id="svg_logo" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
        viewBox="0 0 225 164" xml:space="preserve">
                <g>
                    <path d="M70.7,35H47.6c-1.9,0-2.9,1.1-2.9,3.2c0,2.3,1,3.5,2.9,3.5h19.5v62.7c0,14-6.6,21.1-19.6,21.1c-5.8,0-10.6-1.4-14.2-4.3
                        c-3.6-2.8-5.5-6.9-5.6-12.2c0-1.9-1.2-2.9-3.5-2.9c-2.3,0-3.5,1.2-3.5,3.6c0,6.5,2.5,11.9,7.3,16.1c4.9,4.2,11.4,6.3,19.5,6.3
                        c8,0,14.4-2.2,19.2-6.7c4.8-4.4,7.2-11.5,7.2-21.1V38.1C74,36.1,72.9,35,70.7,35z"/>
                    <path d="M102.9,65.9c-2.2,0-3.4,0.9-3.4,2.8v60.1c0,0.8,0.3,1.6,1,2.2c0.7,0.6,1.4,0.9,2.4,0.9s1.7-0.3,2.4-1c0.7-0.7,1-1.4,1-2.1
                        V68.7C106.4,66.8,105.3,65.9,102.9,65.9z"/>
                    <path d="M102.9,35c-1.5,0-2.8,0.5-3.8,1.5c-1,1-1.5,2.1-1.5,3.4c0,1.4,0.5,2.6,1.5,3.6c1,1,2.3,1.5,3.8,1.5c1.4,0,2.6-0.5,3.6-1.5
                        c1-1,1.5-2.2,1.5-3.6c0-1.3-0.5-2.4-1.5-3.4C105.6,35.5,104.3,35,102.9,35z"/>
                    <path d="M162.6,65.1h-5c-4.4,0-8.2,1-11.5,3.1c-3.3,2.1-5.8,4.6-7.5,7.7v-7.1c0-0.8-0.3-1.5-1-2c-0.7-0.5-1.4-0.8-2.4-0.8
                        c-2.2,0-3.4,0.9-3.4,2.8v60.1c0,0.8,0.3,1.6,1,2.2c0.7,0.6,1.4,0.9,2.4,0.9c0.9,0,1.7-0.3,2.4-1c0.7-0.7,1-1.4,1-2.1V91.9
                        c0-6.1,1.9-11,5.7-14.7c3.8-3.8,8.2-5.7,13.2-5.7h5c0.8,0,1.6-0.3,2.2-0.9c0.6-0.6,0.9-1.4,0.9-2.3c0-0.9-0.3-1.7-0.9-2.3
                        C164.2,65.4,163.5,65.1,162.6,65.1z"/>
                    <path d="M190.5,36.5c-1-1-2.2-1.5-3.6-1.5c-1.5,0-2.8,0.5-3.8,1.5c-1,1-1.5,2.1-1.5,3.4c0,1.4,0.5,2.6,1.5,3.6c1,1,2.3,1.5,3.8,1.5
                        c1.4,0,2.6-0.5,3.6-1.5c1-1,1.5-2.2,1.5-3.6C192,38.6,191.5,37.4,190.5,36.5z"/>
                    <path d="M186.8,65.9c-2.2,0-3.4,0.9-3.4,2.8v60.1c0,0.8,0.3,1.6,1,2.2c0.7,0.6,1.4,0.9,2.4,0.9s1.7-0.3,2.4-1c0.7-0.7,1-1.4,1-2.1
                        V68.7C190.3,66.8,189.2,65.9,186.8,65.9z"/>
                    <path d="M168.2,37.1h-46.8c-1.6,0-2.8,1.3-2.8,2.8s1.3,2.8,2.8,2.8h46.8c1.6,0,2.8-1.3,2.8-2.8S169.8,37.1,168.2,37.1z"/>
                </g>
            </svg>
        </a>
        <span @click.prevent="logout" class="logout" v-if="this.getState.token">Déconnexion</span>
    </div>
    <div class="admin-nav" v-if="this.getState.user.is_admin">
        <router-link :to="{name:'dashboard'}" class="admin-nav__link">État du jury</router-link>
        <router-link :to="{name:'event-info'}" class="admin-nav__link">Créer une nouvelle épreuve</router-link>
        <router-link :to="{name:'events'}" class="admin-nav__link">Voir toutes les épreuves</router-link>
        <router-link :to="{name:'projects'}" class="admin-nav__link">Gérer les travaux</router-link>
        <router-link :to="{name:'students'}" class="admin-nav__link">Gérer les étudiants</router-link>
        <router-link :to="{name:'users'}" class="admin-nav__link">Gérer les jurés</router-link>
        <router-link :to="{name:'meetings'}" class="admin-nav__link">Rencontrer un étudiant</router-link>
    </div>
</div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import {router} from '../router'

    export default {
        name: 'navigation',
        computed: {
            ...mapGetters([
                'getState'
            ])
        },
        methods: {
            logout() {
                this.$store.dispatch('logout')
            },
            goToHome() {
                if(this.getState.user.is_admin) {
                    router.push({path: '/dashboard'})
                } else {
                    router.push({path: '/meetings'})
                }
            }
        }
    }
</script>

<style>
.main-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 70%;
    max-width: 70%;
    margin: 0 auto;
}
.admin-nav {
    color: white;
    margin: 2rem auto 0;
    max-width: 70%;
    width: 70%;
    display: flex;
    align-items: center;
    justify-content: space-between
}
.admin-nav__link {
    color: white;
    text-decoration: none;
    font-weight: 600;
    font-size: 1rem;
}
[id='svg_logo'] {
    fill: white;
    max-width: 100px;
}
.logout {
    color: white;
    text-decoration: none;
    cursor: pointer;
    font-weight: 600;
    font-size: 1.25rem;
}
</style>
