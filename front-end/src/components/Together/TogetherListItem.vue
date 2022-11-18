<template>
  <div>
    <router-link :to="{ name : 'TogetherDetailView', params : { id : together.id} }"><h3>{{together.title}}</h3></router-link>
    <p>{{together.nickname}}</p>
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