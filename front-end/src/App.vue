<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link :to="{name :'ShowMoviesView'}">Movie</router-link> |
      <router-link :to="{name :'ForumView'}">Forum</router-link> |
      <router-link :to="{name :'ReviewView'}">Review</router-link> |
      <router-link :to="{name :'TogetherView'}">Together</router-link> |
      <router-link :to="{name :'SignupView'}">Signup</router-link> |
      <router-link :to="{name :'LoginView'}">Login</router-link> |
      <button @click="Logout">Logout</button>
    </nav>
    <router-view/>
  </div>
</template>
<script>
export default {
  methods : {
    Logout() { this.$store.dispatch('logout')}
  }

}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
