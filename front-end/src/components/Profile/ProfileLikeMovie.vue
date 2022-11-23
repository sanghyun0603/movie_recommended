<template>
  <div>
    <h2>좋아요한 영화</h2>
    <div v-for="(movie,idxMovie) in userLikesMovies" :key="idxMovie+'c'">
      <img :src="`https://image.tmdb.org/t/p/w200${movie.poster_path}`" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name : 'ProfileLikeMovie',
  props : {
    userLikesMovies : Array,
  }
}
</script>

<style>

</style>