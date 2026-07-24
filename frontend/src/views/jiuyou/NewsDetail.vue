<script setup>
import { useRoute, useRouter } from 'vue-router'
import { news } from '../../data/news.js'

const route = useRoute()
const router = useRouter()
const id = Number(route.params.id)
const article = news.find(n => n.id === id)

function getParagraphs() {
  if (!article) return []
  return (article.content || '').split('\n\n')
}
</script>
<template>
  <div class="detail-page" v-if="article">
    <section class="page-hero"><div class="hero-bg"></div><div class="hero-overlay"></div><div class="hero-content"><span class="breadcrumb">首页 / 新闻中心</span><h1>{{ article.title }}</h1><span class="hero-date">{{ article.date }}</span></div></section>
    <section class="section"><div class="container"><h2 style="text-align:center;color:#c9a84c;margin-bottom:30px;">{{ article.title }}</h2><div class="article-content"><p v-for="(p, i) in getParagraphs()" :key="i" class="article-p">{{ p }}</p></div><div style="text-align:center;margin-top:40px;" v-if="!getParagraphs().length"><p style="color:#999;">暂无内容</p></div><button class="back-btn" @click="router.push('/news')">← 返回新闻列表</button></div></section>
  </div>
</template>
<style scoped>
.detail-page { background: #fff; }
.page-hero { position: relative; height: 45vh; min-height: 320px; overflow: hidden; display: flex; align-items: center; justify-content: center; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(0,0,0,0.75),rgba(0,0,0,0.3)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; }
.breadcrumb { color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; }
.hero-content h1 { font-size: 2.2rem; color: #fff; font-weight: 300; margin: 15px 0; letter-spacing: 3px; }
.hero-date { color: rgba(255,255,255,0.4); font-size: 0.85rem; }
.container { max-width: 800px; margin: 0 auto; padding: 0 20px; }
.section { padding: 60px 0; }
.article-content { line-height: 2.2; color: #444; font-size: 0.95rem; }
.article-p { margin-bottom: 20px; text-indent: 2em; }
.back-btn { margin-top: 40px; padding: 12px 30px; background: none; border: 1px solid #c9a84c; color: #c9a84c; font-size: 0.85rem; cursor: pointer; transition: all 0.3s; font-family: inherit; letter-spacing: 1px; }
.back-btn:hover { background: #c9a84c; color: #fff; }
@media (max-width:768px) { .hero-content h1 { font-size: 1.6rem; } }
</style>
