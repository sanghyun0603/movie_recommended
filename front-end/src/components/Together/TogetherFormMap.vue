<template>
  <div>
    <h4>어디서 만날까요?</h4>
    <div class="my-3 mx-auto w-25 form-floating">
      <input class="form-control" type="text" @keyup.enter="searchPlace" v-model.trim="keyword">
      <label for="moviename">주소를 입력하세요</label>
    </div>
    <div id="map"></div>
  </div>
</template>

<script>
export default {
  name : 'KakaoMap',
  data() {
    return {
      map: [],
      coords : [],
      lat : null,
      lng : null,
      keyword : '',
    };
  },
  props : {
    mapLng : Number,
    mapLat : Number,
  },
  methods: {
    initMap() {
      const container = document.getElementById("map");
      const center = new kakao.maps.LatLng(this.mapLat, this.mapLng)
      const options = {
        center: center,
        level: 3,
      };
      this.map = new kakao.maps.Map(container, options);
      const marker = new kakao.maps.Marker({
            map: this.map,
            position: center
        });
      var infowindow = new kakao.maps.InfoWindow({
            content: `<div style="width:150px;text-align:center;padding:6px 0;">기준장소</div>`
        });
        infowindow.open(this.map, marker);
    },
    searchPlace(){
      
      const keyword = this.keyword
      const geocoder = new kakao.maps.services.Geocoder()
      
      const container = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(this.mapLat, this.mapLng),
        level: 3,
      };
      const map = new kakao.maps.Map(container, options);

      const createOverlay = result => {
        const coords = new kakao.maps.LatLng(result[0].y, result[0].x)
        // 결과값으로 받은 위치를 마커로 표시합니다
        const marker = new kakao.maps.Marker({
            map: map,
            position: coords
        });
        // 인포윈도우로 장소에 대한 설명을 표시합니다
        const infowindow = new kakao.maps.InfoWindow({
            content: `<div style="width:150px;text-align:center;padding:6px 0;">${this.keyword}</div>`
        });
        infowindow.open(map, marker);
        // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
        map.setCenter(coords);
      }
      const addressSearch = address => {
        return new Promise((resolve, reject) => {
          geocoder.addressSearch(address, function(result, status) {
            if (status === kakao.maps.services.Status.OK) {
              resolve(result)
            } else {
              reject(status)
            }
          })
        })
      }
      (async () => {
        try {
          const result = await addressSearch(keyword)
          const posiX = result[0].x
          const posiY = result[0].y
          const posi = {
            posiX,posiY
          }
          this.$emit('to-form', posi)
          createOverlay(result)
        } catch (e) {
          console.log(e)
        }
      })()
    }
  },
  mounted() {
    if (!window.kakao || !window.kakao.maps) {
      const script = document.createElement("script");
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=3f64d33753d781a868a5c3d7ec488788&libraries=services`;
      /* global kakao */
      script.addEventListener("load", () => {
        kakao.maps.load(this.initMap);
      });
      document.head.appendChild(script);
    } else {
      //console.log("이미 로딩됨: ", window.kakao);
      this.initMap();
      // this.searchPlace(this.keyword)
    }
  },
};
</script>

<style scoped>
#map {
  width: 100%;
  height: 300px;
}
</style>