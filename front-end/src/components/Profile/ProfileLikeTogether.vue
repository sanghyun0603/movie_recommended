<template>
  <div>
    <h2>좋아요한 구해요글</h2>
    <div v-for="(together,idxTogether) in userLikesTogethers" :key="idxTogether+'r'">
      {{together.title}}
    </div>
  </div>
</template>

<script>
export default {
  name : 'ProfileLikeTogether',
  props : {
    userLikesTogethers : Array,
  }
}
</script>

<style>

</style>