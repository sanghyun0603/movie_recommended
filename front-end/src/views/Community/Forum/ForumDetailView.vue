<template>
  <div>
    <h2>ForumDetailView</h2>
    {{forum.title}}
    <router-link :to="{ name : 'ForumUpdateView' }">UPDATE</router-link> <br>
    <button @click="deleteForum">삭제</button>
    <ForumComment
    :forum-comments="forum.forumcomment_set"
    :forum-id="forum.id"
    />
  </div>
</template>

<script>
import ForumComment from '@/components/Forum/ForumComment'

export default {
  name : 'ForumDetailView',
  components : {
    ForumComment,
  },
  created() {
    this.$store.dispatch('getForumDetail', this.$route.params.id)
  },
  computed : {
    forum() {
      return this.$store.getters.forum
    }
  },
  methods : {
    deleteForum() {
      this.$store.dispatch('deleteForum', this.forum.id)
    }
  }
}
</script>

<style>

</style>