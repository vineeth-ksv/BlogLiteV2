<template>
    <div>
        <AppHeader>
            <div v-if="currentPost.username===userData.username">
                <div class="button-container" v-if="currentPost.isArchive === false">
                    <div class="left-btns">
                        <router-link :to="{ name: 'UserProfile', params: { userName: currentPost.username }}">
                            <b-button variant="outline-secondary" size="sm">Back</b-button>
                        </router-link>
                    </div>
                    <div class="right-btns">
                        <b-button variant="outline-primary" size="sm" @click="editPost">Edit Post</b-button>
                        <b-button variant="outline-secondary" size="sm" @click="archivePost">Archive Post</b-button>
                        <b-button variant="outline-danger" size="sm" @click="deletePost">Delete Post</b-button>
                    </div>
                </div>
                <div class="button-container" v-else>
                    <div class="left-btns">
                        <router-link :to="{ name: 'ArchivedPosts' }">
                            <b-button variant="outline-secondary" size="sm">Back</b-button>
                        </router-link>
                    </div>
                    <div class="right-btns">
                        <b-button variant="secondary" size="sm" @click="archivePost">Unarchive Post</b-button>
                    </div>
                </div>
            </div>
            <div v-else>
                <div class="button-container" v-if="currentPost.isArchive === false">
                    <div class="left-btns">
                        <router-link :to="{ name: 'UserProfile', params: { userName: currentPost.username }}">
                            <b-button variant="outline-secondary" size="sm">Back</b-button>
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="current-post">
                <div>
                    <b-card
                        :header="currentPost.username"
                        header-tag="header"
                        class="overflow-hidden"
                        no-body
                    >
                    <b-card-body>
                        <div class="post-image-container">
                            <b-img 
                                :src="getBase64Image(currentPost.post_img)"
                                fluid 
                                alt="Image" 
                                class="post-image">
                            </b-img>
                        </div>
                        <div class="d-flex flex-row justify-content-between">
                            <h5 class="card-title">{{ currentPost.post_name }}</h5>
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
                        <p class="card-text">{{ currentPost.post_caption }}</p>

                        <div class="comments-container" v-bind:class="{ 'show': showComments }">
                            <div v-for="comment in postComments" :key="comment.id">
                                <div class="d-flex align-items-center justify-content-between" style="margin: 0px;padding: 0px;">
                                    <div>
                                        <router-link :to="{ name: 'UserProfile', params: { userName: comment.username } }">
                                            <small>{{ comment.username }}</small>
                                        </router-link>
                                        :&ensp; <small>{{ comment.text }}</small>
                                    </div>
                                    <div v-if="(userData.username===comment.username) || (userData.username===currentPost.username)">
                                        <b-icon icon="trash" aria-hidden="true" style="cursor: pointer;"  @click="deleteComment(comment.comment_id)"></b-icon>
                                    </div>
                                </div>
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
                        <small class="text-muted">{{ currentPost.updated_date }}</small>
                    </b-card-footer>
                    </b-card>
                </div>
            </div>

            <div class="chart-container" v-if="currentPost.username===userData.username">
                <h5>Post Engagements: </h5>
                <div style="width:400px;">
                    <canvas id="engagementChart"></canvas>
                </div>
            </div>
        </AppHeader>
    </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'
import Chart from 'chart.js/auto';

export default {
    name: "ViewPost",
    components: {
        AppHeader,
    },
    data () {
        return { 
            comment: '',
            showComments: false,
        }
    },
    methods: {
        getBase64Image(base64Image) {
            return "data:image/*;base64," + base64Image;
        },
        showGraph(){
            let chartData = {
                labels: ['Engagements'],
                datasets: [{
                    label: 'Comments',
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgb(54, 162, 235, 1)',
                    borderWidth: 2,
                    data: [this.postComments.length],
                },{
                    label: 'Likes',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgb(255, 99, 132, 1)',
                    borderWidth: 2,
                    data: [this.postLikes.length],
                }]
            };

            let config = {
                type: 'bar',
                data: chartData,
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                stepSize: 1
                            }
                        }
                    }
                }
            };

            let engagementChart = new Chart(document.getElementById("engagementChart"), config);
            engagementChart;
        },
        toggleComments() {
            this.showComments = !this.showComments;
        },
        async toggleLike(){
            const payload = {
                user_id: this.userData.id,
                post_id: this.currentPost.post_id
            }
            await this.$store.dispatch('togglePostLike', payload)
            .catch((error) => {
                console.error(error)
            })

            await this.$store.dispatch("fetchProfileData", this.currentPost.username)
            .catch((error) => {
                console.error(error);
            })
            this.showGraph();
        },
        async addComment(){
            if (this.comment==''){
                alert("Comment cannot be empty..")
            }
            else{
                const payload = {
                    comment: this.comment,
                    user_id: this.$store.getters.getUserData.id,
                    post_id: this.currentPost.post_id,
                }
                this.comment = ''
                
                await this.$store.dispatch("addComment", payload)
                .catch((error) => {
                    console.error(error)
                })

                await this.$store.dispatch("fetchProfileData", this.currentPost.username)
                .catch((error) => {
                    console.error(error);
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

                    await this.$store.dispatch("fetchProfileData", this.currentPost.username)
                    .catch((error) => {
                        console.error(error);
                    })
                } 
                else{
                    // do nothing
                }
            })

        },
        async editPost() {
            // navigate to the EditPost component with current post id
            this.$router.push({ 
                name: "EditPost", 
                params: { postId: this.currentPost.post_id }
            });
        },
        async archivePost() {
            // archive the current post
            const username = this.$store.getters.getLoggedInUsername;
            const postId = this.post_id
            const payload = {
                username: username, 
                postId: postId
            }
            await this.$store.dispatch("archivePost", payload)
        },
        async deletePost() {
            // show confirmation dialog
            this.$bvModal.msgBoxConfirm('Are you sure you want to delete this post?', {
                title: 'Delete Post',
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
                if (value){
                    // delete the current post
                    const username = this.$store.getters.getLoggedInUsername;
                    const postId = this.post_id
                    const payload = {
                        username: username, 
                        postId: postId
                    }
                    await this.$store.dispatch("deletePost", payload)
                } else {
                    // do nothing
                }
            })
            .catch((error)=>{
                console.error(error);
            });
        },
    },
    computed: {
        post_id() {
            return this.$route.params.postId
        },
        currentPost(){
            const postId = this.$route.params.postId;
            const profileData = this.$store.getters.getProfileData;

            let userPost = profileData.userposts.find(post => post.post_id === postId);

            if (userPost) {
                return userPost;
            } else {
                // handle error
                const archivedPosts = this.$store.getters.getArchivedPosts
                userPost = archivedPosts.find(post => post.post_id === postId);
                return userPost;
            } 
        },
        userData(){
            return this.$store.getters.getUserData
        },
        postComments(){
            return this.currentPost.comments ? this.currentPost.comments : []
        },
        postLikes() {
            return this.currentPost.likes ? this.currentPost.likes.map((like) => like.user_id) : []
        },
    },

    mounted() {
        this.showGraph()
    }
}
</script>

<style scoped>
a{
    color: black;
    text-decoration: none;
}
.current-post{  
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: 10px 0px;
}
.post-image{
    width: 600px;
    height: 500px
}
.post-image-container{
    margin-bottom: 20px;
}
.button-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 50px auto 20px;
  width: 650px;
}

.button-container button{
    margin: 0px 5px;
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

.chart-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 50px 0px;
}
</style>