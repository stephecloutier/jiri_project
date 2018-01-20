<template>
  <div>
    <h2>Création d'une épreuve</h2>

    <a @click.prevent="next">Suite</a>
  </div>
</template>

<script>
import {router} from '../router'

export default {
  name: 'event-info',
  methods: {
    next() {
      router.push({path: '/events/add/projects'})
    }
  }
}
</script>
