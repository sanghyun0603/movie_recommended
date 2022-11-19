<template>
  <div>
    <h2>ForumCreateView</h2>
    <ForumForm
    :forum="forum" action="create"
    />
  </div>
</template>

<script>
import ForumForm from '@/components/Forum/ForumForm'

export default {
  name : 'ForumCreateView',
  components : {
    ForumForm,
  },
  data() {
    return {
      forum : {id:null, title:'', content:''}
    }
  }
}
</script>

<style>

</style>