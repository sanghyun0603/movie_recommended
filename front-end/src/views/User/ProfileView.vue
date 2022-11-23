<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-4">
          <ProfileInfo
          :nickname="userProfile?.nickname"
          :username="userProfile?.username"
          />
          <div class="container">
            <button @click="select('forum')" class="btn btn-primary col-5 m-2">좋아요한 포럼</button>
            <button @click="select('review')" class="btn btn-primary col-5 m-2">좋아요한 리뷰</button>
            <button @click="select('together')" class="btn btn-primary col-5 m-2">좋아요한 구해</button>
            <button @click="select('movie')" class="btn btn-primary col-5 m-2">좋아요한 영화</button>
          </div>
            
        </div>
        <div class="col-8">
          <span v-if="sel === 'forum'">
            <ProfileLikeForum
            :user-likes-forums="userLikesForums"
            />   
          </span>
          <span v-else-if=" sel === 'review'">
            <ProfileLikeReview
            :user-likes-reviews="userLikesReviews"
            />
          </span>
          <span v-else-if="sel === 'together'">
            <ProfileLikeTogether
            :user-likes-togethers="userLikesTogethers"
            />
          </span>
          <span v-else>
            <ProfileLikeMovie
            :user-likes-movies="userLikesMovies"
            />
          </span>
        </div>
      </div>
    </div>
    

  </div>
</template>

<script>
import ProfileInfo from '@/components/Profile/ProfileInfo'
import ProfileLikeMovie from '@/components/Profile/ProfileLikeMovie'
import ProfileLikeForum from '@/components/Profile/ProfileLikeForum'
import ProfileLikeReview from '@/components/Profile/ProfileLikeReview'
import ProfileLikeTogether from '@/components/Profile/ProfileLikeTogether'
export default {
  name : 'ProfileView',
  data() {
    return {
      sel : 'movie',
    }
  },
  components : {
    ProfileInfo,
    ProfileLikeTogether,
    ProfileLikeReview,
    ProfileLikeForum,
    ProfileLikeMovie,
  },
  created() {
    this.$store.dispatch('customGetUserInfo',this.$route.params.username)
    this.$store.dispatch('userLikesForums', this.$route.params.username)
    this.$store.dispatch('userLikesReviews', this.$route.params.username)
    this.$store.dispatch('userLikesTogethers', this.$route.params.username)
    this.$store.dispatch('userLikesMovies', this.$route.params.username)
  },
  computed : {
    userProfile() {
      return this.$store.getters.userProfile
    },
    userLikesForums() {
      return this.$store.getters.userLikesForums
    },
    userLikesReviews() {
      return this.$store.getters.userLikesReviews
    },
    userLikesTogethers() {
      return this.$store.getters.userLikesTogethers
    },
    userLikesMovies() {
      return this.$store.getters.userLikesMovies
    },
    user() {
      return this.$store.getters.user
    },
    
  },
  methods : {
    select(data) {
      console.log(data)
      this.sel = data
    }
  },
}
</script>

<style>

</style>