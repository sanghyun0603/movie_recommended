<template>
  <div>
    <h2>ForumView</h2>
    <router-link :to="{ name : 'ForumCreateView'}">CREATE</router-link> <br>
    <router-link :to="{ name : 'ForumUpdateView' }">UPDATE</router-link> <br>
    <ForumList/>
  </div>
</template>

<script>
import ForumList from '@/components/Forum/ForumList'

export default {
  name : 'ForumView',
  components : {
    ForumList,
  },
  created() {
      this.$store.dispatch('getForums')
  },
}
</script>

<style>

</style>