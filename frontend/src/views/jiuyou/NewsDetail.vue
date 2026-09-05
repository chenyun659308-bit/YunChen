<script setup>
import { useRoute, useRouter } from 'vue-router'
import { news, news_en } from '../../data/news.js'
import { useI18n } from '../../i18n.js'

const route = useRoute()
const router = useRouter()
const { locale } = useI18n()
const id = Number(route.params.id)
const article = news.find(n => n.id === id)

function titleOf() {
  return locale.value === 'en' ? (news_en[id]?.title_en || article?.title) : article?.title
}
function paragraphs() {
  if (!article) return []
  if (locale.value === 'en') return (news_en[id]?.content_en || '').split('\\n\\n')
  return (article.content || '').split('\\n\\n')
}
function crumb() {
  return locale.value === 'en' ? 'Home / News' : '\u9996\u9875 / \u65b0\u95fb\u4e2d\u5fc3'
}
function emptyText() {
  return locale.value === 'en' ? 'No content' : '\u6682\u65e0\u5185\u5bb9'
}
function backText() {
  return locale.value === 'en' ? 'Back to News' : '\u2190 \u8fd4\u56de\u65b0\u95fb\u5217\u8868'
}
</script>
<template>
  <div class="detail-page" v-if="article">
    <section class="page-hero"><div class="hero-bg"><img src="https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1920&h=500&fit=crop" alt=""></div><div class="hero-overlay"></div><div class="hero-content" style="position:relative;z-index:1;"><span class="breadcrumb">{{ crumb() }}</span><h1>{{ titleOf() }}</h1><span class="hero-date">{{ article.date }}</span></div></section>
    <section class="section"><div class="container"><h2 style="text-align:center;color:#c9a84c;margin-bottom:30px;">{{ titleOf() }}</h2><div class="article-content"><p v-for="(p, i) in paragraphs()" :key="i" class="article-p">{{ p }}</p></div><div style="text-align:center;margin-top:40px;" v-if="!paragraphs().length"><p style="color:#999;">{{ emptyText() }}</p></div><button class="back-btn" @click="router.push('/news')">{{ backText() }}</button></div></section>
  </div>
</template>

<style scoped>
.page-hero { position: relative; background: #fafaf8; padding: 90px 0 80px; text-align: center; overflow: hidden; }
.page-hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent, #c9a84c, transparent); }
.page-hero::after { content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 60px; height: 1px; background: #c9a84c; }
.breadcrumb { display: block; color: #c9a84c; font-size: 0.72rem; letter-spacing: 3px; margin-bottom: 16px; text-transform: uppercase; }
.page-hero h1 { font-size: 2.6rem; font-weight: 300; color: #1a1a1a; margin-bottom: 12px; letter-spacing: 5px; }
.page-hero p { color: #999; font-size: 0.92rem; max-width: 600px; margin: 0 auto; line-height: 1.8; }






.detail-page { background: #fff; }


.hero-bg img { width: 100%; height: 100%; object-fit: cover; }




.hero-date { color: rgba(255,255,255,0.4); font-size: 0.85rem; }
.container { max-width: 800px; margin: 0 auto; padding: 0 20px; }
.section { padding: 60px 0; }
.article-content { line-height: 2.2; color: #444; font-size: 0.95rem; }
.article-p { margin-bottom: 20px; text-indent: 2em; }
.back-btn { margin-top: 40px; padding: 12px 30px; background: none; border: 1px solid #c9a84c; color: #c9a84c; font-size: 0.85rem; cursor: pointer; transition: all 0.3s; font-family: inherit; letter-spacing: 1px; }
.back-btn:hover { background: #c9a84c; color: #fff; }
@media (max-width:768px) {  }

.page-hero { position: relative; padding: 0; text-align: center; overflow: hidden; height: 40vh; min-height: 320px; display: flex; align-items: center; justify-content: center; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.3)); z-index: 1; }
.hero-content { position: relative; z-index: 2; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 15px; }
.page-hero h1 { font-size: 3rem; font-weight: 300; color: #fff; margin-bottom: 12px; letter-spacing: 5px; }
.page-hero p { color: rgba(255,255,255,0.5); font-size: 1rem; }
</style>
