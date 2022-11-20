<template>
  <div>
    <h2>ReviewForm</h2>
    <form @submit.prevent="onSubmit">
      <label for="title">title</label>
      <input id="title" type="text" v-model="title">

      <label for="review">review</label>
      <input id="review" type="text" v-model="review">
      
      <label for="movie_title">movie_title</label>
      <input id="movie_title" type="text" v-model="movie_title">
      
      <label for="poster_path">poster_path</label>
      <input id="poster_path" type="text" v-model="poster_path">
      
      <label for="score">score</label>
      <input id="score" type="number" v-model="score">

      <input type="submit">
    </form>
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
    }
  },
  props : {
    action : String,
    Review : Object,
  },
  methods : {
    createReview(){
      const title = this.title
      const review = this.review
      const movie_title = this.movie_title
      const poster_path = this.poster_path
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
    }
  }
}
</script>

<style>

</style>