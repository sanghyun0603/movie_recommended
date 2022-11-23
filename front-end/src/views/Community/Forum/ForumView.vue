<template>
  <div class="forumContainer">
    <h2>자유게시판</h2>
    <ForumList/>
    <router-link class="forumCreate" :to="{ name : 'ForumCreateView'}">글쓰러가기</router-link>
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

<style scoped>
.forumContainer{
  height: 1000px;
  width: 1500px;
  margin-left: auto;
  margin-right: auto ;
  margin-top: 100px ;
}
</style>