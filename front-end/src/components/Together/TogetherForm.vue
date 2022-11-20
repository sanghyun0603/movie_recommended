<template>
  <div>
    <h2>TogetherForm</h2>
    <form @submit.prevent="onSubmit">
      <label for="title">title</label>
      <input id='title' type="text" v-model="title">

      <label for="content">content</label>
      <input id='content' type="text" v-model="content">
      

      <label for="endtime">endtime</label>
      <input id='endtime' type="datetime-local" v-model="endtime">
      
      <input type="submit">
    </form>
    <TogetherFormMap
    :map-lat="this.map_lat"
    :map-lng="this.map_lng"
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
      title : this.Together.title,
      content : this.Together.content,
      map_lat : this.Together.map_lat,
      map_lng : this.Together.map_lng,
      endtime : this.Together.endtime,
    }
  },
  components : {
    TogetherFormMap,
  },
  props : {
    Together : Object,
    action : String,
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
    updateTogether() {
      const title = this.title
      const content = this.content
      const map_lat = this.map_lat
      const map_lng = this.map_lng
      const endtime = this.endtime
      const id = this.Together.id
      const payload = {
        title, content, map_lat, map_lng, endtime,id
      }

      this.$store.dispatch('updateTogether', payload)
    },
    onSubmit() {
      if (this.action === 'create') {
        this.createTogether()
      } else {
        this.updateTogether()
      }
    },
    mapPosi(posi) {
      this.map_lng = posi.posiX
      this.map_lat = posi.posiY
      console.log(posi.posiY,posi.posiX)
    },
    updateTime() {
      var now = new Date(this.Together.endtime);
      now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
      now.setMilliseconds(null)
      now.setSeconds(null)
      document.getElementById('endtime').value = now.toISOString().slice(0, -1);
    },
    createTime() {
      var now = new Date();
    now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
    now.setMilliseconds(null)
    now.setSeconds(null)
    document.getElementById('endtime').value = now.toISOString().slice(0, -1);
    }
  },
  mounted() {
    if (this.Together.endtime) {
      this.updateTime()
    } else {
      this.createTime()
    }
  },
}
</script>

<style>

</style>