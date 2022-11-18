<template>
  <div>
    <router-link :to="{name : 'MovieDetailView', params : {id : movie.id} }">{{movie.title}}</router-link>
  </div>
</template>

<script>
export default {
    name : 'MoviesListItem',
    props : {
      movie : Object
    }
}
</script>

<style>

</style>