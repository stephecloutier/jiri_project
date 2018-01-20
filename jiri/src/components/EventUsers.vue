<template>
    <div>
        <h2>Ajout de jurés</h2>
        <a @click.prevent="next">Suite</a>
    </div>
</template>

<script>
export default {
  name: 'event-users',
  methods: {
    next() {
      router.push({path: '/events/add/recap'})
    }
  }
}
</script>
