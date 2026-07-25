<script setup>
import { useRouter } from 'vue-router'
import { news } from '../../data/news.js'

const router = useRouter()
function goDetail(id) { router.push('/news/' + id) }
</script>
<template>
  <div class="news-page">
    <section class="page-hero"><div class="hero-content"><span class="breadcrumb">首页 / {{ t('news_hero') }}</span><h1>{{ t('news_hero') }}</h1><p>{{ t('news_hero_desc') }}</p></div></section>
    <section class="section"><div class="container">
      <div class="news-list"><div v-for="item in news" :key="item.id" class="news-item"><div class="news-info"><span class="news-date">{{ item.date }}</span><h3>{{ l(item, "title") }}</h3><p>{{ l(item, "summary").slice(0, 120) + '...' }}</p><button class="detail-btn" @click="goDetail(item.id)">{{ t('news_btn') }}</button></div></div></div>
    </div></section>
  </div>
</template>
<style scoped>
.page-hero { background: #1a1a1a; padding: 70px 0; text-align: center; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 12px; }
.page-hero h1 { font-size: 2.8rem; font-weight: 300; color: #fff; margin-bottom: 10px; letter-spacing: 4px; }
.page-hero p { color: rgba(255,255,255,0.45); font-size: 1rem; }

.news-page { background: #fff; }



.hero-content { position: relative; z-index: 2; text-align: center; }

.hero-content h1 { font-size: 2.8rem; color: #fff; font-weight: 300; margin-bottom: 12px; letter-spacing: 4px; }
.hero-content p { color: rgba(255,255,255,0.5); }
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
</style>
