<template>
  <div>
    <h2>댓글수정</h2>
    <form @submit.prevent="forumCommentUpdate">
    <input type="text" id="ForumComment" v-model="content">
    <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
export default {
  name : 'ForumCommentUpdateForm',
  props : {
    commentAll : Object,
  },
  data() {
    return {
      content : this.commentAll.content,
    }
  },
  methods  : {
    forumCommentUpdate() {
      const content = this.content
      const commentId = this.commentAll.id
      const payload = {
        content, commentId
      }
      this.$store.dispatch('forumCommentUpdate',payload)
    }
  }
}
</script>

<style>

</style>