<template>
  <div>
    {{together.title}}
    {{endtims}}
    <!-- 업데이트 -->
    <router-link :to="{ name : 'TogetherUpdateView'}">UPDATE</router-link> <br>
    <!-- 좋아요 -->
    <p>좋아요 누른 사람 : {{likeUsers}} </p>
    <div v-if="together.like_users.includes(user.pk)">
      <button @click="likesTogether">좋아요 취소</button>
    </div>
    <div v-else>
      <button @click="likesTogether">좋아요</button>
    </div>
    <!-- 삭제 -->
    <button @click="deleteTogether">삭제</button>
    <!-- 맵컴포넌트 -->
    <TogetherMap
    :map-lat="together.map_lat"
    :map-lng="together.map_lng"
    />
    <hr>
    <!-- 댓글 -->
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
    },
    user() {
      return this.$store.getters.user
    },
    likeUsers() {
      return (this.together?.like_users.length)
     
    },
  },
  methods : {
    deleteTogether() {
      this.$store.dispatch('deleteTogether', this.together.id )
    },
    likesTogether() {
      this.$store.dispatch('likesTogether', this.together.id)
    },
  }
}
</script>

<style>

</style>