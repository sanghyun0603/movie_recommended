<template>
  <div>
    <h2>ReviewDetailView</h2>
    {{review.title}}
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
    }
  }
}
</script>

<style>

</style>