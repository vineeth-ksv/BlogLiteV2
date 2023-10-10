<template>
    <div>
        <AppHeader>
            <div class="d-flex justify-content-center">
                <div class="profile-title">
                    <h3>Edit Profile</h3>
                </div>
            </div>
            <div class="addpost-container d-flex justify-content-center">
                <div class="form-container">
                    <form @submit.prevent="submitForm">
                        <div class="row mb-3">
                            <label for="username" class="col-sm-3 col-form-label">Username</label>
                            <div class="col-sm-9">
                                <input type="text" class="form-control" id="username" v-model="profileData.username" readonly required>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <label for="email" class="col-sm-3 col-form-label">Email</label>
                            <div class="col-sm-9">
                                <input type="text" class="form-control" id="email" rows="3" v-model="profileData.email" required readonly>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <label for="fullname" class="col-sm-3 col-form-label">Full Name</label>
                            <div class="col-sm-9">
                                <input type="text" class="form-control" id="fullname" v-model="profileData.fullname" required>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <label for="mobileNumber" class="col-sm-3 col-form-label">Mobile Number</label>
                            <div class="col-sm-9">
                                <input type="text" class="form-control" id="mobileNumber" rows="3" v-model="profileData.mobile_number" required>
                            </div>
                        </div>
                        <div class="row mb-3 submit-btns">
                            <router-link :to="{ name: 'UserProfile', params: { userName: userName } }" class="user-name">
                                <b-button variant="outline-secondary">Back</b-button>
                            </router-link>
                            <b-button variant="primary" type="submit">Update Profile</b-button>
                        </div>
                    </form>
                </div>
            </div>
        </AppHeader>
    </div>
</template>


<script>
import AppHeader from '@/components/AppHeader.vue'

export default {
    name: "EditProfile",
    components: {
        AppHeader,
    },
    data() {
        return {
            profileData: {},
        }
    },
    mounted() {
        this.profileData = this.$store.getters.getUserData
    },
    computed: {
        userData(){
            return this.$store.state.userData
        },
        userName() {
            return this.$store.getters.getLoggedInUsername
        },
    },
    methods: {
        getBase64Image(base64Image) {
            return "data:image/*;base64," + base64Image;
        },
        onFileChange(event) {
            this.image = event.target.files[0]
            this.imageName = this.image.name
        },

        async submitForm() {
            const payload = {
                username: this.profileData.username,
                fullname: this.profileData.fullname,
                mobile_number: this.profileData.mobile_number,
            }
            console.log(payload)
            await this.$store.dispatch('EditProfile', payload)
        }
    },
}

</script>

<style scoped>
.profile-title{
    margin: 50px 0px;
}
.form-container{
    width: 550px;
}
.submit-btns{
    margin-left: 200px;
}
.submit-btns button{
    margin: 5px;
}
</style>