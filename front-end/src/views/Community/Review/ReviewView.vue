<template>
  <div>
    <h2>ReviewView</h2>
    <router-link :to="{ name : 'ReviewCreateView'}">CREATE</router-link> <br>
    <router-link :to="{ name : 'ReviewUpdateView'}">UPDATE</router-link> <br>
    <router-link :to="{ name : 'ReviewDetailView'}">DETAIL</router-link> <br>  
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/Review/ReviewList'


export default {
  name : 'ReviewView',
  components : {
    ReviewList,
  }
}
</script>

<style>

</style>