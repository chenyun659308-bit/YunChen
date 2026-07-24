<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { products } from '../../data/products.js'

const route = useRoute()
const router = useRouter()
const id = Number(route.params.id)
const product = computed(() => products.find(p => p.id === id))
const related = computed(() => products.filter(p => p.category === product.value?.category && p.id !== id).slice(0, 4))
function goDetail(id) { router.push('/product/' + id) }
</script>
<template>
  <div class="detail-page" v-if="product">
    <section class="hero-section"><div class="hero-bg"><img :src="product.image.replace('w=600&h=400','w=1200&h=700')" :alt="product.name"></div><div class="hero-overlay"></div><div class="hero-content"><span class="breadcrumb">首页 / 产品中心 / {{ product.name }}</span><h1>{{ product.name }}</h1><span class="hero-cat">{{ product.category }}</span></div></section>

    <section class="section"><div class="container">
      <div class="detail-layout">
        <div class="detail-image"><img :src="product.image.replace('w=600&h=400','w=800&h=600')" :alt="product.name"></div>
        <div class="detail-info">
          <h2>{{ product.name }}</h2>
          <span class="detail-cat">{{ product.category }}</span>
          <p class="detail-desc" v-if="product.category !== '冷暖净风器'">{{ product.desc }}</p>
          <div class="detail-features" v-if="product.category !== '冷暖净风器'"><h3>产品特点</h3><ul><li v-for="s in product.specs" :key="s">{{ s }}</li></ul></div>
          <div class="detail-meta"><div><h4>产品型号</h4><p>{{ product.name.split(' ')[0] }}</p></div><div><h4>产品系列</h4><p>{{ product.category }}</p></div><div><h4>产品状态</h4><p>在售</p></div><div><h4>保修期限</h4><p>整机三年</p></div></div>
          <button class="back-btn" @click="router.push('/products')">← 返回产品中心</button>
        </div>
      </div>
    </div></section>

    <section class="section specs-section" v-if="product.category !== '冷暖净风器'"><div class="container"><div class="section-header"><span class="section-tag">SPECIFICATIONS</span><h2 class="section-title">技术规格</h2></div>
      <div class="specs-table"><div v-for="(s,i) in product.specs" :key="i" class="spec-row"><span class="spec-label">规格参数 {{ i+1 }}</span><span class="spec-value">{{ s }}</span></div></div>
    </div></section>

    <section class="section related-section" v-if="related.length"><div class="container"><div class="section-header"><span class="section-tag">RELATED</span><h2 class="section-title">相关产品</h2></div>
      <div class="related-grid"><div v-for="p in related" :key="p.id" class="related-card" @click="goDetail(p.id)"><img :src="p.image" :alt="p.name"><h3>{{ p.name }}</h3></div></div>
    </div></section>
  </div>
  <div class="not-found" v-else><h2>产品未找到</h2><router-link to="/products">返回产品中心</router-link></div>
</template>
<style scoped>
.detail-page { background: #fff; }
.hero-section { position: relative; height: 55vh; min-height: 380px; overflow: hidden; display: flex; align-items: center; justify-content: center; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(0,0,0,0.75),rgba(0,0,0,0.3)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; }
.breadcrumb { color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; }
.hero-content h1 { font-size: 2.8rem; color: #fff; font-weight: 300; margin: 15px 0; letter-spacing: 3px; }
.hero-cat { display: inline-block; padding: 5px 18px; border: 1px solid rgba(201,168,76,0.4); color: #c9a84c; font-size: 0.78rem; letter-spacing: 2px; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.section { padding: 70px 0; }
.section-header { text-align: center; margin-bottom: 50px; }
.section-tag { color: #c9a84c; font-size: 0.72rem; letter-spacing: 3px; }
.section-title { font-size: 2rem; font-weight: 300; color: #1a1a1a; margin: 10px 0; letter-spacing: 2px; }
.detail-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: start; }
.detail-image img { width: 100%; display: block; }
.detail-info h2 { font-size: 1.8rem; font-weight: 300; color: #1a1a1a; margin-bottom: 10px; }
.detail-cat { color: #c9a84c; font-size: 0.82rem; letter-spacing: 1px; }
.detail-desc { color: #666; line-height: 1.9; font-size: 0.92rem; margin: 20px 0; }
.detail-features h3 { font-size: 1rem; color: #1a1a1a; margin-bottom: 12px; font-weight: 400; letter-spacing: 1px; }
.detail-features ul { list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.detail-features li { padding: 8px 12px; background: #f8f8f6; color: #555; font-size: 0.82rem; }
.detail-meta { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 25px 0; padding: 20px; background: #f8f8f6; }
.detail-meta h4 { color: #999; font-size: 0.75rem; letter-spacing: 1px; margin-bottom: 5px; }
.detail-meta p { color: #1a1a1a; font-size: 0.9rem; }
.back-btn { padding: 12px 30px; background: none; border: 1px solid #c9a84c; color: #c9a84c; font-size: 0.82rem; cursor: pointer; transition: all 0.3s; font-family: inherit; letter-spacing: 1px; }
.back-btn:hover { background: #c9a84c; color: #fff; }
.specs-section { background: #f8f8f6; }
.specs-table { max-width: 700px; margin: 0 auto; }
.spec-row { display: flex; justify-content: space-between; padding: 15px 20px; border-bottom: 1px solid #e8e8e3; }
.spec-label { color: #888; font-size: 0.85rem; }
.spec-value { color: #1a1a1a; font-size: 0.85rem; }
.related-section { background: #fff; }
.related-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; }
.related-card { cursor: pointer; border: 1px solid #e8e8e3; transition: all 0.3s; }
.related-card:hover { border-color: #c9a84c; }
.related-card { background: #f8f8f6; }
.related-card img { width: 100%; height: 200px; object-fit: contain; display: block; padding: 15px; }
.related-card h3 { padding: 15px; color: #333; font-size: 0.85rem; font-weight: 400; }
.not-found { text-align: center; padding: 100px 20px; }
.not-found h2 { color: #1a1a1a; margin-bottom: 20px; font-weight: 300; }
.not-found a { color: #c9a84c; }
@media (max-width:768px) { .detail-layout { grid-template-columns: 1fr; } .related-grid { grid-template-columns: 1fr 1fr; } .detail-features ul { grid-template-columns: 1fr; } }
</style>
