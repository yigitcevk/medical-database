import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import EczanePage from '../views/EczanePage.vue'



const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/eczanepage',
    name: 'EczanePage',
    component: EczanePage
  },   
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router