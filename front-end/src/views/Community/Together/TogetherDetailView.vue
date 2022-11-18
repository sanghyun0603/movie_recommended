<template>
  <div>
    <h2>TogetherDetailView</h2>
    {{together.title}}
    <TogetherComment
    :together-comments="together.togethercomment_set"
    :together-id="together.id"
    />
  </div>
</template>

<script>
import TogetherComment from '@/components/Together/TogetherComment.vue'

export default {
  name : 'TogetherDetailView',
  components: {
    TogetherComment,
  },
  created() {
    this.$store.dispatch('getTogetherDetail', this.$route.params.id)
  },
  computed : {
    together() {
      return this.$store.getters.together
    }
  }
}
</script>

<style>

</style>