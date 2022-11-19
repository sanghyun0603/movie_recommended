<template>
  <div>
    <h2>TogetherView</h2>
    <router-link :to="{ name : 'TogetherCreateView'}">CREATE</router-link> <br>
    
    <TogetherList/>
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

</style>