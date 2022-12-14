import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import EczanePage from '../views/EczanePage.vue'
import MusteriPage from '../views/MusteriPage.vue'
import EczaneAdmin from '../views/EczaneAdmin.vue'
import EczaneUser from '../views/EczaneUser.vue'



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
  {
    path: '/musteripage',
    name: 'MusteriPage',
    component: MusteriPage
  },
  {
    path: '/eczaneadmin/:eczaneID',
    name: 'EczaneAdmin',
    component: EczaneAdmin,    
  }, 
  {
    path: '/eczaneuser/:tcNum',
    name: 'EczaneUser',
    component: EczaneUser,    
  },    
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router