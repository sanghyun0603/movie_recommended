<template>
  <div>
    <h2>당신이 좋아하는 {{this.genre}}장르</h2>
    <swiper
      class="swiper"
      :options="swiperOption">
      <swiper-slide v-for="movie in genreMovies" :key="movie.id" id="swiperSlid">
          <figure class="hover-img">
            <img id="swiperSlidImg" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
              <figcaption >
                <router-view />
              <router-link  :to="`/showmovie/${movie.id}`">
                {{movie.title}}
              </router-link>
              </figcaption> 
          </figure>
      </swiper-slide>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
    </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
    name : 'MoviesList',
    components : {
      Swiper,
      SwiperSlide,
    },
    props : {
      genreMovies : Array,
      genre : String,
    },
    data(){
      return{      
        swiperOption: { 
            grabCursor : "true",
            centeredSlides : "true",
            slidesPerView : 5,
            spaceBetween: 10, 
            loop: true, 
            slidesPerGroup : 5,
            navigation: { 
              nextEl: '.swiper-button-next', 
              prevEl: '.swiper-button-prev' 
          } 
        },
      }
    },
}
</script>

<style scoped>
a {
  color: #FCF7FF;
  font-size: 24px;
  font-family: sans-serif;
  font-weight: 400;
}
.hover-img {
  background-color: #000;
  color: rgb(137, 58, 58);
  display: inline-block;
  margin: 8px;
  max-width: 240px;
  min-width: 220px;
  overflow: hidden;
  position: relative;
  text-align: center;
  width: 100%;
}
/* height: 235px;
width: 220px; */

.hover-img * {
  box-sizing: border-box;
  transition: all 0.45s ease;
}

.hover-img::before,
.hover-img::after {
  background-color: rgba(0, 0, 0, 0.5);
  border-top: 32px solid rgba(0, 0, 0, 0.5);
  border-bottom: 32px solid rgba(0, 0, 0, 0.5);
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  content: '';
  transition: all 0.3s ease;
  z-index: 1;
  opacity: 0;
  transform: scaleY(2);
}

.hover-img img {
  vertical-align: top;
  max-width: 100%;
  backface-visibility: hidden;
}

.hover-img figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  align-items: center;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.1em;
  opacity: 0;
  z-index: 2;
  transition-delay: 0.1s;
  font-size: 24px;
  font-family: sans-serif;
  font-weight: 400;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.hover-img:hover::before,
.hover-img:hover::after {
  transform: scale(1);
  opacity: 1;
}

.hover-img:hover > img {
  opacity: 0.7;
}

.hover-img:hover figcaption {
  opacity: 1;
}
#swiperSlidImg{
  height: 250px;
  width: 240px;
}
</style>