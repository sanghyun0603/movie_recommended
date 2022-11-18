<template>
  <div>
    {{reviewComment.content}}
  </div>
</template>

<script>
export default {
  name:'ReviewCommentItem',
  props : {
    reviewComment : Object
  }
}
</script>

<style>

</style>