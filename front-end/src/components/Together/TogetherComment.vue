<template>
  <div>
    <h4>댓글</h4>
    <TogetherCommentItem
    v-for="togethercomment in togetherComments" :key="togethercomment.id"
    :together-comment="togethercomment"
    />
    <TogetherCommentForm
    :together-id="togetherId"
    />
  </div>
</template>

<script>
import TogetherCommentItem from '@/components/Together/TogetherCommentItem.vue'
import TogetherCommentForm from '@/components/Together/TogetherCommentForm'

export default {
  name : 'TogetherComment',
  components : {
    TogetherCommentItem,
    TogetherCommentForm,
  },
  props : {
    togetherComments : Array,
    togetherId : Number,
  }
}
</script>

<style>

</style>