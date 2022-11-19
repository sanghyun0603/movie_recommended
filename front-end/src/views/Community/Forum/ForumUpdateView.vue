<template>
  <div>
    <h2>ForumUpdateView</h2>
    <ForumForm
    :forum="forum" action="update"
    />
  </div>
</template>

<script>
import ForumForm from '@/components/Forum/ForumForm'

export default {
  name : 'ForumUpdateView',
  components : {
    ForumForm,
  },
  computed : {
    forum() {
      return this.$store.getters.forum
    }
  }
}
</script>

<style>

</style>