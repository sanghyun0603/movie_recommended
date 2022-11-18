<template>
  <div>
    <h2> MovieDetailView</h2>
    {{movie.title}}
    <p>{{movie.overview}}</p>
  </div>
</template>

<script>
export default {
  name : 'MovieDetailView',
  computed : {
    movie() {
      return this.$store.getters.movie
    }
  },
  created(){
    this.$store.dispatch('getMovieDetail', this.$route.params.id)
  }
}
</script>

<style>

</style>