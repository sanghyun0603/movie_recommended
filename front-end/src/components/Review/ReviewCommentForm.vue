<template>
  <div>
    <h3>댓글작성</h3>
    <form @submit.prevent="reviewCommentCreate" >
      <label for="ReviewComment">댓글 쓰기</label>
      <input type="text" id="ReviewComment" v-model="content">
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
export default {
  name : 'ReviewCommentForm',
  props : {
    reviewId : Number
  },
  data() {
    return {
      content : null,
    }
  },
  methods : {
    reviewCommentCreate() {
      const content = this.content
      const reviewId = this.reviewId

      const payload = {
        content,reviewId
      }
      this.$store.dispatch('reviewCommentCreate',payload)
    }
  }
}
</script>

<style>

</style>