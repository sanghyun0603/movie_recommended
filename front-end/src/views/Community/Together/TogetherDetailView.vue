<template>
  <div>
    <h2>TogetherDetailView</h2>
    {{together.title}}
    {{endtims}}
    <router-link :to="{ name : 'TogetherUpdateView'}">UPDATE</router-link> <br>
    <button @click="deleteTogether">삭제</button>
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
    this.$store.dispatch('getTogetherDetail', this.$route.params.id)
  },
  computed : {
    together() {
      return this.$store.getters.together
    },
    endtims() {
      const togetherEndtime = this.together.endtime
      console.log(this.together.endtime)
      const date = new Date(togetherEndtime)
      const output = `${date.getFullYear()}년 ${date.getMonth()+1}월 ${date.getDate()}일 ${date.getHours()}시 ${date.getMinutes()}분까지`
      return output
    }
  },
  methods : {
    deleteTogether() {
      this.$store.dispatch('deleteTogether', this.together.id )
    }
  }
}
</script>

<style>

</style>