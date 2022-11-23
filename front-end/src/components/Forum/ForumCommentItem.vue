<template>
  <div>
    {{forumComment.nickname}}
    {{forumComment.content}}
    <button v-if="!isUpdate" @click="updateForumComment">수정</button>
    <div v-if="isUpdate">
      <ForumCommentUpdateForm
      :comment-all="forumComment"
      />
    </div>
    <button v-if="!isUpdate" @click="deleteFourmComment">삭제</button>
    
  </div>
</template>

<script>
import ForumCommentUpdateForm from './ForumCommentUpdateForm.vue'

export default {
 name : 'ForumCommentItem',
 data() {
  return {
    isUpdate : false,
  }
 },
 components : {
  ForumCommentUpdateForm,
 },
 props : {
  forumComment : Object,
 },
 methods : {
  deleteFourmComment() {
    this.$store.dispatch('deleteFourmComment', this.forumComment.id)
  },
  updateForumComment() {
    this.isUpdate = !this.isUpdate
  }
 }
}
</script>

<style>

</style>