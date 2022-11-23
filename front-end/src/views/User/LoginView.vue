<template>
  <div id="whole">
    <div id="loginContainer" class="">
      <h1 id="loginTitle">로그인 하셈</h1>
      <form @submit.prevent="login">
          <span>
            <input placeholder='아이디를 입력하도록' type="text" id="username" v-model="username"><br>
          </span>

          <span>
            <input placeholder='비밀번호를 입력하도록' type="password" id="password" v-model="password"><br>
          </span>


          <button type="submit" id="logInButton">로그인</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('login', payload)
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
  background-image: url('@/assets/userpage (4).jpg');
  background-size: cover;
}
#loginContainer{
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
#logInButton{
  width: 300px;
  height: 50px;
  margin-top: 10px;
  border-radius: 10px;
  font-size: large;
  font-weight: bold ;
  background-color: #710627;
}
#password,
#username{
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
#loginTitle{
  padding-bottom: 10px;
  font-size: xx-large;
  color: white;
}
</style>