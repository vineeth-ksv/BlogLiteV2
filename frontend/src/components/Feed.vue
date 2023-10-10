<template>
    <AppHeader>
        <div v-if="feedPostsCount === 0">
            <NoBlogs></NoBlogs>
        </div>
        <div v-else class="nesting-all-posts-container">
            <div class="all-posts-container">
                <BlogComponent v-for="post in feedData" :key="post.post_id" :post="post"/>
            </div>
        </div>
    </AppHeader>
</template>


<script>
import AppHeader from '@/components/AppHeader.vue'

export default {
    name: "HomeFeed",
    components: {
        AppHeader,
    },
    data() {
        return {
            show: false,
        }
    },

    computed: {
        userName() {
            return this.$store.getters.getLoggedInUsername
        },
        feedData() {
            return this.$store.getters.getFeedData;
        },
        feedPostsCount() {
            return this.feedData ? this.feedData.length : 0;
        }
    },

    mounted(){
        this.$store.dispatch("fetchFeedData", this.$store.getters.getLoggedInUsername);
    },
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