<template>
    <div>
        <!-- <AppHeader /> -->
        <!-- <div v-if="userpostsCount === 0">
            <NoBlogs></NoBlogs>
        </div>
        <div v-else class="nesting-all-posts-container">
            <div class="all-posts-container">
                <BlogComponent v-for="post in feed" :key="post.post_id" :post="post" :user-id="post.user_id"/>
            </div>
        </div> -->
    </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'

export default {
    name: "HomeView",
    components: {
        AppHeader,
    },
    data() {
        return {
            show: false,
        }
    },
    computed: {
        userData() {
            return this.$store.state.userData;
        },
        feed() {
            return this.$store.state.userData.userposts;
        },
        userpostsCount() {
            return this.feed ? this.feed.length : 0;
        }
    },
    // async mounted(){
    //     await this.$store.dispatch('fetchData')
    // },
    methods: {

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
    width: 1100px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    flex-wrap: wrap;
}
</style>