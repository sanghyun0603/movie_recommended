<template>
  <div>
    <TogetherForm
    :Together="Together" action="create"
    />
  </div>
</template>

<script>
import TogetherForm from '@/components/Together/TogetherForm'

export default {
  name : 'TogetherCreateView',
  components : {
    TogetherForm,
  },
  data() {
    return {
      Together : {id:null, title:'', content:'',endtime:null,map_lat:36.3553193257957,map_lng:127.29820111515,}
    }
  }
}
</script>

<style>

</style>