<template>
  <div>
    <h2>ForumComment</h2>
    <ForumCommentItem
    v-for=" forumComment in forumComments" :key="forumComment.id"
    :forum-comment="forumComment"
    />
    <ForumCommentForm
    :forum-id="forumId"
    />
  </div>
</template>

<script>
import ForumCommentItem from '@/components/Forum/ForumCommentItem'
import ForumCommentForm from '@/components/Forum/ForumCommentForm'

export default {
  name : 'ForumComment',
  props : {
    forumComments : Array,
    forumId : Number
  },
  components : {
    ForumCommentItem,
    ForumCommentForm,
  }
}
</script>

<style>

</style>