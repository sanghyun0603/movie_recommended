<template>
  <div class="home">

    <label for="moviename">홈에서 영화검색</label>
    <input id="moviename" @input="searchMovieHome" type="text">

    <div v-for="findMovie in findMovies" :key="findMovie.id">
      <p><a :href="`http://localhost:8080/showmovie/${findMovie.id}`"> {{findMovie.title}}</a></p>
      <!-- <img :src="`https://image.tmdb.org/t/p/w500${findMovie.poster_path}`" alt=""> -->
      <!-- <button @click="select(findMovie)">확정</button> -->
      <!-- <a :href="findMovieId">{{}}</a> -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'HomeView',
  components: {
  },
  methods : {
    searchMovieHome(event){
      if (event.target.value) {
        const movie_name = event.target.value
      this.$store.dispatch('searchMovieHome', movie_name)
      } else {
        this.$store.dispatch('searchMovieHome', 'dsofkasozvoxckvoxckvo')
      }
    },
  },
  computed : {
    findMovies(){
      return this.$store.getters.searchMovieHome
    },
    findMovieImg(){ 
      return `https://image.tmdb.org/t/p/w500${this.$store.getters.searchMovieHome.poster_path}`
    },
    findMovieId(){
      return `http://localhost:8080/showmovie/`
    }
  },
  created() {
    this.$store.dispatch('resetSearchMovieHome')
  }
  
}
</script>
