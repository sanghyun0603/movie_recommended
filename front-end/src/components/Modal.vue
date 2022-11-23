<template>
  <portal to="modal">
    <div class="modal-wrapper1">
      <div class="overlay1" @click="$router.back()"></div>
      <div class="modal1">
        <component :is="component" v-bind="$attrs" />
      </div>
    </div>
  </portal>
</template>

<script>
export default {
  
  name: "Modal",
  props: ["component"],
  // watch: {
  //   '$route' (to,from) {
  //     to
  //     from
  //     window.scrollTo(0,0)
  //   }
  // },
  mounted() {
    window.scrollTo(0,0)
  }
};
</script>

<style scoped>
.modal-wrapper1 {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
}
.modal1 {
  position: absolute;
  z-index: 1;
  margin: auto;
  max-height: calc(80vh);
  overflow-y : auto;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 1em;
  box-shadow: 0 0 1em #00000033;
}

.overlay1 {
  z-index: 1;
  position: absolute;
  width: 100vw;
  height: 100vh;
  background-color: #00000055;
}
</style>