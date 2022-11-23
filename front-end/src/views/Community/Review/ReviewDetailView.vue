<template>
  <div>
    <h2>ReviewDetailView</h2>
    {{review.title}}
    {{review.movie_title}}
    <!-- <img :src="review.poster_path" alt=""> -->
    <!-- <img :src=`https://image.tmdb.org/t/p/w500${}` alt=""> -->
    <img :src="`https://image.tmdb.org/t/p/w500${review.poster_path}`" alt="">
    <router-link :to="{ name : 'ReviewUpdateView'}">UPDATE</router-link> <br>	
    <p>좋아요 누른 사람 : {{ likeUsers }}</p>
    <div v-if="review.like_users.includes(user.pk)">
      <button @click="likesReview">좋아요 취소</button>
      
    </div>
    <div v-else>
      <button @click="likesReview">좋아요</button>
    </div>
    
    <button @click="deleteReview">삭제</button>
    <ReviewComment
    :review-comments="review.reviewcomment_set"
    :review-id="review.id"
    />
  </div>
</template>

<script>
import ReviewComment from '@/components/Review/ReviewComment'

export default {
  name : 'ReviewDetailView',
  components: {
    ReviewComment,
  },
  created() {
    this.$store.dispatch('getReviewDetail', this.$route.params.id)
  },
  computed : {
    review() {
      return this.$store.getters.review
    },
    user() {
      return this.$store.getters.user
    },
    likeUsers() {
      return (this.review?.like_users.length)
     
    }
  },
  methods : {	
    deleteReview() {	
      this.$store.dispatch('deleteReview', this.review.id)	
    },
    likesReview() {
      this.$store.dispatch('likesReview', this.review.id)
    },
  },
  
}
</script>

<style>

</style>