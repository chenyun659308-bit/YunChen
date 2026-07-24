<script setup>
import { ref, computed } from 'vue'
const files = ref([
  { id:1, name:'JY-9800 智能变频吸油烟机产品说明书', type:'PDF', size:'4.2MB', date:'2026-06', cat:'说明书' },
  { id:2, name:'JY-R9 微蒸烤一体机用户手册', type:'PDF', size:'3.8MB', date:'2026-05', cat:'说明书' },
  { id:3, name:'JY-Z7 智能马桶盖安装指南', type:'PDF', size:'3.5MB', date:'2026-04', cat:'说明书' },
  { id:4, name:'JY-K10 全屋新风机使用说明', type:'PDF', size:'4.0MB', date:'2026-06', cat:'说明书' },
  { id:5, name:'JY-A3 空气净化器产品手册', type:'PDF', size:'2.8MB', date:'2026-05', cat:'说明书' },
  { id:6, name:'久友电器2026年产品选型手册', type:'PDF', size:'12.6MB', date:'2026-06', cat:'产品手册' },
  { id:7, name:'智能厨房系列产品画册', type:'PDF', size:'8.5MB', date:'2026-05', cat:'产品手册' },
  { id:8, name:'智能卫浴系列产品画册', type:'PDF', size:'7.2MB', date:'2026-04', cat:'产品手册' },
  { id:9, name:'久友电器企业介绍画册', type:'PDF', size:'8.9MB', date:'2026-03', cat:'企业资料' },
  { id:10, name:'售后服务政策与保修条款', type:'PDF', size:'1.2MB', date:'2026-01', cat:'企业资料' },
  { id:11, name:'智能厨房解决方案白皮书', type:'PDF', size:'6.7MB', date:'2026-02', cat:'技术资料' },
  { id:12, name:'全屋智能家电配置方案', type:'PDF', size:'5.1MB', date:'2026-01', cat:'技术资料' },
  { id:13, name:'智能家电互联互通技术规范', type:'PDF', size:'8.3MB', date:'2026-03', cat:'技术资料' },
  { id:14, name:'JY-7系嵌入式烤箱食谱手册', type:'PDF', size:'3.2MB', date:'2026-04', cat:'产品手册' },
  { id:15, name:'产品能效标识一览表', type:'PDF', size:'1.8MB', date:'2026-05', cat:'企业资料' }
])
const activeCat = ref('全部')
const categories = ['全部','说明书','产品手册','技术资料','企业资料']
const filtered = computed(() => activeCat.value === '全部' ? files.value : files.value.filter(f => f.cat === activeCat.value))
function filter(cat) { activeCat.value = cat }
</script>
<template>
  <div class="downloads-page">
    <section class="page-hero"><div class="hero-bg"></div><div class="hero-overlay"></div><div class="hero-content"><span class="breadcrumb">首页 / {{ t('dl_hero') }}</span><h1>{{ t('dl_hero') }}</h1><p>产品资料、技术文档、企业画册一站式{{ t('dl_btn') }}</p></div></section>
    <section class="section"><div class="container">
      <div class="filter-tabs"><button v-for="cat in categories" :key="cat" :class="['filter-btn', {active:activeCat===cat}]" @click="filter(cat)">{{ cat }}</button></div>
      <div class="download-list"><div v-for="f in filtered" :key="f.id" class="download-item"><div class="dl-icon"><span>{{ f.type }}</span></div><div class="dl-info"><h3>{{ f.name }}</h3><span class="dl-meta">{{ f.cat }} · {{ f.size }} · {{ f.date }}</span></div><button class="dl-btn">{{ t('dl_btn') }}</button></div></div>
    </div></section>
  </div>
</template>
<style scoped>
.downloads-page { background: #fff; }
.page-hero { position: relative; height: 40vh; min-height: 300px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; background: url('https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=1920&h=600&fit=crop') center/cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.4)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 15px; }
.hero-content h1 { font-size: 2.8rem; color: #fff; font-weight: 300; margin-bottom: 12px; letter-spacing: 4px; }
.hero-content p { color: rgba(255,255,255,0.5); }
.container { max-width: 1000px; margin: 0 auto; padding: 0 20px; }
.section { padding: 60px 0; }
.filter-tabs { display: flex; gap: 0; margin-bottom: 30px; border-bottom: 1px solid #e8e8e3; }
.filter-btn { padding: 12px 28px; background: none; border: none; border-bottom: 2px solid transparent; color: #888; cursor: pointer; font-size: 0.85rem; letter-spacing: 1px; transition: all 0.3s; font-family: inherit; }
.filter-btn:hover, .filter-btn.active { color: #1a1a1a; border-bottom-color: #c9a84c; }
.download-item { display: flex; align-items: center; gap: 20px; padding: 20px; border: 1px solid #e8e8e3; margin-bottom: 10px; transition: all 0.3s; }
.download-item:hover { border-color: #c9a84c; }
.dl-icon { width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; background: #f8f8f6; flex-shrink: 0; }
.dl-icon span { color: #c9a84c; font-size: 0.7rem; font-weight: 600; letter-spacing: 1px; }
.dl-info { flex: 1; }
.dl-info h3 { color: #1a1a1a; font-size: 0.9rem; font-weight: 400; margin-bottom: 4px; }
.dl-meta { color: #bbb; font-size: 0.78rem; }
.dl-btn { padding: 8px 24px; background: transparent; border: 1px solid #c9a84c; color: #c9a84c; cursor: pointer; font-size: 0.82rem; letter-spacing: 1px; transition: all 0.3s; font-family: inherit; }
.dl-btn:hover { background: #c9a84c; color: #fff; }
</style>
