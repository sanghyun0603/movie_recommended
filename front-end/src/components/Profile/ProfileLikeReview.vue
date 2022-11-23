<template>
  <div>
    <h2>좋아요한  리뷰글</h2>
    <div v-for="(review,idxReview) in userLikesReviews" :key="idxReview+'l'">
      {{review.title}}
    </div>
  </div>
</template>

<script>
export default {
  name : 'ProfileLikeReview',
  props: {
    userLikesReviews : Array,
  }
}
</script>

<style>

</style>