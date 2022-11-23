<template>
  <div id="whole">
    <div id="signUpContainer" class="">

      <h2 id="signUpTitle">회원가입 하쉴?</h2>
      <form @submit.prevent="signUp">
        <span>
          <input placeholder = '아이디를 입력하세요' type="text" id="username" v-model="username"><br>
        </span>

        <span>
          <input placeholder = '닉네임을 입력하세요' type="text" id="nickname" v-model="nickname"><br>
        </span>

        <span>
          <input placeholder = '비밀번호를 입력하세요' type="password" id="password1" v-model="password1"><br>
        </span>

        <span>
          <input placeholder = '비밀번호를 확인하세요' type="password" id="password2" v-model="password2">
        </span>

        <button type="submit" id="signUpButton">회원가입</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name : 'SignupView',
  data() {
    return {
      username : null,
      nickname : null,
      password1 : null,
      password2 : null,
    }
  },
  methods : {
    signUp() {
      const username = this.username
      const nickname = this.nickname
      const password1 = this.password1
      const password2 = this.password2
      const payload = {
        username,
        nickname,
        password1,
        password2,
      }
      this.$store.dispatch('signUp',payload)
    }
  }
}
</script>


<style scoped>
#whole{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
  background-image: url('@/assets/userpage (3).jpg');
  background-size: cover;
}
#signUpContainer{
  display: flex;
  flex-direction: column;
  text-align: center;
  position: relative;
  width: 440px;
  padding: 70px;
  background-color: #02111B;
  opacity: 0.9;
  border-radius: 30px;
}

#signUpButton{
  width: 300px;
  height: 50px;
  margin-top: 10px;
  border-radius: 10px;
  /* font-size: large; */
  background-color: #710627;
  font-size: large;
  font-weight: bold ;
}

#username,
#nickname,
#password1,
#password2{
  width: 300px;
  height: 50px;
  margin-top: 10px;
  border-radius: 10px;
  font-size: large;
  background-color: #A7A7A9;
  border: solid #02111B;
}
input::placeholder{
  font-style: italic;
  color: #60594D;
}
#signUpTitle{
  padding-bottom: 10px;
  font-size: xx-large;
  color: white;
}
</style>