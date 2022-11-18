<template>
  <div>
    <h2>댓글작성</h2>
    <form @submit.prevent="forumCommentCreate">
    <label for="ForumComment">댓글 쓰기</label>
    <input type="text" id="ForumComment" v-model="content">
    <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
export default {
  name : 'ForumCommentForm',
  props : {
    forumId : Number,
  },
  data() {
    return {
      content : null,
    }
  },
  methods  : {
    forumCommentCreate() {
      const content = this.content
      const forumId = this.forumId
      const payload = {
        content, forumId
      }
      this.$store.dispatch('forumCommentCreate',payload)
    }
  }
}
</script>

<style>

</style>