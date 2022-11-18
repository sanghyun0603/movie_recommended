<template>
  <div>
    {{forumComment.nickname}}
    {{forumComment.content}}
  </div>
</template>

<script>
export default {
 name : 'ForumCommentItem',
 props : {
  forumComment : Object
 }
}
</script>

<style>

</style>