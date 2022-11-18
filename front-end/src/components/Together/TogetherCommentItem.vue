<template>
  <div>
    {{togetherComment.content}}
  </div>
</template>

<script>
export default {
 name: 'TogetherCommentItem',
 props : {
  togetherComment : Object, 
}
}
</script>

<style>

</style>