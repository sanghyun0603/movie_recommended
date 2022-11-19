<template>
  <div>
    <hr>
    <h2>지도맵보여주기</h2>
    <div id="map"></div>
  </div>
</template>

<script>
export default {
 name: 'KakaoMap',
 data() {
  return {
    map: [],
    coords : [],
  }
 },
 props: {
  mapLat : Number,
  mapLng : Number,
 },
 methods : {
  initMap() {
      const container = document.getElementById("map");
      const center = new kakao.maps.LatLng(this.mapLat , this.mapLng)
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
 },
 mounted() {
  console.log('mounterd')
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
}
</script>

<style>
#map {
  width: 100%;
  height: 300px;
}
</style>