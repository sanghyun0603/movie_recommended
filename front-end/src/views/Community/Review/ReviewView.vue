<template>
  <div class="reviewContainer">
    <h2>영화 리뷰</h2>
    <ReviewList/>
    <router-link :to="{ name : 'ReviewCreateView', params : { action : 'newCreate'} }">리뷰쓰러가기</router-link>
  </div>
</template>

<script>
import ReviewList from '@/components/Review/ReviewList'


export default {
  name : 'ReviewView',
  components : {
    ReviewList,
  },
  created() {
      this.$store.dispatch('getReviews')
  },
  computed:{
    createUrl(){
      return 'http://localhost:8080/review/create'
    }
  },
}
</script>

<style scoped>
.reviewContainer{
  height: 500px;
  width: 1000px;
  margin-left: auto;
  margin-right: auto ;
  margin-top: 100px ;
}
</style>