<template>
  <div>
    <div id="mainWrapper">

<ul>
    <!-- 게시판 제목 -->

    <!-- 게시판 목록  -->
    <li>
        <ul id ="ulTable">
            <li>
                <ul>
                    <li>No</li>
                    <li>제목</li>
                    <li>종료시간</li>
                    <li>작성자</li>
                    <li>작성시간</li>
                </ul>
            </li>
            <!-- 게시물이 출력될 영역 -->
            <li>
                <ul v-for ="together in Togethers" :key="together.id">
                  <li>
                    {{together.id}}
                  </li>
                  <li class="left" id="over">
                    <router-link :to="{ name : 'TogetherDetailView', params : { id : together.id} }">{{together.title}} </router-link>
                  </li>
                  <li>
                    {{createTime(together.endtime)}}까지
                  </li>
                  <li>
                    <router-link :to="{ name : 'ProfileView', params : { username : together.username} }">{{together.nickname}}</router-link>
                  </li>
                  <li>
                    {{createTime(together.created_at)}}
                  </li>
                </ul>
            </li>                                     
        </ul>
    </li>
    <!-- 게시판 페이징 영역 -->
    <li>
        <div id="divPaging">
            <div>◀</div>
               <div><b>1</b></div>
            <div>2</div>
            <div>3</div>
            <div>4</div>
            <div>5</div>
            <div>▶</div>
        </div>
    </li>
</ul>
</div>
  </div>
</template>

<script>

export default {
  name : 'TogetherList',
  computed : {
    Togethers() {
      return this.$store.getters.togethers
    }
  },
  methods : {
    createTime(data) {
      var now = new Date(data);
    now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
    now.setMilliseconds(null)
    now.setSeconds(null)
    const nows = now.toISOString().slice(0, 10)+' '+now.toISOString().slice(11, 16)
    return nows
    }
  }
}
</script>

<style scoped type="text/css">
#over {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: break-word;
  
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
    body{
        line-height:2em;        
        font-family:"맑은 고딕";
}
    ul, li{ 
        list-style:none;
        text-align:center;
        padding:0;
        margin:0;
}

    #mainWrapper{
        width: 800px;
        margin-left :auto;
      margin-right : auto;
    }

    #mainWrapper > ul > li:first-child {
        text-align: center;
        font-size:14pt;
        height:40px;
        vertical-align:middle;
        line-height:30px;
}

    #ulTable {margin-top:10px;
      
    }
    

    #ulTable > li:first-child > ul > li {
        background-color:#72dad1;
        font-weight:bold;
        text-align:center;
}

    #ulTable > li > ul {
        clear:both;
        padding:0px auto;
        
        position:relative;
        min-width:40px;
}
    #ulTable > li > ul > li { 
        float:left;
        font-size:10pt;
        border-bottom:1px solid silver;
        vertical-align:baseline;
}    

    #ulTable > li > ul > li:first-child               {width:10%;} /*No 열 크기*/
    #ulTable > li > ul > li:first-child +li           {width:25%;} /*제목 열 크기*/
    #ulTable > li > ul > li:first-child +li+li        {width:20%;} /*종료시간 열 크기*/
    #ulTable > li > ul > li:first-child +li+li+li    {width:25%;} /*작성자 열 크기*/
    #ulTable > li > ul > li:first-child +li+li+li+li  {width:20%;} /*작성일 열 크기*/


    #divPaging {
          clear:both; 
        margin:0 auto; 
        width:220px; 
        height:50px;
}

    #divPaging > div {
        float:left;
        width: 30px;
        margin:0 auto;
        text-align:center;
}


    .left {
        text-align : left;
}


</style>