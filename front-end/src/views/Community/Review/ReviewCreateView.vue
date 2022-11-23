<template>
  <div>
    <!-- <h2>리뷰 쓰기</h2> -->
    <div v-if="$route.params.action === 'direct'">
      <ReviewForm
    :Review="Review" action="create"
    :movie="movie" :trues="true"
    />
    </div>
    <div v-else>
      <ReviewForm
    :Review="Review" action="create"
    :movie="movie" :trues="false"
    />
    </div>
    
  </div>
</template>

<script>
import ReviewForm from '@/components/Review/ReviewForm'

export default {
  name : 'ReviewCreateView',
  components : {
    ReviewForm,
  },
  data() {
    return {
      Review : {id:null, title :'',review:'',movie_title: null,poster_path:null,score:null,}
    }
  },
  computed : {
    movie() {
    return this.$store.getters.movie 
  },
  }
}

</script>

<style>

</style>