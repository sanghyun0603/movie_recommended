<template>
  <div>
    <!-- <h2>글쓰기</h2> -->
    <div class="container" role="main">
        <!-- <h2>board Form</h2> -->
          <form class="m-4" @submit.prevent="onSubmit">

            <div class="form-floating mb-3">
              <input class="form-control" placeholder="제목을 작성하세요" id="title" type="text" v-model="title">
              <label for="title">제목</label>
            </div>

            <div class="form-floating mb-3">
              <textarea style="height:300px" class="form-control" rows="5" name="content" id="content" placeholder="내용을 입력해 주세요" v-model="content"></textarea>
              <label for="content">내용</label>
            </div>

            <button class="createBtn">작성</button>
          </form>
    </div>
  </div>
</template>

<script>
export default {
  name : 'ForumForm',
  data(){
    return {
      title : this.forum.title,
      content : this.forum.content,
    }
  },
  props : {
    forum : Object,
    action : String,
  },
  methods : {
    createForum(){
      const title = this.title
      const content = this.content

      const payload = {
        title, content
      }
      this.$store.dispatch('createForum', payload)
    },
    updateForum(){
      const title = this.title
      const content = this.content
      const id = this.forum.id
      const payload = {
        title, content,id
      }
      this.$store.dispatch('updateForum', payload)
    },
    onSubmit() {
      if (this.action === 'create') {
        this.createForum()
      } else {
        this.updateForum()
      }
    }
  }
}
</script>

<style scoped>
.createBtn{
  background: rgba(102,152,203,1);
  background: -moz-linear-gradient(top, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(102,152,203,1)), color-stop(100%, rgba(92,138,184,1)));
  background: -webkit-linear-gradient(top, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  background: -o-linear-gradient(top, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  background: -ms-linear-gradient(top, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  background: linear-gradient(to bottom, rgba(102,152,203,1) 0%, rgba(92,138,184,1) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#6698cb', endColorstr='#5c8ab8', GradientType=0 );
  color: white;
  display: inline-block;
  position: relative;
  text-shadow: rgba(0, 0, 0, 0.15) 0px 1px 0px;
  text-decoration: none;
  padding: 10px 30px;
  border-width: 1px 1px 4px;
  border-style: solid;
  border-color: rgba(0, 0, 0, 0.21);
  border-image: initial;
  border-bottom: 4px solid rgba(0, 0, 0, 0.21);
  border-radius: 4px;
  font-size: 12px;
  padding: 4px 12px;
}
.createBtn:active {
  background: #608FBF;
}

/* .form-wrapper{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  font-size: 1.5rem;
  font-weight: bold;
}
#title {
  margin-top: 10px;
  width: 500px;
}
#content{
  margin-top: 10px
}
.formBtn{

} */
</style>