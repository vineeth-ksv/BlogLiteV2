<template>
    <header>
      <div class="head-container">
        <div class="logo-container">
          <h1>𝔅𝔩𝔬𝔤𝔏𝔦𝔱𝔢</h1>
        </div>
        <div class="profile-container">
          <div class="upper-section">
            <img
                :src="require('@/assets/images/blank-profile-picture.png')"
                id="userProfilePic"
                class="user-profile-pic"
            />
            <div class="names-container">
              <router-link :to="{ name: 'UserProfile', params: { userName: userName } }" class="user-name">
                   <h5>{{ userData.username }}</h5>
              </router-link>
              <p class="full-name">{{ userData.fullname }}</p>
            </div>
          </div>
          <div class="lower-section">
            <router-link to="/home" class="links-in-header">Home</router-link>
            <router-link to="/addpost" class="links-in-header">Add Post</router-link>
            <router-link to="/search" class="links-in-header">Search</router-link>
            <a class="links-in-header" href="javascript:void(0)" @click="logout">Logout</a>
          </div>
        </div>
      </div>
      <slot></slot>
    </header>
  </template>
  
<script>

  export default {
    name: 'AppHeader',
    components: {
    },
    computed: {
      userData(){
        return this.$store.state.userData
      },
      userName() {
        return this.$store.state.loggedInUsername
      },
    },
    methods:{
      logout() {
        this.$store.dispatch('logoutUser')
      },
    },
    created() {
      this.$store.dispatch("fetchUserData");
    }


  }
  </script>
  
  <style scoped>
  *{
  font-family: poppins;
}

.head-container{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 10px 10px;
  background-color: whitesmoke;
  border-radius: 10px;
  margin: 5px 5px;
  height: 95px;
  align-items: center;
}

.logo-container h1{
  font-size: 50px;
}

.upper-section {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  margin-right: 50px;
}

.user-profile-pic {
  height: 60px;
  width: 60px;
  border-radius: 50%;
  margin-right: 10px;
}

.names-container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 40px;
  margin: 0px;
}

.names-container a{
  text-decoration: none;
  color: black;
}

.user-name {
  margin: 0px 0px 0px 0px;
  line-height: 1px;
}

.full-name {
  margin: 0px 0px 0px 0px;
  font-size: 15px;
}


.lower-section {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-end;
}

.links-in-header {
  margin-right: 10px;
  text-decoration: none;
  color: black;
}

.lower-section a {
  position: relative;
  color: #000;
  text-decoration: none;
}

.lower-section a:hover {
  color: #000;
}

.lower-section a::before {
  content: "";
  position: absolute;
  display: block;
  width: 100%;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: blue;
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.lower-section a:hover::before {
  transform: scaleX(1);
}
  </style>
  