<template>
  <div>
    <h2>Toutes les épreuves</h2>
    <div v-if="this.loading">
      Loading...
    </div>
    <ul v-else>
      <li v-for="event in this.getEvents" :key="event.id" @click.prevent="updateEvent(event.id)">
        {{ event.course_name }} - {{ event.exam_date }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import router from '../router'


export default {
  name: 'events',
  data() {
    return {
      loading: true,
    }
  },
  computed: {
    ...mapGetters([
      'getEvents'
    ])
  },
  methods: {
    fetchEvents() {
      this.loading = true
      this.$store.dispatch('fetchAllEvents')
        .then((response) => {
          this.loading = false
        })
        .catch((error) => {
          console.log(error)
        })
    },
    updateEvent() {
      console.log('updateEvent')
    },
  },
  created() {
    this.fetchEvents()
  },
}
</script>
