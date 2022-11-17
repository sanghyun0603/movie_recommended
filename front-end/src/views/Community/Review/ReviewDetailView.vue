<template>
  <div>
    <h2>ReviewDetailView</h2>
    <ReviewComment/>
  </div>
</template>

<script>
import ReviewComment from '@/components/Review/ReviewComment'

export default {
  name : 'ReviewDetailView',
  components: {
    ReviewComment,
  }
}
</script>

<style>

</style>