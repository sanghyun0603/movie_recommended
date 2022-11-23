<template>
  <div class="detail_all">
    <div class="detail_page">
      <div class="detail_info">
        <h1 >{{movie.title}}</h1>
        <h2>장르 : <span v-for="genre in movieGenres" :key="genre.id">{{ genre.name }},</span></h2>
        <h3>출연진 : <span v-for="actor in movieActors" :key="actor.id">{{ actor.name }},</span></h3>
        <h3>개봉일 : {{movie.release_date}}</h3>
        <h3><img src="@/assets/stars.png" alt="평점" style="width:50px; height:40px;"> : {{movie.vote_average	}}</h3>
        <h3>좋아요 : {{likeUsers}} </h3>
      <div v-if="movie.like_users.includes(user.pk)">
        <h2 type="button" @click="likesMovie"><img alt="likes" src="@/assets/heart (2).png" style="width:30px; height:30px;"></h2>
      </div>
      <div v-else>
        <h2 type="button" @click="likesMovie"><img alt="likes" src="@/assets/heart (1).png" style="width:30px; height:30px;"></h2>
      </div>
        <iframe width="560" height="315" :src="movieYoutube"></iframe>
      </div>
      <div class="posterimg">
      <img :src="movieImg" alt="">
      </div>
    </div>
    <div class="detail_page">
      <div class="overview">
        <p  id="over" >{{movie.overview}}</p>
      </div>
    </div>
    <div class="detail_page">
      <p> <router-link :to="{ name: 'ReviewCreateView', params : { action : 'direct'} }">리뷰 작성하러 가기</router-link></p>
      
    </div>
      
      
      
      

  </div>
</template>

<script>
export default {
  name : 'MovieDetailView',
  computed : {
  movie() {
    return this.$store.getters.movie 
  },
  movieImg(){
    return `https://image.tmdb.org/t/p/w400${this.$store.getters.movie.poster_path}`
  },
  movieYoutube(){
    return `https://www.youtube.com/embed/${this.$store.getters.movie.youtube_key}`
  },
  movieActors(){
    return this.$store.getters.actors 
  },
  movieGenres(){
    return this.$store.getters.detailGenres
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
    this.$store.dispatch('getMovieDetail', this.$route.params.movieId)
    this.$store.dispatch('getMovieActors', this.$route.params.movieId)
    this.$store.dispatch('getMovieGenres', this.$route.params.movieId)
  },
}
</script>

<style scoped>
h1 {
  font-size: 50px;
}
.detail_all {
  background-color: #36454f;
  color:#ffffff;
}
#over {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: break-word;
  
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
.detail_info {
  width:100%;
  float: left;
  padding: 10px;
  text-align: left;
}
.posterimg {
  width:70%;
  float:left;
  margin-right : 30px;
  text-align: right;
  padding-top:92px;
}
.detail_page {
  width : 100%;
  padding : 10px;
  top: 10px;
  left: 50%;
  margin : auto;
  overflow: hidden;
  display: flex;
  padding-top: 20px;
}
.overview {
  width: 100%;
  /* line-height: 200%; */
}

</style>