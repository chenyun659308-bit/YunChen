<script setup>
import { useRouter } from 'vue-router'
import { news } from '../../data/news.js'

const router = useRouter()
function goDetail(id) { router.push('/news/' + id) }
</script>
<template>
  <div class="news-page">
    <section class="page-hero"><div class="hero-content" style="position:relative;z-index:1;"><span class="breadcrumb">首页 / {{ t('news_hero') }}</span><h1>{{ t('news_hero') }}</h1><p>{{ t('news_hero_desc') }}</p></div></section>
    <section class="section"><div class="container">
      <div class="news-list"><div v-for="item in news" :key="item.id" class="news-item"><div class="news-info"><span class="news-date">{{ item.date }}</span><h3>{{ l(item, "title") }}</h3><p>{{ l(item, "summary").slice(0, 120) + '...' }}</p><button class="detail-btn" @click="goDetail(item.id)">{{ t('news_btn') }}</button></div></div></div>
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
</style>
