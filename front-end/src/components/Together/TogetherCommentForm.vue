<template>
  <div>
    <form @submit.prevent="togetherCommentCreate" >
      <label for="TogetherComment">댓글작성 : </label>
      <input type="text" id="TogetherComment" v-model="content">
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
export default {
  name : 'TogetherCommentForm',
  props : {
    togetherId : Number,
  },
  data() {
    return {
      content : null,
    }
  },
  methods : {
    togetherCommentCreate() {
      const content = this.content
      const togetherId = this.togetherId

      const payload = {
        content, togetherId
      }
      this.$store.dispatch('togetherCommentCreate',payload)
    }
  }
}
</script>

<style>

</style>