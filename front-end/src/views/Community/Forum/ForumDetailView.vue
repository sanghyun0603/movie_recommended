<template>
  <div>
    <h2>ForumDetailView</h2>
    {{forum.title}}
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
      return this.$store.state.forum
    }
  }
}
</script>

<style>

</style>