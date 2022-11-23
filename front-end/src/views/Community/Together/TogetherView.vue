<template>
  <div class="togetherContainer">
    <h2>구해요 게시판</h2>
    <TogetherList/>
    <router-link :to="{ name : 'TogetherCreateView'}">CREATE</router-link>
  </div> 
</template>

<script>
import TogetherList from '@/components/Together/TogetherList'

export default {
  name : 'TogetherView',
  components : {
    TogetherList,
  },
  created() {
    this.$store.dispatch('getTogethers')
  }
}
</script>

<style>
.togetherContainer{
  height: 500px;
  width: 1000px;
  margin-left: auto;
  margin-right: auto ;
  margin-top: 100px ;
}
</style>