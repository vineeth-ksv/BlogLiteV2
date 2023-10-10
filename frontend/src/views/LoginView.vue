<template>
    <div>
      <b-container fluid>
        <div class="head-container">
          <h1>𝔅𝔩𝔬𝔤 𝔏𝔦𝔱𝔢</h1>
          <p>Blog Lite helps you to connect and share with the people in your life.</p>
        </div>
        <b-row>
          <b-col md="7" class="blogliteimage">
            <b-img :src="require('@/assets/images/blogliteimg.png')" fluid alt="Blog Lite Image"></b-img>
          </b-col>
          <b-col md="5">
            <div class="login-container">
              <b-card>
                    <div class="login-header">
                        <h4>𝔅𝔩𝔬𝔤 𝔏𝔦𝔱𝔢</h4>
                    </div>
                <!-- <b-form @submit="onSubmit"  v-if="!formSuccess"> -->
                <b-form @submit="onSubmit">
                  <b-form-group id="enail-group" label="Email:" label-for="email">
                    <b-form-input id="email" v-model="user.email" type="text" placeholder="Enter Email" required></b-form-input>
                  </b-form-group>
  
                  <b-form-group id="password-group" label="Password:" label-for="password">
                    <b-form-input id="password" v-model="user.password" type="password" placeholder="Enter password" required></b-form-input>
                  </b-form-group>
                  <div class="login-btn-container">
                    <b-button type="submit" variant="primary" class="login-button" title="login">Log In</b-button>
                  </div>
                </b-form>
                <!-- <b-card-text v-else>
                  <p>Logging you in...</p>
                </b-card-text> -->
                  <div class="separator">
                    <div class="line"></div>
                  </div>
                  <div class="other">
                    <a class="forgot-password" href="#">Forgot password?</a>
                  </div>
                  <div class="signup-container">
                    <p>Don't have an account? <router-link to="/signup">Sign Up</router-link></p>
                  </div>
              </b-card>
            </div>
          </b-col>
        </b-row>
        <div class="footer">
          <p>© 2023 Blog Lite</p>
        </div>
      </b-container>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginView',
    data() {
      return {
        user: {
          email: '',
          password: '',
        },
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault();
        this.$store.dispatch('loginUser', {email: this.user.email, password: this.user.password})
      },
    },
    // mounted() {
    //     this.user.email = "saivineeth.ksv@gmail.com";
    //     this.user.password = "Vineeth_28";
    //   }
  }

  </script>
  
  <style scoped>
  /* Your custom CSS styles go here */
  .head-container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    margin-top: 20px;
  }
  .head-container h1{
    font-size: 50px;
    margin: 0px;
    font-weight: 550;
  }

  .blogliteimage{
    width: 700px;
  }

  .blogliteimage img{
    width: 1000px;
    height: 500px;
  }
  .login-container {
    width: 400px;
    margin: 50px auto;
    border: 1px solid #dbdbdb;
    border-radius: 5px;
    padding: 20px;
    background-color: #fff;
  }

  .login-header {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 20px;
  }

  .login-header h4 {
    font-size: 2rem;
    font-weight: 600;
    color: #262626;
  }

  .login-btn-container{
    display: flex;
    flex-direction: row;
    justify-content: center;
  }
  .login-button {
    background-color: #2c7aee;
    color: #fff;
    font-size: 16px;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 3px;
    border: none;
    cursor: pointer;
    margin-top: 20px;
  }

  .login-button:hover {
    background-color: #265b9a;
  }

  .login-button:active {
    background-color: #0a4f9e;
  }

  .separator {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #999;
    margin-top: 6px;
  }

  .separator .line {
    margin: 20px 0px;
    height: 1px;
    width: 100%;
    background-color: #dbdbdb;
  }

  .other {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin: 10px 0px;
  }

  .forgot-password {
    font-size: 11px;
    color: #003569;
  }

  .signup-container{
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

  .footer {
    bottom: 0;
    height: 2.5rem;
    margin-top: 50px;
  }

  .footer p {
    margin: 10px 0;
    text-align: center;
    color: #8e9096;
    font-size: 14px;
  }

  /* flash messages styling */

</style>


  