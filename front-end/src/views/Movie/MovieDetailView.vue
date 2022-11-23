<template>
  <div>
    <h2> MovieDetailView</h2>
    {{movie.title}}
    <p>좋아요 누른 사람 : {{likeUsers}} </p>
    <div v-if="movie.like_users.includes(user.pk)">
      <button @click="likesMovie">좋아요 취소</button>
    </div>
    <div v-else>
      <button @click="likesMovie">좋아요</button>
    </div>
    <p v-for="actor in movieActors" :key="actor.id">{{ actor.name }}</p>
    <p>{{movie.overview}}</p>
    
    <router-link :to="{ name: 'ReviewCreateView', params : { action : 'direct'} }">리뷰 작성</router-link>

    <iframe width="560" height="315" :src="movieYoutube"></iframe>
    <img :src="movieImg" alt="">
  </div>
</template>

<script>
export default {
  name : 'MovieDetailView',
  props: ["movieId"],
  computed : {
  movie() {
    return this.$store.getters.movie 
  },
  movieImg(){
    return `https://image.tmdb.org/t/p/w500${this.$store.getters.movie.poster_path}`
  },
  movieYoutube(){
    return `https://www.youtube.com/embed/${this.$store.getters.movie.youtube_key}`
  },
  movieActors(){
    return this.$store.getters.actors 
  },
  user() {
      return this.$store.getters.user
    },
  likeUsers() {
      return (this.movie.like_users.length)
    },
  userProfile() {
    return this.$store.getters.userProfile
  },
  },
  methods : {
    likesMovie() {
      this.$store.dispatch('likesMovie', this.movie.id)
    }
  },
  created(){
    console.log(this.movidId)
    this.$store.dispatch('getMovieDetail', this.movieId)
    this.$store.dispatch('getMovieActors', this.movieId)
  },
}
</script>

<style scoped>

</style>