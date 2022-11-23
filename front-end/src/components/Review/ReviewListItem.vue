<template>
  <div>
    <!-- <router-link :to="{ name : 'ReviewDetailView', params : { id : review.id} }"><h3>{{review.title}}</h3></router-link> -->
    <a :href="`http://localhost:8080/review/${review.id}/`">{{ review.title }}</a>
    <router-link :to="{ name : 'ProfileView', params : { username : review.username} }"><p>{{review.nickname}}</p></router-link>
    
  </div>
</template>

<script>


export default {
  name : 'ReviewListItem',
  props : {
    review : Object,
  }
}
</script>

<style>

</style>