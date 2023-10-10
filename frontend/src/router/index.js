import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import UserProfile from '../components/UserProfile.vue'
import HomeFeed from '../components/Feed.vue'
import ViewPost from '../components/ViewPost.vue'
import AddPost from '../components/AddPost.vue'
import EditPost from '../components/EditPost.vue'
import ArchivedPosts from '../components/ArchivedPosts.vue'
import EditProfile from '../components/EditProfile.vue'
import SearchBar from '../components/Search.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/home',
    name: 'HomeFeed',
    component: HomeFeed
  },
  {
    path: '/search',
    name: 'SearchBar',
    component: SearchBar
  },
  {
    path: '/profile/:userName',
    name: 'UserProfile',
    component: UserProfile
  },
  {
    path: '/archived_posts',
    name: 'ArchivedPosts',
    component: ArchivedPosts
  },
  {
    path: '/edit_profile',
    name: 'EditProfile',
    component: EditProfile
  },
  {
    path: '/addpost',
    name: 'AddPost',
    component: AddPost
  },
  {
    path: '/viewpost/:postId',
    name: 'ViewPost',
    component: ViewPost
  },
  {
    path: '/editpost/:postId',
    name: 'EditPost',
    component: EditPost
  }
]

const router = new VueRouter({
  routes
})

export default router
