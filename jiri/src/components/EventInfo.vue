<template>
  <div>
    <h2>Création d'une épreuve</h2>

    <label for="course_name">Nom du cours</label>
    <input type="text" id="course_name" v-model="info.course_name">
    <br>
    <label for="exam_date">Date</label>
    <input type="date" v-model="info.exam_date">
    <br>
    <span class="label-like">Session</span>
    <input type="radio" name="exam_session" id="1" value="1" v-model="info.exam_session">
    <label class="inline-label" for="1">1<sup>ère</sup> session</label>
    <input type="radio" name="exam_session" id="2" value="2" v-model="info.exam_session">
    <label class="inline-label" for="2">2<sup>e</sup> session</label>
    <br>

    <a class="button" @click.prevent="next">Suite</a>
  </div>
</template>

<script>
import {router} from '../router'

export default {
  name: 'event-info',
  props: ['event'],
  data() {
    return {
      info: {
        course_name: this.event.course_name,
        exam_session: this.event.exam_session,
        exam_date: this.event.exam_date,
      }
    }
  },
  methods: {
    next() {
      router.push({path: '/events/add/projects'})
    }
  },
  updated() {
    this.$emit('update', this.info)
  },
  created() {
  }
}
</script>

<style>

.label-like {
  display: block;
  margin: 1em 0 0.5em;
  color: #2C003D;
  font-family: "Dosis", Helvetica, arial, sans-serif;
  font-weight: 600;
}
</style>
