<template>
  <div>
    <h2>TogetherList</h2>
    <TogetherListItem
    v-for="together in Togethers" :key="together.id"
    :together="together"
    />
  </div>
</template>

<script>
import TogetherListItem from '@/components/Together/TogetherListItem'

export default {
  name : 'TogetherList',
  components : {
    TogetherListItem,
  },
  computed : {
    Togethers() {
      return this.$store.getters.togethers
    }
  }
}
</script>

<style>

</style>