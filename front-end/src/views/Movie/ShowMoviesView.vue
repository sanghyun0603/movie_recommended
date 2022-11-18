<template>
  <div>
    <h2>ShowMoviesView</h2>
    <MoviesList/>
  </div>
</template>

<script>
import MoviesList from '@/components/Movie/MoviesList'
export default {
  name : 'ShowMoviesView',
  components : {
    MoviesList
  },
  created(){
    this.$store.dispatch('getMovies')
  },
}
</script>

<style>

</style>