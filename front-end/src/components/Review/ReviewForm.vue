<template>
  <div class="reviewContainer">
    <div class="row" role="main">
        <div v-if="trues">
          <div class="mx-auto w-25 form-floating">
            <input class="form-control" id="moviename" @input="searchMovie" type="text" v-model="movie_titleDirect" >
            <label for="moviename">영화검색</label>
            {{selectDirect()}}
          </div>
        </div>

      <div v-else>
        <h2>리뷰 작성</h2>
        <div class="mx-auto w-25 form-floating" >
          <input class=" form-control" id="moviename" @input="searchMovie" type="text" v-model="movie_title" >
          <label for="moviename">영화검색</label>
        </div>
      </div>      
    </div>

    <form class="m-4" @submit.prevent="onSubmit">
      <div class="row g-3">
        <div class="form-floating col-sm-9 m-3">
          <input class="form-control" id="title" type="text" v-model="title">
          <label for="title">title</label>
        </div>

        <div class="form-floating m-3 col-sm m-3">
          <input class="form-control" id="score" type="number" v-model="score">
          <label for="score">1~5점</label>
        </div>
      </div>

      <div class="form-floating m-3">
        <textarea class="form-control" id="review" type="text" v-model="review" style="height:300px"></textarea>
        <label for="review">review</label>
      </div>
      

      <button class="createBtn">작성</button>
    </form>
    <div v-for="findMovie in findMovies" :key="findMovie.id">
      <p>{{findMovie.title}}</p>
      <!-- <img :src="`https://image.tmdb.org/t/p/w500${findMovie.poster_path}`" alt=""> -->
      <button @click="select(findMovie)">확정</button>
    </div>
    
  </div>
</template>

<script>
export default {
  name : 'ReviewForm',
  data(){
    return {
      title : this.Review.title,	
      review : this.Review.review,	
      movie_title : this.Review.movie_title,	
      poster_path : this.Review.poster_path,	
      score : this.Review.score,
      movie_titleDirect : this.movie.title,
      poster_pathDirect : this.movie.poster_path,
    }
  },
  props : {	
    action : String,	
    Review : Object,	
    movie : Object,
    trues : Boolean,
  },
  methods : {
    createReview(){
      
      const title = this.title
      const review = this.review
      // const movie_title = this.movie_title
      const movie_title = this.$store.getters.selectedMovieTitle
      const poster_path = this.$store.getters.selectedMoviePoster
      console.log(this.$store.getters.selectedMovieTitle)
      const score = this.score
      
      const payload = {
        title, review, movie_title, poster_path, score
      }

      this.$store.dispatch('createReview', payload)
    },
    updateReview(){	
      const title = this.title	
      const review = this.review	
      const movie_title = this.movie_title
      const poster_path = this.poster_path
      const score = this.score	
      const id = this.Review.id	
      const payload = {	
        title, review, movie_title, poster_path, score, id	
      }	
      this.$store.dispatch('updateReview', payload)	
    },
    onSubmit() {	
      if (this.action === 'create') {	
        this.createReview()	
      } else {	
        this.updateReview()	
      }	
    },
    searchMovie(event){
      if (event.target.value) {
       const movie_name = event.target.value
      this.$store.dispatch('searchMovie', movie_name) 
      } else {
        this.$store.dispatch('searchMovie', 'ofkadfkaokokvokovxczovo')
      }
    },
    select(findMovie){
      this.movie_title = findMovie.title
      this.poster_path = findMovie.poster_path
      this.$store.dispatch('selectMovie', findMovie)
    },
    selectDirect() {
      this.$store.dispatch('selectMovie', this.movie)
    }
  },
  computed : {
    findMovies(){
      return this.$store.getters.searchMovie
    },
    findMovieImg(){ 
      return `https://image.tmdb.org/t/p/w500${this.$store.getters.searchMovie.poster_path}`
    },

  },
  created() {
    this.$store.dispatch('setSelectedMovie')
    this.$store.dispatch('setSearchMovies')
  }
}
</script>

<style>
.reviewContainer{
  height: 500px;
  width: 1000px;
  margin-left: auto;
  margin-right: auto ;
  margin-top: 100px ;
}
.createBtn{
  background: rgba(102,152,203,1);
  background: -moz-linear-gradient(top, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(102,152,203,1)), color-stop(100%, rgba(92,138,184,1)));
  background: -webkit-linear-gradient(top, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  background: -o-linear-gradient(top, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  background: -ms-linear-gradient(top, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  background: linear-gradient(to bottom, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#6698cb', endColorstr='#5c8ab8', GradientType=0 );
  color: white;
  display: inline-block;
  position: relative;
  text-shadow: rgba(0, 0, 0, 0.15) 0px 1px 0px;
  text-decoration: none;
  padding: 10px 30px;
  border-width: 1px 1px 4px;
  border-style: solid;
  border-color: rgba(0, 0, 0, 0.21);
  border-image: initial;
  border-bottom: 4px solid rgba(0, 0, 0, 0.21);
  border-radius: 4px;
  font-size: 12px;
  padding: 4px 12px;
}
.createBtn:active {
  background: #608FBF;
}
</style>