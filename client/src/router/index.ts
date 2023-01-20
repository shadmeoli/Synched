import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // [TODO] ->  create and connect the newly added routes | and make them lazy loaded
    {
      path: '/my_playlist',
      name: 'my_playlist',
      component: () => import('../views/MyPlaylist.vue')
    },
    {
      path: '/saved_playlist',
      name: 'saved_playlist',
      component: () => import('../views/SavedPlaylist.vue')
    },
    
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
