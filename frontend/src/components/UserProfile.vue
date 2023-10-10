<template>
    <div>
        <AppHeader>
            <div v-if="username===loggedInUsername">
                <div class="profile-container d-flex align-items-center justify-content-between mx-auto">
                    <b-img 
                        :src="require('@/assets/images/blank-profile-picture.png')" 
                        class="profileImage" 
                        id="profileImage" 
                        style="width: 200px; height: 200px;"
                        rounded="circle"
                        fluid>
                    </b-img>
                    <div>
                        <div class="inner-container d-flex justify-content-between flex-row ">
                            <h3 class="ms-5 h3-username">{{ profileData.username }}</h3>
                            <div>
                                <b-button variant="secondary" class="edit-profile-btn" :to="{ name: 'EditProfile'}">Edit Profile</b-button>
                                <b-dropdown text-class="dropbtn">
                                    <b-dropdown-item :to="{ name: 'ArchivedPosts' }">Archived</b-dropdown-item>
                                    <b-dropdown-item @click="deleteProfile">Delete profile</b-dropdown-item>
                                    <b-dropdown-item @click="exportBlogs">Export Blogs</b-dropdown-item>
                                </b-dropdown>
                            </div>
                        </div>
                        <div class="profile-insights d-flex justify-content-between mt-4">
                            <h6 class="ms-5"><b>{{ userpostsCount }}</b> Posts</h6>
                            <b-link @click="showFollowersModal = true"><h6 class="ms-5"><b>{{ followersCount }}</b> Followers</h6></b-link>
                            <b-link @click="showFollowingModal = true"><h6 class="ms-5"><b>{{ followingCount }}</b> Following</h6></b-link>
                        </div>

                        <b-modal v-model="showFollowersModal" title="Followers" hide-footer>
                            <div class="connections-list">
                                <div v-if="followersCount > 0">
                                        <div v-for="follower in followersList" :key="follower.follower_id" class="d-flex flex-row justify-content-between my-2">
                                            <div>
                                                <b-link @click="fetchUserProfile(follower.follower_name)">{{ follower.follower_name }}</b-link>
                                            </div>
                                            <div>
                                                <b-button variant="danger" size="sm" @click="removeFollower(follower.follower_name, follower.follower_id)">Remove</b-button>
                                            </div>
                                        </div>
                                </div>
                                <div v-else>
                                    <center><b>No Followers</b></center>
                                </div>
                            </div>
                        </b-modal>

                        <b-modal v-model="showFollowingModal" title="Following" hide-footer>
                            <div class="connections-list">
                                <div v-if="followingCount > 0">
                                        <div v-for="following in followingList" :key="following.following_id" class="d-flex flex-row justify-content-between my-2">
                                            <div>
                                                <b-link @click="fetchUserProfile(following.following_name)">{{ following.following_name }}</b-link>
                                            </div>
                                            <div>
                                                <b-button variant="secondary" size="sm" @click="unfollowUser(following.following_name, following.following_id)">Unfollow</b-button>
                                            </div>
                                        </div>
                                </div>
                                <div v-else>
                                    <center><b>No Followers</b></center>
                                </div>
                            </div> 
                        </b-modal>
                    </div>
                </div>
                <hr style="border: 1px solid gray; width: 1200px; margin-top: 30px; margin-bottom: 30px;" />
                <div v-if="userpostsCount === 0">
                    <div class="no-posts">
                        <center>
                            <b-img
                                src="https://icon-library.com/images/photo-icon-png/photo-icon-png-1.jpg"
                                width="70px"
                                height="70px">
                            </b-img>
                            <h5>When you share photos & videos, they'll appear on your profile.</h5>
                            <h5>Share your first photo or video.</h5>
                        </center>
                    </div>
                </div>
                <div v-else class="nesting-all-posts-container">
                    <div class="all-posts-container">
                        <div class="posts-container" v-for="post in profileData.userposts" :key="post.post_id" >
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
            </div>
            <div v-else>
                <div class="profile-container d-flex align-items-center justify-content-between mx-auto">
                    <b-img 
                        :src="require('@/assets/images/blank-profile-picture.png')" 
                        class="profileImage" 
                        id="profileImage" 
                        style="width: 180px; height: 180px;"
                        rounded="circle"
                        fluid>
                    </b-img>
                    <div>
                        <div class="inner-container d-flex justify-content-between flex-row ">
                            <h3 class="ms-5 h3-username">{{ profileData.username }}</h3>
                        </div>
                        <div class="profile-insights d-flex justify-content-between mt-4">
                            <h6 class="ms-5"><b>{{ userpostsCount }}</b> Posts</h6>
                            <b-link @click="showFollowersModal = true"><h6 class="ms-5"><b>{{ followersCount }}</b> Followers</h6></b-link>
                            <b-link @click="showFollowingModal = true"><h6 class="ms-5"><b>{{ followingCount }}</b> Following</h6></b-link>
                        </div>

                        <b-modal v-model="showFollowersModal" title="Followers" hide-footer>
                            <div v-if="followersCount > 0">
                                    <div v-for="follower in followersList" :key="follower.follower_id">
                                        <div>
                                            {{ follower.follower_name }}
                                        </div>
                                    </div>
                            </div>
                            <div v-else>
                                <center><b>No Followers</b></center>
                            </div>
                        </b-modal>

                        <b-modal v-model="showFollowingModal" title="Following" hide-footer>
                            <div v-if="followingCount > 0">
                                    <div v-for="following in followingList" :key="following.following_id">
                                        <div>
                                            {{ following.following_name }}
                                        </div>
                                    </div>
                            </div>
                            <div v-else>
                                <center><b>No Followers</b></center>
                            </div>
                        </b-modal>

                        <div class="follow-btn" v-if="followerFlag">
                            <b-button variant="primary" size="sm" @click="unfollowUser(profileData.username, profileData.id)">Following</b-button>
                        </div>
                        <div class="follow-btn" v-else>
                            <b-button variant="primary" size="sm" @click="followUser(profileData.username, profileData.id)">Follow</b-button>
                        </div>
                    </div>
                </div>
                <hr style="border: 1px solid gray; width: 1100px; margin-top: 30px; margin-bottom: 30px;" />
                <div v-if="followerFlag">
                    <div v-if="userpostsCount === 0">
                        <div class="no-posts">
                            <center>
                                <b-img
                                    src="https://icon-library.com/images/photo-icon-png/photo-icon-png-1.jpg"
                                    width="70px"
                                    height="70px">
                                </b-img>
                                <h5>No Posts Yet.</h5>
                            </center>
                        </div>
                    </div>
                    <div v-else class="nesting-all-posts-container">
                        <div class="all-posts-container">
                                <!-- <BlogComponent v-for="post in profileData.userposts" :key="post.post_id" :post="post"/> -->
                            <div class="posts-container" v-for="post in profileData.userposts" :key="post.post_id" >
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
                </div>
                <div v-else>
                    <div class="no-posts">
                        <center>
                            <b-img
                                src="https://www.talk-english.co.uk/wp-content/uploads/2018/05/Padlock-symbol.png"
                                width="70px"
                                height="70px">
                            </b-img>
                            <h5>This account is private.</h5>
                            <p>Follow this account to see their posts.</p>
                        </center>
                    </div>
                </div>
            </div>
        </AppHeader>
    </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'

export default {
    name: "UserProfile",
    components: {
        AppHeader,
    },
    data() {
        return {
            show: false,
            showFollowersModal: false,
            showFollowingModal: false,
        }
    },
    computed: {
        username() {
            return this.profileData.username
        },
        loggedInUsername() {
            return this.$store.getters.getLoggedInUsername
        },
        userData() {
            return this.$store.getters.getUserData;
        },
        profileData() {
            return this.$store.getters.getProfileData;
        },
        userpostsCount() {
            return this.profileData.userposts ? this.profileData.userposts.length : 0;
        },
        followersCount() {
            return this.profileData.followers_list ? this.profileData.followers_list.length : 0
        },
        followingCount(){
            return this.profileData.following_list ? this.profileData.following_list.length : 0
        },
        followersList(){
            return this.$store.getters.getFollowersList
        },
        followingList() {
            return this.$store.getters.getFollowingList
        },
        followerFlag() {
            const loggedInId = this.userData.id;
            if((this.profileData.followers_list) && (this.profileData.followers_list.length > 0)){
                return this.profileData.followers_list.some(follower => follower.follower_id === loggedInId);
            }
            else{
                return false;
            }
        }

    },

    created() {
        // Fetch the initial user profile data
        // this.fetchUserProfile(this.$route.params.userName)
        this.$store.dispatch("fetchProfileData", this.$route.params.userName)
    },

    watch: {
        // Watch for changes to the route parameter and update the profile accordingly
        '$route.params.userName'(newUsername) {
            this.$store.dispatch("fetchProfileData", newUsername)
            // this.fetchUserProfile(newUsername)
        }
    },

    methods: {
        getBase64Image(base64Image) {
            return "data:image/*;base64," + base64Image;
        },
        async deleteProfile() {
            this.$bvModal.msgBoxConfirm('Are you sure you want to delete this profile?', {
                title: 'Delete Profile',
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
                    // delete the profile
                    const username = this.$store.getters.getLoggedInUsername;
                    const payload = {
                        username: username, 
                    }
                    await this.$store.dispatch("deleteProfile", payload)
                } else {
                    // do nothing
                }
            })
            .catch((error)=>{
                console.error(error);
            });

        },

        async unfollowUser(unfollow_username, unfollow_id){
            this.$bvModal.msgBoxConfirm('Are you sure you want to unfollow this user?', {
                title: 'Unfollow User',
                size: 'sm',
                buttonSize: 'sm',
                okVariant: 'danger',
                okTitle: 'Unfollow',
                cancelTitle: 'Cancel',
                footerClass: 'p-2',
                hideHeaderClose: false,
                centered: true
            })
            .then(async(value) => {
                if (value){
                    // unfollow the current user
                    const userData = this.$store.state.userData
                    const payload = {
                        unfollow_username: unfollow_username,
                        user_id: userData.id, 
                        unfollow_id: unfollow_id
                    }
                    
                    await this.$store.dispatch("unfollowUser", payload)

                    const username = this.$route.params.userName
                    // const username = this.$store.getters.getLoggedInUsername;
                    this.$store.dispatch("fetchProfileData", username);
                } else {
                    // do nothing
                }
            })
            .catch((error)=>{
                console.error(error);
            });
        },

        async followUser(follow_username, follow_id){
            const userData = this.$store.state.userData
            const payload = {
                follow_username: follow_username,
                user_id: userData.id, 
                follow_id: follow_id
            }  
            console.log(payload)
            await this.$store.dispatch("followUser", payload);
            
            const username = this.$route.params.userName
            // const username = this.$store.getters.getLoggedInUsername;
            this.$store.dispatch("fetchProfileData", username);
        },

        async removeFollower(follower_name, follower_id){
            const userData = this.$store.state.userData
            const payload = {
                follower_username: follower_name,
                user_id: userData.id,
                follower_id: follower_id
            }
            console.log(payload);
            await this.$store.dispatch("removeFollower", payload);

            const username = this.$route.params.userName
            this.$store.dispatch("fetchProfileData", username);
        },   

        fetchUserProfile(temp_username) {
            this.showFollowersModal = false;
            this.showFollowingModal = false;
            this.$router.push({
                name: 'UserProfile',
                params: { userName: temp_username }
            })
        },

        async exportBlogs(){
            const payload = {
                username: this.profileData.username
            }
            await this.$store.dispatch('exportBlogs', payload)
        }

    },


}
</script>

<style scoped>
.profile-container{
    width: 600px;
}
.inner-container{
    width: 380px;
}

.profile-insights{
    width: 300px;
}

.edit-profile-btn{
    margin: 0px 3px;
}

.connections-list{
    margin: auto;
    width: 80%;
}
.connections-list a{
    text-decoration: none;
    color: black;
}
.connections-list a:hover{
    text-decoration: none;
    color: blue;
}

.profile-insights a{
    color: black;
    text-decoration: none;
}

* {
    font-family: poppins;
}

.no-posts{
    margin-top: 50px;
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

.follow-btn{
    margin: 10px 0px;
}

.posts-container {
    margin: 30px 20px;
    width: 350px;
}

</style>