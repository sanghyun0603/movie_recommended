<template>
  <div>
    <h2>SelectGenreView</h2>
    <GenreList/>
  </div>

</template>

<script>
import GenreList from '@/components/Movie/GenreList'
export default {
  name : 'SelectGenreView',
  components : {
    GenreList,
  },
  created(){
    this.$store.dispatch('getGenres')
  }
}
</script>

<style scoped>
h2{
  visibility:hidden 
}
</style>