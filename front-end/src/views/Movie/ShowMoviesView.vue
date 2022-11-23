<template>
<div v-if="this.$store.state.loadingStatus">
      <LoadingBar :loading="this.$store.state.loadingStatus"></LoadingBar>
</div>
  <div v-else>
    <MoviesListSwiper/>
    <span v-for="(genremovies, idx) in selgenremovies" :key="idx">
      <MoviesList
      :genre-movies="genremovies"
      :genre="showGenres[idx]"
      />
    </span>
</div>
</template>

<script>
import MoviesList from '@/components/Movie/MoviesList'
import MoviesListSwiper from '@/components/Movie/MoviesListSwiper'
import LoadingBar from '@/components/LoadingBar'
export default {
  name : 'ShowMoviesView',
  components : {
    MoviesList,
    MoviesListSwiper,
    LoadingBar,
  },
  computed : {
      selgenremovies(){
        return this.$store.getters.recommendMovies
      },
      showGenres(){
        return this.$store.getters.showGenres
      },
    },
  created(){
    //검색기능
    this.$store.dispatch('getMovies')
  },
}
</script>

<style>

</style>