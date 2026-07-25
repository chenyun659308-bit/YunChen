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
    <section class="hero"><div v-for="(img, i) in slides" :key="i" class="hero-slide" :class="{ active: i === currentSlide }" :style="{ backgroundImage: &apos;url(&apos; + img + &apos;)&apos; }"></div><div class="hero-overlay"></div><div class="hero-content"><span class="hero-badge">JIUYOU · 始于2001</span><h1 class="hero-title">久友电器<br/><span class="gold">智造品质生活</span></h1><p class="hero-subtitle">专注电风扇与取暖器 · 让每个家庭享受科技带来的舒适与便捷</p><div class="hero-actions"><router-link to="/products" class="btn-primary">探索产品</router-link><router-link to="/about" class="btn-outline">了解久友</router-link></div></div></section>
    <section class="stats"><div class="container"><div class="stats-grid"><div v-for="(s,i) in [{n:&apos;2001&apos;,l:&apos;公司成立&apos;},{n:&apos;40+&apos;,l:&apos;出口国家&apos;},{n:&apos;10+&apos;,l:&apos;国内省市&apos;},{n:&apos;8&apos;,l:&apos;国际认证&apos;},{n:&apos;ISO&apos;,l:&apos;体系认证&apos;}]" :key="i" class="stat-item"><span class="stat-num">{{ s.n }}</span><span class="stat-label">{{ s.l }}</span></div></div></div></section>
    <section class="about-section"><div class="container"><div class="section-header"><span class="section-tag">关于我们</span><h2 class="section-title">始于2001 · 专注电风扇与取暖器</h2></div><p>浙江久友电器科技有限公司成立于2001年，专注于电风扇和取暖器两大系列产品的研究、开发、生产及销售。</p><p>产品出口欧洲、中东、非洲、南美等40多个国家和地区。电风扇出口量连续几年稳居慈溪市电风扇生产企业前列。</p></div></section>
  </div>
</template>
<style scoped>
.home-page { background: #fff; }
.hero { position: relative; height: 100vh; min-height: 650px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.hero-slide { position: absolute; inset: 0; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.8s ease; }
.hero-slide.active { opacity: 1; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(0,0,0,0.75),rgba(0,0,0,0.4),rgba(0,0,0,0.6)); z-index: 1; }
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
.stats-grid { display: grid; grid-template-columns: repeat(5,1fr); gap: 20px; text-align: center; }
.stat-num { display: block; font-size: 2.2rem; font-weight: 300; color: #c9a84c; margin-bottom: 6px; }
.stat-label { font-size: 0.8rem; color: #999; }
.section { padding: 60px 0; }
.section-header { text-align: center; margin-bottom: 40px; }
.about-section { padding: 100px 0; background: #f8f8f6; text-align: center; }
.about-section p { max-width: 800px; margin: 0 auto 20px; color: #666; line-height: 2; font-size: 0.95rem; text-indent: 2em; }
.about-section .section-title { font-size: 2rem; margin-bottom: 30px; }
.about-section .section-tag { display: block; margin-bottom: 15px; }
.section-tag { color: #c9a84c; font-size: 0.72rem; letter-spacing: 3px; }
.section-title { font-size: 1.8rem; font-weight: 300; color: #1a1a1a; margin: 10px 0; letter-spacing: 2px; }
</style>
