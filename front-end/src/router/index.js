import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
//Forum
import ForumView from '@/views/Community/Forum/ForumView'
import ForumCreateView from '@/views/Community/Forum/ForumCreateView'
import ForumUpdateView from '@/views/Community/Forum/ForumUpdateView'
import ForumDetailView from '@/views/Community/Forum/ForumDetailView'
//Review
import ReviewView from '@/views/Community/Review/ReviewView'
import ReviewCreateView from '@/views/Community/Review/ReviewCreateView'
import ReviewUpdateView from '@/views/Community/Review/ReviewUpdateView'
import ReviewDetailView from '@/views/Community/Review/ReviewDetailView'
//Together
import TogetherView from '@/views/Community/Together/TogetherView'
import TogetherCreateView from '@/views/Community/Together/TogetherCreateView'
import TogetherUpdateView from '@/views/Community/Together/TogetherUpdateView'
import TogetherDetailView from '@/views/Community/Together/TogetherDetailView'
//User
import SignupView from '@/views/User/SignupView'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  //Forum router
  {
    path: '/forum',
    name: 'ForumView',
    component: ForumView,
  },
  {
    path: '/forum/create',
    name: 'ForumCreateView',
    component: ForumCreateView,
  },
  {
    path: '/forum/update',
    name: 'ForumUpdateView',
    component : ForumUpdateView,
  },
  {
    //추후 path :id로 수정필요
    path: '/forum/detail',
    name: 'ForumDetailView',
    component : ForumDetailView
  },
  //Review
  {
    path: '/review',
    name: 'ReviewView',
    component : ReviewView,
  },
  {
    path: '/review/create',
    name: 'ReviewCreateView',
    component : ReviewCreateView,
  },
  {
    path: '/review/update',
    name: 'ReviewUpdateView',
    component : ReviewUpdateView,
  },
  {
    //추후 path 수정
    path: '/review/detail',
    name: 'ReviewDetailView',
    component : ReviewDetailView,
  },
  //Together
  {
    path: '/together',
    name: 'TogetherView',
    component : TogetherView,
  },
  {
    path: '/together/create',
    name: 'TogetherCreateView',
    component : TogetherCreateView,
  },
  {
    path: '/together/update',
    name: 'TogetherUpdateView',
    component : TogetherUpdateView,
  },
  {//수정
    path: '/together/detail',
    name: 'TogetherDetailView',
    component : TogetherDetailView,
  },
  //user
  {
    path: '/signup',
    name: 'SignupView',
    component : SignupView,
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
