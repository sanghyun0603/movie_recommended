<template>
  <div>
    <h2>ReviewComment</h2>
    <ReviewCommentItem
    v-for="reviewcomment in reviewComments" :key="reviewcomment.id"
    :review-comment="reviewcomment"
    />
    <ReviewCommentForm
    :review-id="reviewId"
    />
  </div>
</template>

<script>
import ReviewCommentItem from '@/components/Review/ReviewCommentItem'
import ReviewCommentForm from '@/components/Review/ReviewCommentForm'

export default {
  name : 'ReviewComment',
  components : {
    ReviewCommentItem,
    ReviewCommentForm,
  },
  props : {
    reviewComments : Array,
    reviewId : Number,
  }
}
</script>

<style>

</style>