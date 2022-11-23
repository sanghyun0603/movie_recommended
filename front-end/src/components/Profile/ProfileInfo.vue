<template>
  <div>
    <h2>{{nickname}}의 프로필입니다.</h2>
    <ProfileAv
    :username="username"
    />
  </div>
</template>

<script>
import ProfileAv from '@/components/Profile/ProfileAv'
export default {
  name : 'ProfileInfo',
  components : {
    ProfileAv,
  },
  props : {
    nickname : String,
    username : String,
  }
}
</script>

<style>

</style>