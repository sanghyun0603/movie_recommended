<template>
  <label id="genre">
    <div :class="{'afterBtn':want}" class="genreBtn">
      <span id="genreSpan">
        <input id="genreInput" type="checkbox" @change="check" @click="genreSelect" :value="genre.name" v-model="want">
        {{genre.name}}
      </span>
    </div>
  </label>
</template>

<script>
export default {
    name : 'GenreListItem',
    props : {
      genre : Object,
      all : Number,
    },
    data(){
      return {
        selected : 0,
        want : false,
      }
    },
    methods : {
      genreSelect(){
        if (this.want === false) {
          this.$store.commit('INCREASE_GENRE')
          return this.$store.getters.selectedGenres.push(this.genre.id)
        }
        else if (this.want === true){
          this.$store.commit('DECREASE_GENRE')
          this.$store.dispatch('deleteGenre', this.genre.id)
        }
      },
      check(){
        console.log(this.$store.getters.selectGenreNum);
        console.log(this.want);
        console.log(this.genre.name);
        if(this.$store.getters.selectGenreNum>=6){
          alert('5개 넘기지 마셈')
          this.want = !this.want
          this.$store.commit('DECREASE_GENRE')
          this.$store.dispatch('deleteGenre', this.genre.id)
        }
      },
    },
}
</script>

<style scoped>
.genreBtn{
  border-radius: 100px;
  height: 45px;
  width: 150px;
  margin: 10px;
  background: rgba(240,210,100,1);
  background: -webkit-gradient(linear, 0 0, 0 100%, from(rgba(240,210,100,1)), to(rgba(229,201,96,1)));
  background: -webkit-linear-gradient(rgba(240,210,100,1) 0%, rgba(229,201,96,1) 100%);
  background: -moz-linear-gradient(rgba(240,210,100,1) 0%, rgba(229,201,96,1) 100%);
  background: -o-linear-gradient(rgba(240,210,100,1) 0%, rgba(229,201,96,1) 100%);
  background: linear-gradient(rgba(240,210,100,1) 0%, rgba(229,201,96,1) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f0d264', endColorstr='#e5c960', GradientType=0 );
}
.afterBtn{
  border-radius: 100px;
  height: 45px;
  width: 150px;
  margin: 10px;
  font-weight: bold;
  background: rgba(255,105,30,1);
  background: -webkit-gradient(linear, 0 0, 0 100%, from(rgba(255,105,30,1)), to(rgba(230,95,28,1)));
  background: -webkit-linear-gradient(rgba(255,105,30,1) 0%, rgba(230,95,28,1) 100%);
  background: -moz-linear-gradient(rgba(255,105,30,1) 0%, rgba(230,95,28,1) 100%);
  background: -o-linear-gradient(rgba(255,105,30,1) 0%, rgba(230,95,28,1) 100%);
  background: linear-gradient(rgba(255,105,30,1) 0%, rgba(230,95,28,1) 100%);
}
#genreInput{
  display: none;
}
#genreSpan{
  display: inline-grid;
  margin: 10px;
}
</style>