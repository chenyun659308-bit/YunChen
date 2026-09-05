<script setup>
import { useRouter } from 'vue-router'
import { news, news_en } from '../../data/news.js'
import { useI18n } from '../../i18n.js'

const router = useRouter()
const { locale } = useI18n()

function titleOf(item) {
  return locale.value === 'en' ? (news_en[item.id]?.title_en || item.title) : item.title
}
function summaryOf(item) {
  return locale.value === 'en' ? (news_en[item.id]?.summary_en || item.summary) : item.summary
}
function crumb() {
  return locale.value === 'en' ? 'Home / News' : '\u9996\u9875 / \u65b0\u95fb\u4e2d\u5fc3'
}
function goDetail(id) { router.push('/news/' + id) }
</script>
<template>
  <div class="news-page">
    <section class="page-hero"><div class="hero-bg"><img src="https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1920&h=500&fit=crop" alt=""></div><div class="hero-overlay"></div><div class="hero-content" style="position:relative;z-index:1;"><span class="breadcrumb">{{ crumb() }}</span><h1>{{ t('news_hero') }}</h1><p>{{ t('news_hero_desc') }}</p></div></section>
    <section class="section"><div class="container">
      <div class="news-list"><div v-for="item in news" :key="item.id" class="news-item"><div class="news-info"><span class="news-date">{{ item.date }}</span><h3>{{ titleOf(item) }}</h3><p>{{ summaryOf(item).slice(0, 120) + '...' }}</p><button class="detail-btn" @click="goDetail(item.id)">{{ t('news_btn') }}</button></div></div></div>
    </div></section>
  </div>
</template>

<style scoped>
.page-hero { position: relative; background: #fafaf8; padding: 90px 0 80px; text-align: center; overflow: hidden; }
.page-hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent, #c9a84c, transparent); }
.page-hero::after { content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 60px; height: 1px; background: #c9a84c; }
.breadcrumb { display: block; color: #c9a84c; font-size: 0.72rem; letter-spacing: 3px; margin-bottom: 16px; text-transform: uppercase; }
.page-hero h1 { font-size: 2.6rem; font-weight: 300; color: #1a1a1a; margin-bottom: 12px; letter-spacing: 5px; }
.page-hero p { color: #999; font-size: 0.92rem; max-width: 600px; margin: 0 auto; line-height: 1.8; }






.news-page { background: #fff; }







.container { max-width: 900px; margin: 0 auto; padding: 0 20px; }
.section { padding: 60px 0; }
.news-list { display: flex; flex-direction: column; gap: 25px; }
.news-item { display: block; padding: 30px; border-bottom: 1px solid #e8e8e3; transition: all 0.3s; }
.news-item:hover { background: #fafaf8; }
.news-info { flex: 1; display: flex; flex-direction: column; justify-content: center; }
.news-date { color: #c9a84c; font-size: 0.8rem; margin-bottom: 8px; }
.news-info h3 { color: #1a1a1a; font-size: 1.1rem; font-weight: 400; margin-bottom: 10px; line-height: 1.5; }
.news-info p { color: #888; font-size: 0.85rem; line-height: 1.7; margin-bottom: 15px; }
.detail-btn { align-self: flex-start; padding: 8px 24px; background: transparent; border: 1px solid #c9a84c; color: #c9a84c; font-size: 0.82rem; cursor: pointer; letter-spacing: 1px; transition: all 0.3s; font-family: inherit; }
.detail-btn:hover { background: #c9a84c; color: #fff; }
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
