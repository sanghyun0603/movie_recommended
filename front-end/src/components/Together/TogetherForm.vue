<template>
  <div class="togetherContainer">
    <!-- <h2>같이봐요</h2> -->
      <TogetherFormMap
      :map-lat="this.map_lat"
      :map-lng="this.map_lng"
      @to-form="mapPosi"
      />
      <form class="m-4" @submit.prevent="onSubmit">

        <div class="row g-3">
          <div class="form-floating col-sm-7 m-3">
            <input class="form-control" id="title" type="text" v-model="title">
            <label for="title">title</label>
          </div>

          <div class="form-floating m-3 col-sm m-3">
            <input id='endtime' type="datetime-local" @change="inputTime">
          </div>
        
        </div>

        <div class="form-floating m-3">
          <textarea class="form-control" id="content" type="text" v-model="content" style="height:300px"></textarea>
          <label for="content">Together</label>
        </div>


      <button class="createBtn">작성</button>
    </form>

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
    inputTime(event){
      this.endtime = event.target.value
    },
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
.togetherContainer{
  height: 500px;
  width: 1000px;
  margin-left: auto;
  margin-right: auto ;
  margin-top: 100px ;
}
</style>