<template>
  <div>
    {{togetherComment.content}}
    <button @click="deleteTogetherComment">삭제</button>
  </div>
</template>

<script>
export default {
 name: 'TogetherCommentItem',
 props : {
  togetherComment : Object, 
},
 methods : {
  deleteTogetherComment() {
    this.$store.dispatch('deleteTogetherComment',this.togetherComment.id)
  }
 }
}
</script>

<style>

</style>