<template>
  <div>
    <h2>ForumForm</h2>
    <form @submit.prevent="onSubmit">
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
      title : this.forum.title,
      content : this.forum.content,
    }
  },
  props : {
    forum : Object,
    action : String,
  },
  methods : {
    createForum(){
      const title = this.title
      const content = this.content

      const payload = {
        title, content
      }
      this.$store.dispatch('createForum', payload)
    },
    updateForum(){
      const title = this.title
      const content = this.content
      const id = this.forum.id
      const payload = {
        title, content,id
      }
      this.$store.dispatch('updateForum', payload)
    },
    onSubmit() {
      if (this.action === 'create') {
        this.createForum()
      } else {
        this.updateForum()
      }
    }
  }
}
</script>

<style>

</style>