import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/jiuyou/Home.vue'
import About from '../views/jiuyou/About.vue'
import Culture from '../views/jiuyou/Culture.vue'
import Products from '../views/jiuyou/Products.vue'
import ProductDetail from '../views/jiuyou/ProductDetail.vue'
import News from '../views/jiuyou/News.vue'
import NewsDetail from '../views/jiuyou/NewsDetail.vue'
import Downloads from '../views/jiuyou/Downloads.vue'
import Contact from '../views/jiuyou/Contact.vue'

const routes = [
  { path: '/home', name: 'HomeAlias', component: () => import(/* webpackChunkName: "home" */ '../views/jiuyou/Home.vue') },
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  { path: '/culture', name: 'Culture', component: Culture },
  { path: '/products', name: 'Products', component: Products },
  { path: '/product/:id', name: 'ProductDetail', component: ProductDetail },
  { path: '/news', name: 'News', component: News },
  { path: '/news/:id', name: 'NewsDetail', component: NewsDetail },
  { path: '/downloads', name: 'Downloads', component: Downloads },
  { path: '/contact', name: 'Contact', component: Contact }
]

const router = createRouter({ history: createWebHistory(), routes })
export default router
