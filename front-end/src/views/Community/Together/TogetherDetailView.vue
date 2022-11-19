<template>
  <div>
    <h2>TogetherDetailView</h2>
    {{together.title}}
    {{together.endtime}}
    <TogetherMap
    :map-lat="together.map_lat"
    :map-lng="together.map_lng"
    />
    <hr>
    <TogetherComment
    :together-comments="together.togethercomment_set"
    :together-id="together.id"
    />
  </div>
</template>

<script>
import TogetherComment from '@/components/Together/TogetherComment.vue'
import TogetherMap from '@/components/Together/TogetherMap.vue'
export default {
  name : 'TogetherDetailView',
  components: {
    TogetherComment,
    TogetherMap,
  },
  created() {
    console.log(this.$route.params.id)
    this.$store.dispatch('getTogetherDetail', this.$route.params.id)
  },
  computed : {
    together() {
      return this.$store.getters.together
    },
  }
}
</script>

<style>

</style>