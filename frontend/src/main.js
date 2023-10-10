import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import AppHeader from '@/components/AppHeader.vue'
import BlogComponent from '@/components/BlogComponent.vue'
import NoBlogs from '@/components/NoBlogs.vue'
import HomeFeed from '@/components/Feed.vue'
import UserProfile from '@/components/UserProfile.vue'
import ViewPost from '@/components/ViewPost.vue'
import AddPost from '@/components/AddPost.vue'
import EditPost from '@/components/EditPost.vue'
import ArchivedPosts from '@/components/ArchivedPosts.vue'
import EditProfile from '@/components/EditProfile.vue'
import SearchBar from '@/components/Search.vue'
// import HelloWorld from '@/components/HelloWorld.vue'
// Vue.component("HelloWorld",HelloWorld)
// import { Vue } from 'vue'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)



Vue.component("AppHeader", AppHeader)
Vue.component("HomeFeed", HomeFeed)
Vue.component("BlogComponent", BlogComponent)
Vue.component("NoBlogs", NoBlogs)
Vue.component("UserProfile", UserProfile)
Vue.component("ViewPost", ViewPost)
Vue.component("AddPost", AddPost)
Vue.component("EditPost", EditPost)
Vue.component("ArchivedPosts", ArchivedPosts)
Vue.component("EditProfile", EditProfile)
Vue.component("SearchBar", SearchBar)


Vue.config.productionTip = false



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
