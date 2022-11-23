<template>
  <div>
    <a :href="bestMovieId">{{bestMovie.title}}</a>
    <p><img :src="bestMovieImg" alt=""></p>
  </div>
</template>

<script>
export default {
    name : 'MoviesListItemSwiper',
    props : {
      bestMovie : Object
    },
    computed : {
      bestMovieImg(){
        return `https://image.tmdb.org/t/p/w500${this.bestMovie.poster_path}`
      },
      bestMovieId(){
        return `http://localhost:8080/showmovie/${this.bestMovie.id}/`
      }
    }
    
}
</script>

<style>

</style>