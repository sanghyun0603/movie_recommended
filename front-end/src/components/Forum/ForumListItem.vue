<template>
  <ul id="ulTable">
  <ul>
    <li>
      {{forum.id}}
    </li>
    <li class="left">
      <label for="">제목</label>
      <router-link :to="{ name : 'ForumDetailView', params : { id : forum.id} }"><h3>{{forum.title}}</h3></router-link>
    </li>

    <li>
      <label for="">작성자</label>
      <router-link :to="{ name : 'ProfileView', params : { username : forum.username} }"><p>{{forum.nickname}}</p></router-link>
    </li>
  </ul>
</ul>

                     <!-- <li>1</li>
                    <li class="left">제목제목제목제목1</li>
                    <li>2014.07.09</li>
                    <li>자바킹</li>
                    <li>0</li> -->
</template>

<script>
export default {
  name : 'ForumListItem',
  props : {
    forum : Object,
  }
}
</script>
