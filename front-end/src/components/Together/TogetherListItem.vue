<template>
  <div>
    <a :href="`http://localhost:8080/together/${together.id}/`"><h3>{{together.title}}</h3></a>
    <router-link :to="{ name : 'ProfileView', params : { username : together.username} }"><p>{{together.nickname}}</p></router-link>
  </div>
</template>

<script>
export default {
  name : 'TogetherListItem',
  props : {
    together : Object,
  }
}
</script>

<style>

</style>