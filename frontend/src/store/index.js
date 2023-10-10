import router from '@/router'
import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userData: {},
    loggedIn: false,
    loggedInUsername: "",
    alertContent: "",
    feedData: {},
    profileData: {},
    ArchivedPosts: {},
    followersList: [],
    followingList: []
  },
  getters: {
    getUserData: (state) => {
      return state.userData
    },
    getLoggedInUsername: (state) => {
      return state.loggedInUsername
    },
    getFeedData: (state) => {
      return state.feedData
    },
    getProfileData: (state) => {
      return state.profileData
    },
    getArchivedPosts: (state) => {
      return state.ArchivedPosts
    },
    getFollowersList: (state) => {
      return state.followersList
    },
    getFollowingList: (state) => {
      return state.followingList
    },
    getAlertContent: (state) => {
      return state.alertContent
    },
  },
  mutations: {
    login(state, authToken) {
      state.loggedIn = true
      state.authToken = authToken
    },
    logout(state) {
      state.loggedIn = false,
      state.authToken = null,
      state.loggedInUsername = "",
      state.userData = {},
      state.feedData = {},
      state.profileData = {},
      state.ArchivedPosts = {}
    },
    setUserData: (state, data) => {
      state.userData = data
    },
    setUserName: (state, data) => {
      state.loggedInUsername = data
    },
    setFeedData: (state, data) => {
      state.feedData = data;
    },
    setProfileData: (state, data) => {
      state.profileData = data;
    },
    setArchivedPosts: (state, data) => {
      state.ArchivedPosts = data;
    },
    setFollowersList: (state, data) => {
      state.followersList = data
    },
    setFollowingList: (state, data) => {
      state.followingList = data
    },
    setAlertContent: (state, data) => {
      state.alertContent = data
    }
  },
  actions: {
    async loginUser({commit}, payload){
      console.log(payload)
      const login = await fetch('http://127.0.0.1:5555/login?include_auth_token',{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      })

      if(!login.ok){
        alert('Incorrect email or password')
      }

      const data = await login.json()
      localStorage.setItem('email', payload.email)
      localStorage.setItem('token', data.response.user.authentication_token)
      commit('login', data.response.user.authentication_token)

      // Make the additional API call
      const user = await fetch(`http://127.0.0.1:5555/api/${localStorage.getItem('email')}`, {
        headers: {
          'Authentication-Token': localStorage.getItem('token')
        }
      })

      if (user.ok) {
        const data = await user.json()
        commit('setUserData', data)
        commit('setUserName', data.username)
        localStorage.setItem('username', data.username)

      }
      
      router.push('/home')
    },

    async fetchUserData({commit}){
      const user = await fetch(`http://127.0.0.1:5555/api/${localStorage.getItem('email')}`, {
        headers: {
          'Authentication-Token': localStorage.getItem('token')
        }
      })

      if (user.ok) {
        const data = await user.json()
        commit('setUserData', data)
        commit('setUserName', data.username)
      }
    },

    async fetchFeedData({commit}, username) {
      try{
        console.log(username);
        console.log('fetching feed...')
        const response = await fetch(`http://127.0.0.1:5555/api/feed/${localStorage.getItem('username')}`,{
          headers: {
            'Authentication-Token': localStorage.getItem('token')
          }
        });
        const data = await response.json();
        commit("setFeedData", data.feed);
      } catch (error) {
        console.error(error);
      }
    },

    async fetchProfileData({commit}, username) {
      try{
        console.log('fetching profile details...')
        const response = await fetch(`http://127.0.0.1:5555/api/profile/${username}`,{
          headers: {
            'Authentication-Token': localStorage.getItem('token')
          }
        });
        const data = await response.json();
        commit("setProfileData", data.profiledata);

        const connections = await fetch(`http://127.0.0.1:5555/api/connections/${username}`,{
          headers: {
            'Authentication-Token': localStorage.getItem('token')
          }
        })
        const connections_data = await connections.json();
        commit("setFollowersList", connections_data.followers)
        commit("setFollowingList", connections_data.followings)
      } catch(error) {
        console.error(error)
      }
    },

    logoutUser({commit}) {
      localStorage.clear()
      console.log('logged out user...')
      commit('logout')
      router.push('/')
    },

    async addPost({commit, getters}, payload){
      // make API request
      console.log(payload)
        const add_post = await fetch('http://127.0.0.1:5555/api/addpost', {
          method: 'POST',
          headers:{
            "Authentication-Token":localStorage.getItem('token'),
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        })
        if(!add_post.ok){
          alert("couldn't upload post...")
        }
        const data = await add_post.json()
        commit('setAlertContent', data.message)
        console.log('Response:', data)
        await this.dispatch('fetchUserData')
        await this.dispatch('fetchFeedData', getters.getLoggedInUsername)
        router.push('/home')
    },

    async EditPost({commit}, payload){
      //make API request
      try{
        const edit_post_response = await fetch('http://127.0.0.1:5555/api/edit_post', {
          method: 'PUT',
          headers: {
            "Authentication-Token": localStorage.getItem('token'),
            "COntent-Type": 'application/json'
          },
          body: JSON.stringify(payload)
        })

        if(!edit_post_response.ok){
          alert("Couldn't update post...")
        }

        const data = await edit_post_response.json()
        commit('setProfileData', data)
        const username = payload.username
        router.push(`/profile/${username}`)
      } catch(error){
        console.error(error)
      }
    },

    async deletePost({commit}, payload){
      //make API request
      try{
        const delete_post_response = await fetch('http://127.0.0.1:5555/api/delete_post', {
          method: 'DELETE',
          headers: {
            "Authentication-Token": localStorage.getItem('token'),
            "Content-Type": 'application/json'
          },
          body: JSON.stringify(payload)
        })
        if(!delete_post_response.ok){
          alert("couldn't delete post")
        }
        const data = await delete_post_response.json()
        console.log(data)
        commit('setProfileData', data);
        const username = payload.username
        router.push(`/profile/${username}`)
      } catch(error) {
        console.error(error)
      }
    },

    async archivePost({commit}, payload){
      //make API request
      try{
        console.log(payload);
        const archive_post_response = await fetch('http://127.0.0.1:5555/api/archive_post',{
          method: 'PUT',
          headers: {
            "Authentication-Token":localStorage.getItem('token'),
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        })
        if(!archive_post_response.ok){
          alert("couldn't archive post...")
        }
        const data = await archive_post_response.json()
        console.log(data)
        commit('setProfileData', data);
        const username = payload.username
        router.push(`/profile/${username}`)
      } catch(error) {
        console.log(error)
      }
    },

    async archivedPosts({commit}, username){
      console.log("fetching archived posts...")
      console.log(username)
      try{
        const archived_posts_response = await fetch(`http://127.0.0.1:5555/api/${username}/archived_posts`, {
          headers: {
            'Authentication-Token': localStorage.getItem('token')
          }
        })
        if(!archived_posts_response.ok){
          alert("couldn't fetch archived posts...")
        }
        const data = await archived_posts_response.json()
        commit('setArchivedPosts', data.archived_posts)
      } catch(error){
        console.error(error)
      }
    },

    async EditProfile({commit}, payload){
      try{
        const edit_profile_response = await fetch('http://127.0.0.1:5555/api/edit_profile', {
          method: 'PUT',
          headers: {
            "Authentication-Token": localStorage.getItem('token'),
            "Content-Type": 'application/json'
          },
          body: JSON.stringify(payload)
        })

        if(!edit_profile_response.ok){
          alert("Couldn't update profile...")
        }

        const data = await edit_profile_response.json()
        console.log(data)
        commit('setUserData', data)
        router.push(`/profile/${data.username}`)
      } catch(error){
        console.error(error)
      }
    },

    async deleteProfile({commit}, payload){
      try{
        const delete_profile_response = await fetch('http://127.0.0.1:5555/api/delete_profile', {
          method: 'DELETE',
          headers: {
            "Authentication-Token": localStorage.getItem('token'),
            "Content-Type": 'application/json'
          },
          body: JSON.stringify(payload)
        })

        if(!delete_profile_response.ok){
          alert("couldn't delete post")
        }

        const data = await delete_profile_response.json()
        alert(data.msg)
        localStorage.clear()
        commit('logout')
        router.push('/')
      } catch(error){
        console.error(error)
      }
    },

    async followUser({commit}, payload){
      try{
        const follow_user = await fetch('http://127.0.0.1:5555/api/follow', {
          method: 'POST',
          headers:{
            "Authentication-Token":localStorage.getItem('token'),
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        })

        if(!follow_user.ok){
          alert("couldn't follow user...")
        }
        
        const data = await follow_user.json()
        console.log(data)
        commit('setAlertContent', data.msg)
      } catch(error){
        console.error(error)
      }
    },

    async unfollowUser({commit}, payload){
      try{
        const unfollow_user = await fetch('http://127.0.0.1:5555/api/unfollow', {
          method: 'PUT',
          headers:{
            "Authentication-Token":localStorage.getItem('token'),
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        })

        if(!unfollow_user.ok){
          alert("couldn't unfollow user...")
        }
        
        const data = await unfollow_user.json()
        commit('setAlertContent', data.msg)
        console.log(data)
      } catch(error){
        console.error(error)
      }
    },

    async removeFollower({commit}, payload){
      try{
        const remove_follower = await fetch('http://127.0.0.1:5555/api/remove_follower', {
          method: 'DELETE',
          headers: {
            "Authentication-Token":localStorage.getItem('token'),
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        })

        if(!remove_follower.ok){
          alert("Could not remove follower...")
        }

        const data = await remove_follower.json()
        commit("setAlertContent", data.msg)
        console.log(data)

      } catch(error){
        console.error(error)
      }
    },

    async togglePostLike({commit}, payload){
      try{
        const toggle_like = await fetch('http://127.0.0.1:5555/api/toggle_like', {
          method: 'PUT',
          headers: {
            "Authentication-Token": localStorage.getItem('token'),
            "Content-Type": 'application/json'
          },
          body: JSON.stringify(payload)
        })
        if(!toggle_like.ok){
          alert("couldn't like the post...")
        }

        const data = await toggle_like.json();
        commit('setAlertContent', data.msg)
        console.log(data)
        // await this.dispatch('fetchFeedData', getters.getLoggedInUsername)

      } catch(error){
        console.error(error);
      }
    },

    async addComment({commit}, payload){
      try{
        console.log(payload)
        const add_comment = await fetch('http://127.0.0.1:5555/api/add_comment', {
          method: 'POST',
          headers:{
            "Authentication-Token": localStorage.getItem('token'),
            "Content-Type": 'application/json'
          },
          body: JSON.stringify(payload)
        })

        if(!add_comment.ok){
          alert("Could not add comment...")
        }

        const data = await add_comment.json();
        commit('setAlertContent', data.msg);
        console.log(data);
        // await this.dispatch('fetchFeedData', getters.getLoggedInUsername)

      } catch(error){
        console.log(error)
      }
    },

    async deleteComment({commit},payload){
      try{
        console.log(payload);
        const delete_comment = await fetch('http://127.0.0.1:5555/api/delete_comment', {
          method: 'DELETE',
          headers:{
            "Authentication-Token": localStorage.getItem('token'),
            "Content-Type": 'application/json'
          },
          body: JSON.stringify(payload)
        })
        if(!delete_comment.ok){
          alert("Could not delete comment...")
        }

        const data = await delete_comment.json()
        commit('setAlertContent', data.msg);
        console.log(data);
        // await this.dispatch('fetchFeedData', getters.getLoggedInUsername)

      } catch(error){
        console.log(error);
      }
    },

    async exportBlogs({commit}, payload){
      try{
        const export_response = await fetch(`http://127.0.01:5555/api/export_blogs/${payload.username}`, {
          headers: {
            'Authentication-Token': localStorage.getItem('token')
          } 
        })
        
        if(!export_response.ok){
          alert("Could not export blobs...")
        }
        const response_blob = await export_response.blob(); 
        const url = window.URL.createObjectURL(response_blob);
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', `${payload.username}-export_blogs.csv`);
        document.body.appendChild(link);
        link.click();
        commit('setAlertContent', 'blogs exported')

      } catch(error){
        console.error(error)
      }
    }
    
  },
  modules: {
  }
})
