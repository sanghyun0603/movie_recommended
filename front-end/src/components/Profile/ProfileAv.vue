<template>
  <img alt="Avatar" :src="avatar">
</template>

<script>
import { createAvatar } from '@dicebear/avatars';
import * as style from '@dicebear/avatars-identicon-sprites';
export default {
  name : 'ProfileAv',
  props : {
    username : String,
  },
  computed: {
    avatar(){
      return createAvatar(style, {
        dataUri: true,
        size: 128,
        seed: this.username,
     });
    },
  },
}
</script>

<style>

</style>