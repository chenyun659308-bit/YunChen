<script setup>
const samples = [
  { id: 1, name: '久友风扇样本册', file: '/downloads/风扇样本册.pdf', size: '19.6MB', pages: 32, date: '2026-07' },
  { id: 2, name: '久友取暖器样本册', file: '/downloads/取暖器样本册.pdf', size: '10.3MB', pages: 20, date: '2026-07' }
]
</script>
<template>
  <div class="downloads-page">
    <section class="page-hero"><div class="hero-content"><span class="breadcrumb">首页 / 样本册下载</span><h1>产品样本册</h1><p>久友电器全系列产品样本册，了解更多产品详情与技术参数</p></div></section>

    <section class="intro-section"><div class="container"><p class="intro-text">欢迎下载久友电器产品样本册。样本册涵盖公司全系列产品详细信息、技术参数及应用场景，为您提供全面的产品参考。</p></div></section>

    <section class="section"><div class="container">
      <div class="section-header"><span class="section-tag">CATALOGS</span><h2 class="section-title">选择样本册</h2><p class="section-desc">点击下方卡片即可下载对应的 PDF 样本册</p></div>
      <div class="sample-grid">
        <div v-for="s in samples" :key="s.id" class="sample-card">
          <div class="card-top">
            <div class="sample-icon"><svg viewBox="0 0 48 48" fill="none"><rect x="6" y="4" width="36" height="40" rx="3" stroke="#c9a84c" stroke-width="1.5"/><path d="M16 14h16M16 20h16M16 26h12" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round"/><path d="M34 30l6 6-6 6" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
            <span class="sample-type">产品样本册</span>
          </div>
          <h3 class="sample-name">{{ s.name }}</h3>
          <div class="sample-specs"><span class="spec-item"><span class="spec-label">格式</span><span class="spec-val">PDF</span></span><span class="spec-divider"></span><span class="spec-item"><span class="spec-label">大小</span><span class="spec-val">{{ s.size }}</span></span><span class="spec-divider"></span><span class="spec-item"><span class="spec-label">页数</span><span class="spec-val">{{ s.pages }}页</span></span></div>
          <a :href="s.file" class="dl-btn" download><span class="dl-icon">↓</span> 下载样本册</a>
        </div>
      </div>
    </div></section>

    <section class="tips-section"><div class="container"><div class="tips-box"><span class="tips-icon">ⓘ</span><p>样本册为 PDF 格式，建议使用 Adobe Acrobat Reader 或浏览器内置 PDF 阅读器打开。</p></div></div></section>
  </div>
</template>
<style scoped>
.page-hero { background: #1a1a1a; padding: 70px 0; text-align: center; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 12px; }
.page-hero h1 { font-size: 2.8rem; font-weight: 300; color: #fff; margin-bottom: 10px; letter-spacing: 4px; }
.page-hero p { color: rgba(255,255,255,0.45); font-size: 1rem; }

.downloads-page { background: #fff; }



.hero-content { position: relative; z-index: 2; text-align: center; }

.hero-content h1 { font-size: 3rem; color: #fff; font-weight: 300; margin-bottom: 12px; letter-spacing: 5px; }
.hero-content p { color: rgba(255,255,255,0.5); font-size: 0.95rem; }
.intro-section { padding: 50px 0 0; text-align: center; }
.intro-text { max-width: 680px; margin: 0 auto; color: #888; font-size: 0.9rem; line-height: 1.9; }
.container { max-width: 860px; margin: 0 auto; padding: 0 20px; }
.section { padding: 60px 0; }
.section-header { text-align: center; margin-bottom: 45px; }
.section-tag { color: #c9a84c; font-size: 0.7rem; letter-spacing: 4px; display: block; margin-bottom: 10px; font-weight: 500; }
.section-title { font-size: 1.8rem; font-weight: 300; color: #1a1a1a; letter-spacing: 4px; margin: 0 0 10px; }
.section-desc { color: #aaa; font-size: 0.85rem; margin: 0; }
.sample-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; max-width: 700px; margin: 0 auto; }
.sample-card { padding: 0; border: 1px solid #e8e8e3; text-align: center; transition: all 0.4s; overflow: hidden; }
.sample-card:hover { border-color: #c9a84c; box-shadow: 0 8px 40px rgba(0,0,0,0.06); transform: translateY(-4px); }
.card-top { padding: 40px 30px 20px; background: #fafaf8; border-bottom: 1px solid #e8e8e3; }
.sample-icon { width: 56px; height: 56px; margin: 0 auto 12px; }
.sample-icon svg { width: 100%; height: 100%; }
.sample-type { display: inline-block; padding: 3px 14px; background: rgba(201,168,76,0.1); color: #c9a84c; font-size: 0.7rem; letter-spacing: 2px; }
.sample-name { font-size: 1.1rem; color: #1a1a1a; font-weight: 400; letter-spacing: 2px; margin: 24px 0 16px; }
.sample-specs { display: flex; justify-content: center; align-items: center; gap: 20px; margin-bottom: 24px; padding: 0 20px; }
.spec-item { display: flex; flex-direction: column; align-items: center; gap: 4px; }
.spec-label { color: #bbb; font-size: 0.7rem; letter-spacing: 1px; }
.spec-val { color: #555; font-size: 0.85rem; font-weight: 500; }
.spec-divider { width: 1px; height: 28px; background: #e0e0e0; }
.dl-btn { display: inline-flex; align-items: center; gap: 8px; margin-bottom: 30px; padding: 12px 36px; background: transparent; border: 1px solid #c9a84c; color: #c9a84c; text-decoration: none; font-size: 0.82rem; letter-spacing: 2px; transition: all 0.3s; }
.dl-btn:hover { background: #c9a84c; color: #fff; }
.dl-icon { font-size: 1.1rem; }
.tips-section { padding: 0 0 60px; }
.tips-box { display: flex; align-items: center; gap: 12px; max-width: 600px; margin: 0 auto; padding: 16px 24px; background: #fafaf8; border: 1px solid #e8e8e3; }
.tips-icon { color: #c9a84c; font-size: 1.1rem; flex-shrink: 0; }
.tips-box p { color: #999; font-size: 0.78rem; margin: 0; line-height: 1.6; }
</style>
