<script setup>
const samples = [
  { id: 1, name: '久友风扇样本册', file: '/downloads/风扇样本册.pdf', size: '19.6MB', date: '2026-07' },
  { id: 2, name: '久友取暖器样本册', file: '/downloads/取暖器样本册.pdf', size: '10.3MB', date: '2026-07' }
]
</script>
<template>
  <div class="downloads-page">
    <section class="page-hero"><div class="hero-bg"></div><div class="hero-overlay"></div><div class="hero-content"><span class="breadcrumb">首页 / 样本册下载</span><h1>样本册下载</h1><p>久友电器产品样本册，了解更多产品详情</p></div></section>
    <section class="section"><div class="container">
      <div class="section-header"><span class="section-tag">SAMPLE BOOKS</span><h2 class="section-title">产品样本册</h2></div>
      <div class="sample-grid">
        <div v-for="s in samples" :key="s.id" class="sample-card">
          <div class="sample-icon"><svg viewBox="0 0 40 40" fill="none"><rect x="5" y="3" width="30" height="34" rx="2" stroke="#c9a84c" stroke-width="1.2"/><path d="M12 12h16M12 18h16M12 24h12" stroke="#c9a84c" stroke-width="1" stroke-linecap="round"/></svg></div>
          <h3 class="sample-name">{{ s.name }}</h3>
          <span class="sample-meta">PDF · {{ s.size }} · {{ s.date }}</span>
          <a :href="s.file" class="dl-btn" download>下载样本册</a>
        </div>
      </div>
    </div></section>
  </div>
</template>
<style scoped>
.downloads-page { background: #fff; }
.page-hero { position: relative; height: 35vh; min-height: 280px; display: flex; align-items: center; justify-content: center; overflow: hidden; }

.hero-bg { position: absolute; inset: 0; background: url('https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=1600photo-1558618666-fcd25c85f82e?w=1920&h=600&fit=croph=500photo-1558618666-fcd25c85f82e?w=1920&h=600&fit=cropfit=crop') center/cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.4)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 15px; }
.hero-content h1 { font-size: 2.6rem; color: #fff; font-weight: 300; margin-bottom: 12px; letter-spacing: 5px; }
.hero-content p { color: rgba(255,255,255,0.5); }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.section { padding: 60px 0; }
.section-header { text-align: center; margin-bottom: 40px; }
.section-tag { color: #c9a84c; font-size: 0.7rem; letter-spacing: 3px; display: block; margin-bottom: 10px; }
.section-title { font-size: 1.6rem; font-weight: 300; color: #fff; letter-spacing: 3px; margin: 0; }
.sample-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; max-width: 1200px; margin: 0 auto; }
.sample-card { padding: 40px 30px; border: 1px solid #e8e8e3; text-align: center; transition: all 0.3s; }
.sample-card:hover { border-color: #c9a84c; }
.sample-icon { width: 48px; height: 48px; margin: 0 auto 16px; opacity: 0.7; }
.sample-name { font-size: 1rem; color: #fff; font-weight: 400; letter-spacing: 1px; margin-bottom: 8px; }
.sample-meta { display: block; color: #bbb; font-size: 0.78rem; margin-bottom: 24px; }
.dl-btn { display: inline-block; padding: 10px 32px; background: transparent; border: 1px solid #c9a84c; color: #c9a84c; text-decoration: none; font-size: 0.8rem; letter-spacing: 2px; transition: all 0.3s; }
.dl-btn:hover { background: #c9a84c; color: #fff; }

@keyframes heroBgShift {
  0%,100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
@keyframes heroGlowBar {
  0%,100% { background-position: 0% 0%; }
  50% { background-position: 100% 0%; }
}

</style>
