<template>
  <div id="whole">
    <div id="changeContainer" class="">
      <h2 id="changeTitle">비밀번호좀 기억해라</h2>
      <form @submit.prevent="login">
          <span>
            <input placeholder='변경할 비밀번호' type="password" id="password1" v-model="password1"><br>
          </span>

          <span>
            <input placeholder='비밀번호 확인' type="password" id="password2" v-model="password2"><br>
          </span>

          <button type="submit" id="changeBtn">비밀번호 바꾸기</button>
      </form>
    </div>
  </div>  
  
</template>

<script>
export default {
  name : 'PasswordChangeView',
  data() {
    return {
      password1 : null,
      password2 : null,
    }
  },
  methods : {
    passwordChange() {
      const new_password1 = this.password1
      const new_password2 = this.password2
      const payload = {
        new_password1,new_password2
      }
      this.$store.dispatch('passwordChange', payload)
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
  background-image: url('@/assets/passwordChange.jpg');
  background-size: cover;
}
#changeContainer{
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

#changeBtn{
  width: 300px;
  height: 50px;
  margin-top: 10px;
  border-radius: 10px;
  background-color: #710627;
  font-size: large;
  font-weight: bold ;
}

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

#changeTitle{
  padding-bottom: 10px;
  color: white;
  font-size: xx-large;
}
</style>