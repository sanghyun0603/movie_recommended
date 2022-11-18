<template>
  <div>
    <h2>ForumForm</h2>
    <form @submit.prevent="createForum">
      <label for="title">title</label>
      <input id="title" type="text" v-model="title">

      <label for="content">content</label>
      <input id="content" type="text" v-model="content">

      <input type="submit">
    </form>
  </div>
</template>

<script>
export default {
  name : 'ForumForm',
  data(){
    return {
      title : null,
      content : null,
    }
  },
  methods : {
    createForum(){
      const title = this.title
      const content = this.content

      const payload = {
        title, content
      }
      this.$store.dispatch('createForum', payload)
    }
  }
}
</script>

<style>

</style>