<template>
<div>
    <h2>Ajout d'étudiants</h2>
    <a @click.prevent="next">Suite</a>
</div>
</template>

<script>
import {router} from '../router'

export default {
  name: 'event-students',
  methods: {
    next() {
      router.push({path: '/events/add/users'})
    }
  }
}
</script>
