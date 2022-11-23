<template>
  <div>
    <!-- <h2>TogetherUpdateView</h2> -->
    <TogetherForm
    :Together="Together" action="update"
    />
  </div>
</template>

<script>
import TogetherForm from '@/components/Together/TogetherForm'

export default {
  name : 'TogetherUpdateView',
  components : {
    TogetherForm,
  },
  computed : {
    Together() {
      return this.$store.getters.together
    }
  }
}
</script>

<style>

</style>