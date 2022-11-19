<template>
  <div>
    <a :href="`http://localhost:8080/together/${together.id}/`"><h3>{{together.title}}</h3></a>
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