<template>
  <div>
    <h2>좋아요한 자유글</h2>
    <div v-for="(forum,idxForum) in userLikesForums" :key="idxForum">
      {{forum.title}}
    </div>
  </div>
</template>

<script>
export default {
 name : 'ProfileLikeForum',
 props : {
  userLikesForums : Array,
 }
}
</script>

<style>

</style>