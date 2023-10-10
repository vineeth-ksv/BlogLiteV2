<template>
    <div>
        <AppHeader>
            <div class="d-flex justify-content-center">
                <div class="addpost-title">
                    <h3>Add a Blog / Post</h3>
                </div>
            </div>
            <div class="addpost-container d-flex justify-content-center">
                <div class="form-container">
                    <form @submit.prevent="submitForm">
                        <div class="row mb-3">
                            <label for="blogName" class="col-sm-3 col-form-label">Blog Name</label>
                            <div class="col-sm-9">
                                <input type="text" class="form-control" id="blogName" v-model="blogName" required>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <label for="blogDescription" class="col-sm-3 col-form-label">Blog Description</label>
                            <div class="col-sm-9">
                                <textarea class="form-control" id="blogDescription" rows="3" v-model="blogDescription" required></textarea>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <label for="image" class="col-sm-3 col-form-label">Image</label>
                            <div class="col-sm-9">
                                <input type="file" class="form-control-file" id="image" @change="onFileChange" name="blogImage" required>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <b-button variant="primary" type="submit" class="submit-btn">Submit</b-button>
                        </div>
                    </form>
                </div>
                <div class="image-container">
                    <center><p>Image Preview</p></center>
                    <div id="image-preview">
                        <img :src="imagePreviewUrl" v-if="imagePreviewUrl">
                        <img v-else
                            :src="require('@/assets/images/no-image-selected.jpg')"
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
    name: "AddPost",
    components: {
        AppHeader,
    },
    data() {
        return {
            show: false,
            blogName: '',
            blogDescription: '',
            image: null,
            imageName: '',
            imagePreviewUrl: null,
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
        onFileChange(event) {
            this.image = event.target.files[0]
            this.imageName = this.image.name
            this.imagePreviewUrl = URL.createObjectURL(this.image);
        },
        resetFields() {
            this.blogName = ''
            this.blogDescription = ''
            this.image = null,
            this.imageName = ''
        },

        async submitForm() {
            const reader = new FileReader();
            reader.readAsDataURL(this.image);

            await new Promise(resolve => {
                reader.onload = () => {
                resolve();
                };
            });

            const payload = {
                username: this.$store.getters.getLoggedInUsername,
                blogName: this.blogName,
                blogDescription: this.blogDescription,
                blogImage: reader.result.split(",")[1],
                imageName: this.imageName
            }

            await this.$store.dispatch('addPost', payload)
            this.resetFields();
            this.show = false;
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
.submit-btn{
    margin-left: 280px;
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