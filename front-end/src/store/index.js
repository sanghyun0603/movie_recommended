import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token : null,
  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN : (state,token) => state.token = token,
  },
  actions: {
    signUp({commit},payload) {
      axios({
        method : 'post',
        url : `${API_URL}/accounts/signup/`,
        data: {...payload}
      })
      .then((res) => {
        commit('SAVE_TOKEN', res.data.key)
        router.push({ name : 'HomeView'})
      })
      .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
