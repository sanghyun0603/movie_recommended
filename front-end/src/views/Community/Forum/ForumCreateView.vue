<template>
  <div class ="forumCreateContainer">
    <h2>글쓰기</h2>
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
.forumCreateContainer{
  height: 500px;
  width: 1000px;
  margin-left: auto;
  margin-right: auto ;
  margin-top: 100px ;
}
</style>