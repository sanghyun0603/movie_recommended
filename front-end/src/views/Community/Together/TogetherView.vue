<template>
  <div>
    <h2>TogetherView</h2>
    <router-link :to="{ name : 'TogetherCreateView'}">CREATE</router-link> <br>
    <router-link :to="{ name : 'TogetherUpdateView'}">UPDATE</router-link> <br>
    <router-link :to="{ name : 'TogetherDetailView'}">DETAIL</router-link>
    <TogetherList/>
  </div> 
</template>

<script>
import TogetherList from '@/components/Together/TogetherList'

export default {
  name : 'TogetherView',
  components : {
    TogetherList,
  }
}
</script>

<style>

</style>