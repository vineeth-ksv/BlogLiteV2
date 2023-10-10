<template>
    <div>
        <AppHeader>
            <div class="d-flex justify-content-center">
                <div class="addpost-title">
                    <h3>Edit a Blog / Post</h3>
                </div>
            </div>
            <div class="addpost-container d-flex justify-content-center">
                <div class="form-container">
                    <form @submit.prevent="submitForm">
                        <div class="row mb-3">
                            <label for="blogName" class="col-sm-3 col-form-label">Blog Name</label>
                            <div class="col-sm-9">
                                <input type="text" class="form-control" id="blogName" v-model="currentPost.post_name" required>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <label for="blogDescription" class="col-sm-3 col-form-label">Blog Description</label>
                            <div class="col-sm-9">
                                <textarea class="form-control" id="blogDescription" rows="3" v-model="currentPost.post_caption" required></textarea>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <label for="image" class="col-sm-3 col-form-label">Image</label>
                            <div class="col-sm-9">
                                <input type="file" class="form-control-file" id="image" @change="onFileChange" name="blogImage">
                            </div>
                        </div>
                        <div class="row mb-3 submit-btns">
                            <router-link :to="{ name: 'ViewPost', params: { postId: currentPost.post_id }}">
                                <b-button variant="outline-secondary">Back</b-button>
                            </router-link>
                            <b-button variant="primary" type="submit" >Update</b-button>
                        </div>
                    </form>
                </div>
                <div class="image-container">
                    <center><p>Image Preview</p></center>
                    <div id="image-preview">
                        <img :src="imagePreviewUrl" v-if="imagePreviewUrl">
                        <img v-else
                            :src="getBase64Image(currentPost.post_img)"
                            id="no-image-selected"
                            class="no-image-selected"
                        />
                    </div>
                </div>
            </div>
        </AppHeader>
    </div>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'

export default {
    name: "EditPost",
    components: {
        AppHeader,
    },
    data() {
        return {
            image: null,
            currentPost: {},
            imagePreviewUrl: null,
        }
    },
    mounted() {
        const postId = this.$route.params.postId;
        const profileData = this.$store.getters.getProfileData;

        const userPost = profileData.userposts.find(post => post.post_id === postId);

        if (userPost) {
            this.currentPost = userPost;
        } else {
            // handle error
        }
    },
    computed: {
        username() {
            return this.$route.params.userName
        },
        loggedInUsername() {
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
            this.imagePreviewUrl = URL.createObjectURL(this.image);
        },

        async submitForm() {
            var blogImage = null;
            var imageName = null;
            if (this.image === null){
                blogImage = this.currentPost.post_img
                imageName = this.currentPost.img_filename
            }
            else{
                const reader = new FileReader();
                reader.readAsDataURL(this.image);

                await new Promise(resolve => {
                    reader.onload = () => {
                    resolve();
                    };
                });

                blogImage =  reader.result.split(",")[1],
                imageName =  this.imageName
            }

            const payload = {
                username: this.$store.getters.getLoggedInUsername,
                blogId: this.currentPost.post_id,
                blogName: this.currentPost.post_name,
                blogDescription: this.currentPost.post_caption,
                blogImage: blogImage,
                imageName: imageName
            }
            await this.$store.dispatch('EditPost', payload)
        }
    },
}

</script>

<style scoped>
.addpost-title{
    margin: 50px 0px;
}
.form-container{
    width: 550px;
}
.image-container{
    margin: 0px 0px 0px 50px;
}
.submit-btns{
    margin-left: 200px;
}

.submit-btns button{
    margin: 5px;
}
.no-image-selected{
    max-width: 200px;
    max-height: 200px;
}
#image-preview {
    width: 200px;
    height: 200px;
    margin-top: 20px;
}
#image-preview img {
    max-width: 100%;
    max-height: 100%;
}
</style>