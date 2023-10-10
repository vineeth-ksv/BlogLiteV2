<template>
    <div class="posts-container">
        <b-card
            header="header"
            header-tag="header"
            class="overflow-hidden"
            no-body
        >
        <template #header>
            <div class="d-flex align-items-center" style="margin: 0px;padding: 0px;">
                <router-link :to="{ name: 'UserProfile', params: { userName: post.username } }">
                    {{ post.username }}
                </router-link>
            </div>
        </template>
        <b-card-body>
          <div class="post-image-container">
            <b-img 
                :src="getBase64Image(post.post_img)"
                fluid 
                alt="Image" 
                class="post-image">
            </b-img>
          </div>
          <div class="d-flex flex-row justify-content-between">
            <h5 class="card-title">{{ post.post_name }}</h5>
            <span class="d-flex flex-row">
                <div>
                    {{ postComments.length }}
                    <b-icon icon="chat" aria-hidden="true" @click="toggleComments" style="cursor: pointer;"></b-icon>
                </div>
                &ensp;
                <div>
                    <div v-if="postLikes.includes(userData.id)">
                        {{postLikes.length}}
                        <b-icon icon="hand-thumbs-up-fill" aria-hidden="true" @click="toggleLike" style="cursor: pointer;"></b-icon>
                    </div>
                    <div v-else>
                        {{postLikes.length}}
                        <b-icon icon="hand-thumbs-up" aria-hidden="true" @click="toggleLike" style="cursor: pointer;"></b-icon>
                    </div>
                </div>
            </span>
          </div>
          <p class="card-text">{{ post.post_caption }}</p>
          
          <div class="comments-container" v-bind:class="{ 'show': showComments }">
            <div v-for="comment in postComments" :key="comment.id">
                <div class="d-flex align-items-center justify-content-between" style="margin: 0px;padding: 0px;">
                    <div>
                        <router-link :to="{ name: 'UserProfile', params: { userName: comment.username } }">
                            <small>{{ comment.username }}</small>
                        </router-link>
                        :&ensp; <small>{{ comment.text }}</small>
                    </div>
                    <div v-if="(userData.username===comment.username) || (userData.username===post.username)">
                        <b-icon icon="trash" aria-hidden="true" style="cursor: pointer;"  @click="deleteComment(comment.comment_id)"></b-icon>
                    </div>
                </div>
                <!-- <div><small>{{ comment.text }}</small></div> -->
            </div>
          </div>
          <div>
            <b-form @submit.prevent="addComment" class="input-group mb-3">
                    <b-form-input 
                        v-model="comment" 
                        type="text" 
                        placeholder="Comment something!" size="sm" 
                    ></b-form-input>
                <b-button type="submit" variant="outline-secondary" size="sm">Comment</b-button>
            </b-form>
          </div>
        </b-card-body>
        <b-card-footer>
          <small class="text-muted">{{ post.updated_date }}</small>
        </b-card-footer>
      </b-card>
    </div>
  </template>
  
  <script>
  export default {
    name: "BlogComponent",
    props: {
        post: Object
    },
    data() {
      return {
        comment: '',
        showComments: false,
      };
    },

    computed: {
        userData() {
            return this.$store.getters.getUserData;
        },
        postLikes() {
            return this.post.likes.map((like) => like.user_id);
        },
        postComments(){
            return this.post.comments
        }
    },

    methods: {
        getBase64Image(base64Image) {
            return "data:image/*;base64," + base64Image;
        },
        toggleComments() {
            this.showComments = !this.showComments;
        },
        async addComment(){
            if (this.comment==''){
                alert("Comment cannot be empty..")
            }
            else{
                const payload = {
                    comment: this.comment,
                    user_id: this.$store.getters.getUserData.id,
                    post_id: this.post.post_id,
                }
                this.comment = ''
                
                await this.$store.dispatch("addComment", payload)
                .catch((error) => {
                    console.error(error)
                })
                
                await this.$store.dispatch("fetchFeedData", this.userData.username)
                .catch((error) => {
                    console.error(error)
                })
            }
        },
        async deleteComment(comment_id){
            this.$bvModal.msgBoxConfirm('Are you sure you want to delete this comment?', {
                title: 'Delete Comment',
                size: 'sm',
                buttonSize: 'sm',
                okVariant: 'danger',
                okTitle: 'Delete',
                cancelTitle: 'Cancel',
                footerClass: 'p-2',
                hideHeaderClose: false,
                centered: true
            })
            .then(async(value) => {
                if(value) {
                    const payload = {
                        comment_id: comment_id
                    }
                    await this.$store.dispatch('deleteComment', payload)
                    .catch((error) => {
                        console.error(error);
                    })

                    await this.$store.dispatch("fetchFeedData", this.userData.username)
                    .catch((error) => {
                        console.error(error)
                    })
                }
                else{
                    // do nothing
                }
            })
        },
        async toggleLike(){
            const payload = {
                user_id: this.userData.id,
                post_id: this.post.post_id
            }
            await this.$store.dispatch('togglePostLike', payload)
            .catch((error) => {
                console.error(error)
            })

            await this.$store.dispatch("fetchFeedData", this.userData.username)
            .catch((error) => {
                console.error(error)
            })
        },
    },
}
</script>

<style scoped>
a{
    color: black;
    text-decoration: none;
}

.comments-container {
    width: 95%;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-out;
    margin: auto;
}

.comments-container.show {
    max-height: 75px; 
    overflow-y: scroll;
    margin-bottom: 10px;
    /* border: 1px solid rgb(125, 179, 232);
    border-radius: 5px; */
}

.comments-container a:hover{
    color: blue;
}
.comments-container::-webkit-scrollbar {
    width: 2px;
}

.comments-container::-webkit-scrollbar-track {
    background-color: #f5f5f5;
}

.comments-container::-webkit-scrollbar-thumb {
    background-color: #888;
}

.comments-container::-webkit-scrollbar-thumb:hover {
    background-color: #555;
}

.posts-container {
    margin: 30px 20px;
    width: 500px;
}
.post-image-container{
    width: 500px;
    margin-bottom: 10px;
    padding: 0px;
}

.post-image {
    height: 350px;
    min-width: 450px;
    max-width: 450px;
}
.card-caption-scroll {
    overflow-y: scroll;
    max-height: 100px;
}
</style>
     
  