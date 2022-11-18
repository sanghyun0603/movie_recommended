<template>
  <div>
    <h2>TogetherForm</h2>
    <form @submit.prevent="createTogether">
      <label for="title">title</label>
      <input id='title' type="text" v-model="title">

      <label for="content">content</label>
      <input id='content' type="text" v-model="content">
      
      <!-- 추후에는 컴포넌트 넣어서 주소 검색하면 위도 경도 나올 수 있게 -->
      <!-- const coords = new kakao.maps.LatLng(result[0].y, result[0].x); -->

      <label for="endtime">endtime</label>
      <input id='endtime' type="datetime-local" v-model="endtime">
      
      <input type="submit">
    </form>
    <TogetherFormMap
    @to-form="mapPosi"
    />
  </div>
</template>

<script>
import TogetherFormMap from '@/components/Together/TogetherFormMap'

export default {
  name : 'TogetherForm',
  data(){
    return {
      title : null,
      content : null,
      map_lat : 36.3553193257957,
      map_lng : 127.29820111515,
      endtime : null
    }
  },
  components : {
    TogetherFormMap,
  },
  methods : {
    createTogether(){
      const title = this.title
      const content = this.content
      const map_lat = this.map_lat
      const map_lng = this.map_lng
      const endtime = this.endtime

      const payload = {
        title, content, map_lat, map_lng, endtime
      }

      this.$store.dispatch('createTogether', payload)

    },
    mapPosi(posi) {
      console.log(posi)
    }
  }
}
</script>

<style>

</style>