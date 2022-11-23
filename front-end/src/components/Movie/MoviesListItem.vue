<template>
  <div>
    <!-- <router-link :to="{name : 'MovieDetailView', params : {id : movie.id} }">{{movie.title}}</router-link> -->
    
    <div class="card" style="width: 18rem;">
      <img :src="movieImg" class="card-img-top" alt="">
    </div>


    <!-- 원래 사용하던 부분입니다 -->
    <!-- <a :href="movieId">{{movie.title}}</a> -->
    <!-- <p><img :src="movieImg" alt=""></p> -->
    <!-- 원래 사용하던 부분입니다 -->
  </div>
  
  <!-- <div class="card p-3 mt-4" style="height: 32rem; width: 18rem;" id="imgHover">
      <div style="object-fit:cover; height:360px">
        <img :src="movie.poster_path" style="height:100%; width:100%">
      </div>
      <div class="card-body">
        <h5 class="card-title text-truncate"><b>{{ movie.title }}</b></h5>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div> -->
</template>

<script>
export default {
    name : 'MoviesListItem',
    props : {
      movie : Object
    },
    computed : {
      movieImg(){
        return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      },
      movieId(){
        return `http://localhost:8080/showmovie/${this.movie.id}/`
      }
    }
}
</script>

<style>

</style>