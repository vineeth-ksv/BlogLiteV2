<template>
    <div class="page">
      <div class="header">
        <div class="heading">
          <h1>𝔅𝔩𝔬𝔤 𝔏𝔦𝔱𝔢</h1>
        </div>
        <p>Sign up to see photos and videos from your friends.</p>
        <hr>
      </div>
      <div class="container mt-4">
    <h2 class="text-center">Sign Up</h2>
    <b-form @submit="submitForm" class="mt-4">
      <b-form-group label="Email:" label-for="emailInput" v-bind:state="emailState">
        <b-form-input id="emailInput" v-model="form_data.email" required></b-form-input>
        <b-form-invalid-feedback :state="emailState">
          Please enter a valid email address.
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group label="Mobile Number:" label-for="mobileInput" v-bind:state="mobileState">
        <b-form-input id="mobileInput" v-model="form_data.mobile" required></b-form-input>
        <b-form-invalid-feedback :state="mobileState">
          Please enter a valid 10-digit mobile number that starts with 6, 7, 8, or 9.
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group label="Full Name:" label-for="nameInput" v-bind:state="nameState">
        <b-form-input id="nameInput" v-model="form_data.name" required></b-form-input>
      </b-form-group>
      <b-form-group label="Username:" label-for="usernameInput" v-bind:state="usernameState">
        <b-form-input id="usernameInput" v-model="form_data.username" required></b-form-input>
      </b-form-group>
      <b-form-group label="Password:" label-for="passwordInput" v-bind:state="passwordState">
        <b-form-input id="passwordInput" type="password" v-model="form_data.password" required></b-form-input>
        <b-form-invalid-feedback :state="passwordState">
          Please enter a valid password with at least 1 small character, 1 capital character, 1 number, 1 special character, and between 8 to 16 characters long.
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group label="Confirm Password:" label-for="confirmPasswordInput" v-bind:state="confirmPasswordState">
        <b-form-input id="confirmPasswordInput" type="password" v-model="form_data.confirmPassword" required></b-form-input>
        <b-form-invalid-feedback :state="confirmPasswordState">
          Passwords do not match.
        </b-form-invalid-feedback>
      </b-form-group>
      <b-button type="submit" variant="primary" class="mt-4" :disabled="!allFieldsValid">Sign Up</b-button>
      <div class="mt-2">
        Already have an account? <router-link to="/">Login</router-link>.
      </div>
    </b-form>
  </div>
  </div>
  </template>

<script>
export default {
  data() {
    return {
        form_data: {
            email: '',
            mobile: '',
            name: '',
            username: '',
            password: '',
            confirmPassword: '',
        },
    }
  },
  computed: {
    emailState() {
        return this.validateEmail(this.form_data.email) ? true : false;
    },
    mobileState() {
        return this.validateMobile(this.form_data.mobile) ? true : false;
    },
    nameState() {
      return this.form_data.name ? true : false;
    },
    usernameState() {
        return this.form_data.username ? true : false;
    },
    passwordState() {
      return this.validatePassword(this.form_data.password) ? true : false;
    },
    confirmPasswordState() {
      return this.form_data.confirmPassword === this.form_data.password ? true : false;
    },
    allFieldsValid() {
      return this.emailState && this.mobileState && this.nameState && this.usernameState && this.passwordState && this.confirmPasswordState;
    }
  },
  methods: {
        validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+.[^\s@]+$/;
            return re.test(email);
        },
        validateMobile(mobile) {
            const re = /^[6-9]\d{9}$/;
            return re.test(mobile);
        },
        validatePassword(password) {
            const re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@_#$%^&*])[a-zA-Z0-9!@_#$%^&*]{8,16}$/;
            return re.test(password);
        },
        
        submitForm(event) {
            event.preventDefault();
            if (this.allFieldsValid) {
                // fetch call to register API
                fetch(`http://127.0.0.1:5555/api/register`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.form_data)
                })
                .then(response => {
                    if (response.ok){
                        alert('User registered successfully! \n Please login to your account...');
                        this.$router.push('/');  // redirect to login page
                    }
                    else{
                        throw new Error ('Network response was not ok')
                    }
                })
                .catch(error => {
                    console.error('There was problem with the fetch operation', error);
                });
            } 
            else {
                alert('Invalid Form Data');
            }
        }
    }
}
</script>

<style scoped>
</style>