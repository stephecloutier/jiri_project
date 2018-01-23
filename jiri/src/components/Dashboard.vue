<template>
    <div>
        <div v-if="this.loading">
            Loading...
        </div>
        <div v-else>
            <div v-if="this.loadingErrors != false">
                <p v-for="error in this.loadingErrors" :key="error.index">
                    {{ error }}
                </p>
                <a @click.prevent="navigate('events/add')">Créer une épreuve</a>
            </div>
            <div v-else-if="!this.todayEvent">
                <h2>Il n'y a pas d'épreuve prévue aujourd'hui.</h2>
                <p class="h2-like">Créez une épreuve ou sélectionnez-en une dans la liste</p>
                <a @click.prevent="navigate('events/add')">Créer une épreuve</a>
                <br>
                <select id="event" v-model="selectedEventId">
                    <option v-for="event in this.getEvents" :key="event.id" :value="event.id">
                        {{ event.course_name + ' - ' + event.exam_date }}
                    </option>
                </select>
                <input type="submit" @click.prevent="changeCurrentEvent" value="Changer d'épreuve">
            </div>
            <div v-else>
                <h2>État du jury {{ this.getCurrentEvent.course_name + ' - ' + this.getCurrentEvent.exam_date }}</h2>
                <select id="event" v-model="selectedEventId">
                    <option v-for="event in this.getEvents" :key="event.id" :value="event.id">
                        {{ event.course_name + ' - ' + event.exam_date }}
                    </option>
                </select>
                <input type="submit" @click.prevent="changeCurrentEvent" value="Changer d'épreuve">
                [dashboard]
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import {router} from '../router'

    export default {
        name: 'dashboard',
        data() {
            return {
                loadingErrors: [],
                todayEvent: false,
                selectedEventId: undefined,
                loading: false,
            }
        },
        computed: {
            ...mapGetters([
                'getEvents',
                'getCurrentEvent',
                'getErrors',
                'getState',
            ]),
        },
        methods: {
            init() {
                this.loading = true
                this.$store.dispatch('fetchAllEvents')
                    .then((response) => {
                        if(response.data == false) {
                            this.loading = false
                            this.loadingErrors.push('Il n\'y a aucune épreuve de prévue dans la base de données.')
                            return
                        }
                        this.$store.dispatch('fetchClosestEvent')
                            .then((response) => {
                                this.loading = false
                                console.log(response)
                            }).catch((error) => {
                                console.log(error)
                        })

                }).catch((error) => {
                    console.log(error)
                })   
            },
            navigate(path) {
                router.push(path)
            },
            changeCurrentEvent() {
                if(this.selectedEventId == undefined) {
                    console.log('Vous devez sélectionner un évènement!')
                    return
                }
                this.loading = true
                let newEvent = this.getEvents.find((event) => {
                    return event.id == this.selectedEventId
                })
                this.$store.dispatch('changeCurrentEvent', newEvent)
                this.getDashboard(newEvent.id)
                this.todayEvent = true
            },
            getDashboard(eventId) {
                this.loading = false
                console.log(eventId)
            }
        },
        created () {
            this.init()
        },
    }
</script>