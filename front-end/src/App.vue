<template>
  <div id="app">
    <nav id="navBar" class="navbar navbar-expand-md justify-content-end">
      <div class="container-fluid">
        <span id="navspan" class="navbar-brand"><img id="navImg" src="@/assets/nav.png" alt="logo"></span>

        <div>
      <router-link to="/">Home</router-link> |
      <router-link :to="{name :'ShowMoviesView'}">Movie</router-link> |
      <router-link :to="{name :'SelectGenreView'}">Genre</router-link> |
      <router-link :to="{name :'ForumView'}">Forum</router-link> |
      <router-link :to="{name :'ReviewView'}">Review</router-link> |
      <router-link :to="{name :'TogetherView'}">Together</router-link> |
      <span v-if="this.isLogin">
        <!-- <router-link :to="{name : 'ProfileView',params : { username : userNow.username} }">Profile</router-link> | -->
        <a :href="`http://localhost:8080/profile/${userNow?.username}/`">Profile</a> |
        
      </span>
      <router-link :to="{name :'SignupView'}">Signup</router-link> |
      <router-link :to="{name :'LoginView'}">Login</router-link> | 
      <router-link :to="{name :'PasswordChangeView'}">Passwordchange</router-link> |
      <button @click="Withdrawal">회원탈퇴</button>
      <button @click="Logout">Logout</button>
        </div>
      
      </div>

    </nav>
    <router-view/>
    <portal-target name="modal" />
  </div>
</template>
<script>


export default {
  methods : {
    Logout() { this.$store.dispatch('logout')},
    Withdrawal() {
      this.$store.dispatch('withDrawal')
    },
  },
  components : {
    
  },
  computed : {
      isLogin() {
        return this.$store.getters.isLogin
      },
      userNow() {
        return this.$store.getters.userNow
      },
    },
}
</script>
<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
  /* background: linear-gradient(#292929 , #141414); */
}

nav {
  padding: 30px;
  background-color: #292929;
  /* background: linear-gradient(45deg, #141414, #292929); */
  /* margin-bottom: 20px;/ */
}

/* .home {
  background: linear-gradient(#292929 , #141414);
} */
nav a {
  font-weight: bold;
  color:rgba(166, 38, 57, 0.5);
}

nav a.router-link-exact-active {
  color: #A62639;
}

#navspan {
  width: 50px;
  height: 50px;
}

#navspan > img {
  width: 50;
  height: 50px;
}

/* #navBar {
  background:rgba(20, 20, 20);
  margin-bottom: 20px;
} */
</style>
