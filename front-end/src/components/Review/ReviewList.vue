<template>
  <div>
    <h2>ReviewList</h2>
    <ReviewListItem
    v-for="review in Reviews" :key="review.id"
    :review="review"
    />
  </div>
</template>

<script>
import ReviewListItem from '@/components/Review/ReviewListItem'

export default {
  name : 'ReviewList',
  components : {
    ReviewListItem,
  },
  computed : {
    Reviews(){
      return this.$store.getters.reviews
    }
  },
}
</script>

<style>

</style>