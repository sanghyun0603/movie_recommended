<template>
  <div>
    <router-link :to="{ name : 'ForumDetailView', params : { id : forum.id} }"><h3>{{forum.title}}</h3></router-link>
    <p>{{forum.nickname}}</p>
  </div>
</template>

<script>
export default {
  name : 'ForumListItem',
  props : {
    forum : Object,
  }
}
</script>

<style>

</style>