<template>
  <div>
    <div id="genreContainer">
      <h3>보고싶은 장르를 선택하세요</h3>
      <GenreListItem
        v-for="genre in genres"
        :key="genre.id"
        :genre="genre"
        :all="all"
      />
    </div>
      <button class="selectBtn" @click="pick">선택완료</button>
  </div>
</template>

<script>
import GenreListItem from '@/components/Movie/GenreListItem'
export default {
    name : 'GenreList',
    data(){
      return{
        all : 0
      }
    },
    components : {
      GenreListItem,
    },
    computed : {
      genres(){
        return this.$store.getters.genres
      }
    },
    methods : {
      pick(){
        this.$store.dispatch('selectGenres')
        this.$store.dispatch('selectGenresNum')
        this.$router.push({ name: 'ShowMoviesView'})
      },
    },
}
</script>

<style scoped>
#genreContainer{
  width: 700px;
  height: 370px;
  margin-left: auto;
  margin-right: auto;
}
button{
  background:#C3DFE0;
  color:#fff;
  border:none;
  position:relative;
  height:60px;
  font-size:1.6em;
  padding:0 2em;
  cursor:pointer;
  transition:800ms ease all;
  outline:none;
  border-radius: 100px;
}
button:hover{
  background:#fff;
  color:#C3DFE0;
}
button:before,button:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #C3DFE0;
  transition:400ms ease all;
}
button:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
button:hover:before,button:hover:after{
  width:100%;
  transition:800ms ease all;
}
</style>