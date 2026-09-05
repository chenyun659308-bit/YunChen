<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { products } from '../../data/products.js'
import { news } from '../../data/news.js'

const heroProducts = products.slice(0, 4)
const latestNews = news.slice(0, 3)
const scrollY = ref(0)
const currentSlide = ref(0)
let slideTimer = null

const slides = [
  '/carousel/banner1.jpg',
  '/carousel/banner2.jpg',
  '/carousel/banner3.jpg',
  '/carousel/banner4.jpg',
  '/carousel/banner5.jpg'
]

function prevSlide() {
  currentSlide.value = (currentSlide.value - 1 + slides.length) % slides.length
}
function nextSlide() {
  currentSlide.value = (currentSlide.value + 1) % slides.length
}

onMounted(() => {
  window.addEventListener('scroll', () => { scrollY.value = window.scrollY })
  slideTimer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
})
onUnmounted(() => { if (slideTimer) clearInterval(slideTimer) })
</script>

<template>
  <div class="home-page">
    <section class="hero">
      <div
        v-for="(img, i) in slides"
        :key="i"
        class="hero-slide"
        :class="{ active: i === currentSlide }"
        :style="{ backgroundImage: 'url(' + img + ')' }"
      ></div>
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <span class="hero-badge">JIUYOU · Since 2001</span>
        <h1 class="hero-title">JiuYou Electric<br /><span class="gold">Smart Quality Life</span></h1>
        <p class="hero-subtitle">Fans &amp; Heaters Expert · Bringing comfort and convenience to every family</p>
        <div class="hero-actions">
          <router-link to="/products" class="btn-primary">Explore Products</router-link>
          <router-link to="/about" class="btn-outline">About Us</router-link>
        </div>
      </div>
      <button class="carousel-btn carousel-prev" @click="prevSlide">‹</button>
      <button class="carousel-btn carousel-next" @click="nextSlide">›</button>
    </section>

    <section class="stats">
      <div class="container">
        <div class="stats-grid">
          <div
            v-for="(s, i) in [
              { n: '2001', l: 'Founded' },
              { n: '40+', l: 'Export Countries' },
              { n: '10+', l: 'Provinces' },
              { n: '8', l: 'Certifications' },
              { n: 'ISO', l: 'Certified' }
            ]"
            :key="i"
            class="stat-item"
          >
            <span class="stat-num">{{ s.n }}</span>
            <span class="stat-label">{{ s.l }}</span>
          </div>
        </div>
      </div>
    </section>

    <section class="about-section">
      <div class="container">
        <div class="section-header">
          <span class="section-tag">About JiuYou</span>
          <h2 class="section-title">Since 2001 · Fans &amp; Heaters Expert</h2>
        </div>
        <p>Founded in 2001, Zhejiang JiuYou Electric Technology Co., Ltd. specializes in the research, development, production and sales of electric fans and electric heaters.</p>
        <p>Our products are exported to more than 40 countries and regions across Europe, the Middle East, Africa and South America, ranking among the leading fan manufacturers in Cixi for consecutive years.</p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home-page { background: #fff; }
.hero { position: relative; height: 100vh; min-height: 650px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.hero-slide { position: absolute; inset: 0; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.8s ease; }
.hero-slide.active { opacity: 1; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.75), rgba(0,0,0,0.4), rgba(0,0,0,0.6)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; max-width: 800px; padding: 0 20px; }
.hero-badge { display: inline-block; padding: 8px 24px; border: 1px solid rgba(201,168,76,0.4); color: #c9a84c; font-size: 0.78rem; letter-spacing: 3px; margin-bottom: 30px; }
.hero-title { font-size: 3.8rem; font-weight: 300; color: #fff; line-height: 1.2; margin-bottom: 20px; letter-spacing: 3px; }
.hero-title .gold { color: #c9a84c; }
.hero-subtitle { font-size: 1rem; color: rgba(255,255,255,0.55); line-height: 1.8; margin-bottom: 40px; }
.hero-actions { display: flex; gap: 20px; justify-content: center; }
.btn-primary { display: inline-block; padding: 14px 44px; background: #c9a84c; color: #fff; font-size: 0.85rem; letter-spacing: 2px; transition: all 0.3s; }
.btn-primary:hover { background: #b8942e; }
.btn-outline { display: inline-block; padding: 14px 44px; background: transparent; color: #c9a84c; border: 1px solid #c9a84c; font-size: 0.85rem; letter-spacing: 2px; transition: all 0.3s; }
.stats { background: #f8f8f6; padding: 70px 0; }
.stats-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 20px; text-align: center; }
.stat-num { display: block; font-size: 2.2rem; font-weight: 300; color: #c9a84c; margin-bottom: 6px; }
.stat-label { font-size: 0.8rem; color: #999; }
.section { padding: 60px 0; }
.section-header { text-align: center; margin-bottom: 40px; }
.about-section { padding: 100px 0; background: #f8f8f6; text-align: center; }
.about-section p { max-width: 800px; margin: 0 auto 20px; color: #666; line-height: 2; font-size: 0.95rem; }
.about-section .section-title { font-size: 2rem; margin-bottom: 30px; }
.about-section .section-tag { display: block; margin-bottom: 15px; }
.section-tag { color: #c9a84c; font-size: 0.72rem; letter-spacing: 3px; }
.section-title { font-size: 1.8rem; font-weight: 300; color: #1a1a1a; margin: 10px 0; letter-spacing: 2px; }
.carousel-btn { position: absolute; top: 50%; transform: translateY(-50%); z-index: 10; width: 56px; height: 56px; border: 1px solid rgba(255,255,255,0.15); background: rgba(0,0,0,0.25); color: rgba(255,255,255,0.5); font-size: 2.2rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.3s; border-radius: 50%; backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px); font-family: inherit; line-height: 1; outline: none; }
.carousel-btn:hover { background: rgba(0,0,0,0.5); color: #c9a84c; border-color: rgba(201,168,76,0.5); transform: translateY(-50%) scale(1.05); }
.carousel-prev { left: 24px; }
.carousel-next { right: 24px; }
</style>
