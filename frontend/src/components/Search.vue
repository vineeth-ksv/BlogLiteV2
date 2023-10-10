<template>
    <div>
        <AppHeader>
            <div class="search-container">
                <div class="input-group rounded">
                    <b-form-input 
                        id="search_text" 
                        v-model="searchText" 
                        placeholder="Search user by username ..." 
                        aria-label="Search"
                        aria-describedby="search-addon" 
                        @input="search">
                    </b-form-input>
                </div>
                <br/><br/>

                <div v-if="searchResults.length > 0" class="search-results">
                        <div v-for="(user, index) in searchResults" :key="index" class="search-result">
                            <div>
                                {{ index + 1 }} .
                                <router-link :to="{ name: 'UserProfile', params: { userName: user.username } }">
                                    {{ user.username }}
                                </router-link>
                            </div>
                            <div v-if="user.id !== userData.id">
                                <div v-if="followingIds.includes(user.id)">
                                    <b-button variant="secondary" size="sm" @click="unfollowUser(user.username, user.id)">Unfollow</b-button>
                                </div>
                                <div v-else>
                                    <b-button variant="primary" size="sm" @click="followUser(user.username, user.id)">Follow</b-button>
                                </div>
                            </div>
                        </div>
                </div>
                <div v-else class="no-search-results">
                    <center>
                        <div>
                            <h3>No users found</h3>
                        </div>
                    </center>
                </div>
            </div>
        </AppHeader>
    </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'

export default {
    name: "SearchBar",
    components: {
        AppHeader
    },
    data() {
        return {
            show: false,
            searchText: '',
            searchResults: [],
            followingIds: [],
        }
    },
    computed: {
      userData(){
        return this.$store.state.userData
      },
    },
    methods: {
        search() {
            if (this.searchText !== []) {
                const payload = {
                    query: this.searchText,
                    search_by: this.$store.getters.getLoggedInUsername
                }
                fetch('http://127.0.0.1:5555/api/search', {
                    method: 'POST',
                    headers: {
                        "Authentication-Token": localStorage.getItem('token'),
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                })
                    .then(response => response.json())
                    .then(data => {
                        this.searchResults = data.users
                        this.followingIds = data.following_ids
                        // this.searchResults = data.users.map(user => ({ username: user.username }));
                    })
                    .catch(error => {
                        console.log(error)
                    })
            } else {
                this.searchResults = []
            }
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
                    this.search();
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
            await this.$store.dispatch("followUser", payload);
            this.search();
        }
    }
}
</script>

<style scoped>

.search-container{
    margin: auto;
    margin-top: 50px;
    width: 60%;
}

.search-result{
    margin: auto;
    padding: 10px 8px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 90%;
    border-radius: 5px;
}

.search-result a{
    text-decoration: none;
    color: black;
    font-weight: 500;
}

.search-result a:hover{
    text-decoration: none;
    color: blue;
    font-weight: 500;
}

.search-result:hover{
    background-color: whitesmoke;
}

</style>