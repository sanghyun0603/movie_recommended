<template>
  <div>
    {{forumComment.nickname}}
    {{forumComment.content}}
    <button @click="deleteFourmComment">삭제</button>
  </div>
</template>

<script>
export default {
 name : 'ForumCommentItem',
 props : {
  forumComment : Object,
 },
 methods : {
  deleteFourmComment() {
    this.$store.dispatch('deleteFourmComment', this.forumComment.id)
  }
 }
}
</script>

<style>

</style>