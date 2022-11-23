<template>
  <div>
    <h2>ForumDetailView</h2>
    {{forum.title}}
    <router-link :to="{ name : 'ForumUpdateView' }">UPDATE</router-link> <br>
    <p>좋아요 누른 사람 : {{this.likeUsers}} </p>
    <div v-if="forum.like_users.includes(user.pk)">
      <button @click="likesForum" class=" badge bg-primary">좋아요 취소</button>
      
    </div>
    <div v-else>
      <button @click="likesForum" class=" badge bg-primary">좋아요</button>
    </div>
    <a href="#" data-bs-toggle="modal" data-bs-target="#reveiwDeleteModal">
      <span class=" badge bg-danger">삭제</span>
      
    </a>
    
    <ForumComment
    :forum-comments="forum.forumcomment_set"
    :forum-id="forum.id"
    />

    <div class="modal fade" id="reveiwDeleteModal" tabindex="-1" aria-labelledby="reveiwDeleteModalLabel" aria-hidden="true">
        <div class="modal-dialog">
        <div class="modal-content">

            <div class="modal-body">
            <p>리뷰를 삭제하시겠습니까?</p>
            </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
            <button class=" btn btn-danger" @click="deleteForum" data-bs-dismiss="modal">삭제</button>
            </div>
        </div>
        </div>
    </div>
  </div>
</template>

<script>
import ForumComment from '@/components/Forum/ForumComment'
import router from '@/router'

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
    },
    user() {
      return this.$store.getters.user
    },
    likeUsers() {
      return (this.forum?.like_users.length)
     
    },
  },
  methods : {
    deleteForum() {
      this.$store.dispatch('deleteForum', this.forum.id)
    },
    likesForum() {
      this.$store.dispatch('likesForum', this.forum.id)
    }
  }
}
</script>

<style>

</style>