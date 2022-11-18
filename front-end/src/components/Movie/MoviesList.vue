<template>
  <div>
    <h2>ShowMovies</h2>
    <MoviesListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MoviesListItem from '@/components/Movie/MoviesListItem'
export default {
    name : 'MoviesList',
    components : {
      MoviesListItem,
    },
    computed : {
      movies(){
        return this.$store.getters.movies
      }
    }
}
</script>

<style>

</style>