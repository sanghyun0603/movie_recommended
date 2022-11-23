<template>
  <div>
    <!-- <h2>리뷰 수정</h2> -->
    <ReviewForm
    :Review="Review" action="update"
    :movie="movie" :trues="false"
    />
  </div>
</template>

<script>
import ReviewForm from '@/components/Review/ReviewForm'

export default {
  name : 'ReviewUpdateView',
  components : {
     ReviewForm,
  },
  computed : {
    Review() {
      return this.$store.getters.review
    },
    movie() {
    return this.$store.getters.movie 
  },
  }
}
</script>

<style>

</style>