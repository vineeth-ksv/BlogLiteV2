<template>
    <div>
        <AppHeader>
            <div class="d-flex justify-content-center" style="margin-top: 50px;">
                <h2>Archived Posts</h2>
            </div>
            <hr style="border: 1px solid gray; width: 1200px; margin-top: 30px; margin-bottom: 30px;" />
            <div v-if="archivedPostsCount === 0">
                <div class="no-posts d-flex flex-column justify-content-center align-items-center" style="margin-top: 150px;">
                        <b-img
                            src="https://icon-library.com/images/photo-icon-png/photo-icon-png-1.jpg"
                            width="70px"
                            height="70px">
                        </b-img>
                        <h5>There are no archived posts.</h5>
                </div>
            </div>
            <div v-else class="nesting-all-posts-container">
                <div class="all-posts-container">
                    <div class="posts-container" v-for="post in ArchivedPosts" :key="post.post_id">
                        <router-link :to="{ name: 'ViewPost', params: { postId: post.post_id }}">
                            <b-img
                                :src="getBase64Image(post.post_img)"
                                fluid
                                alt="Image"
                                class="mr-3"
                                style="height: 350px; width: 350px;"
                            ></b-img>
                        </router-link>
                    </div>  
                </div>
            </div>
        </AppHeader>
    </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'

export default {
    name: "ArchivedPosts",
    components: {
        AppHeader,
    },
    data() {
        return {
            show: false,
        }
    },
    computed: {
        // username() {
        //     return this.$route.params.userName
        // },
        username(){
            return this.$store.getters.getLoggedInUsername
        },
        loggedInUsername() {
            return this.$store.getters.getLoggedInUsername
        },
        ArchivedPosts() {
            return this.$store.getters.getArchivedPosts;
        },
        archivedPostsCount() {
            return this.ArchivedPosts ? this.ArchivedPosts.length : 0;
        },
    },
    mounted() {
        const username = this.$store.getters.getLoggedInUsername;
        this.$store.dispatch("archivedPosts", username);
    },
    methods: {
        getBase64Image(base64Image) {
            return "data:image/*;base64," + base64Image;
        },
    }
}
</script>

<style scoped>

* {
    font-family: poppins;
}

.nesting-all-posts-container {
    margin-top: 50px;
    display: flex;
    justify-content: center;
}

.all-posts-container {
    width: 1170px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    flex-wrap: wrap;
}

.posts-container {
    margin: 30px 20px;
    width: 350px;
}

</style>