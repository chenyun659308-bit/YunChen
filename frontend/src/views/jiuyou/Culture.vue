<script setup>
import { computed } from 'vue'
import { useI18n } from '../../i18n.js'

const { locale } = useI18n()

const zhCopy = {
  crumb: '首页 / 企业文化',
  heroTitle: '企业文化',
  heroDesc: '以文化凝聚力量，用创新引领未来',
  intro: '企业文化是企业的灵魂，是推动企业发展的不湇动力。久友电器以"包容、创新、高效、双赢"为核心价值观，致力于为全球家庭打造舒适、安全、健康的居家生活体验。',
  card1Label: '使命', card1Sub: 'Mission', card1Desc: '为人类打造舒适居家生活',
  card2Label: '愿景', card2Sub: 'Vision', card2Desc: '打造两季小家电出口企业带头人',
  divider1: '核心理念',
  valueTitle: '核心价值观', valueSub: 'Core Values', valueDesc: '仰德以求精进，盈利为人谋福。为家电而生、为社会而存、为员工而富、为用户而强',
  divider2: '企业精神 · 理念 · 宗旨',
  s1Title: '企业精神', s1Sub: 'Enterprise Spirit', s1Desc: '塑造团队，培养人才，产品创新，追求品质，爱岗敬业，互信互助，诚信双赢',
  s2Title: '企业理念', s2Sub: 'Enterprise Philosophy', s2Desc: '诚心创新，造行业精品，真诚合作，塑品牌形象',
  s3Title: '企业宗旨', s3Sub: 'Enterprise Purpose', s3Desc: '用高新技术和设计理念，不断创新，着力打造安全、舒适、健康的产品产业',
  divider3: '经营 · 产品理念',
  m1Title: '经营理念', m1Sub: 'Management Concept', m1Desc: '包容、创新、高效',
  m2Title: '产品理念', m2Sub: 'Product Concept', m2Desc: '专业、精细、创新'
}

const enCopy = {
  crumb: 'Home / Corporate Culture',
  heroTitle: 'Corporate Culture',
  heroDesc: 'Uniting strength through culture, leading the future with innovation',
  intro: 'Corporate culture is the soul of an enterprise and the driving force behind sustainable growth. With inclusion, innovation, efficiency and win-win cooperation as its core values, JiuYou Electric is committed to bringing comfortable, safe and healthy home experiences to families worldwide.',
  card1Label: 'Mission', card1Sub: '使命', card1Desc: 'Creating comfortable home living for humanity',
  card2Label: 'Vision', card2Sub: '愿景', card2Desc: 'Leading two-season small appliance exporter',
  divider1: 'Core Concepts',
  valueTitle: 'Core Values', valueSub: '核心价值观', valueDesc: 'Virtue drives excellence and benefits all. Dedicated to home appliances, society, employees and users.',
  divider2: 'Enterprise Spirit · Philosophy · Purpose',
  s1Title: 'Enterprise Spirit', s1Sub: '企业精神', s1Desc: 'Build teams, nurture talent, innovate products, pursue quality, stay dedicated and build trust.',
  s2Title: 'Enterprise Philosophy', s2Sub: '企业理念', s2Desc: 'Innovate with sincerity, create industry excellence, cooperate with goodwill and shape a trusted brand.',
  s3Title: 'Enterprise Purpose', s3Sub: '企业宗旨', s3Desc: 'Apply high-tech and inspired design to build a safe, comfortable and healthy product industry.',
  divider3: 'Management & Product Concepts',
  m1Title: 'Management Concept', m1Sub: '经营理念', m1Desc: 'Inclusive, Innovative, Efficient',
  m2Title: 'Product Concept', m2Sub: '产品理念', m2Desc: 'Professional, Meticulous, Innovative'
}

const copy = computed(() => locale.value === 'en' ? enCopy : zhCopy)
</script>
﻿<template>
  <div class="culture-page">
    <section class="page-hero"><div class="hero-bg"><img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=1920&h=500&fit=crop" alt=""></div><div class="hero-overlay"></div><div class="hero-content" style="position:relative;z-index:1;"><span class="breadcrumb">{{ copy.crumb }}</span><h1>{{ copy.heroTitle }}</h1><p>{{ copy.heroDesc }}</p></div></section>
    <section class="section intro-section"><div class="container"><p class="intro-text">{{ copy.intro }}</p></div></section>
    <section class="section culture-section"><div class="container">
      <div class="culture-grid">
        <div class="culture-card primary"><div class="cc-icon"><svg viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="22" stroke="currentColor" stroke-width="1.5"/><path d="M16 24l5 5 11-11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></div><div class="cc-label">{{ copy.card1Label }}</div><div class="cc-en">{{ copy.card1Sub }}</div><div class="cc-desc">{{ copy.card1Desc }}</div></div>
        <div class="culture-card primary"><div class="cc-icon"><svg viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="22" stroke="currentColor" stroke-width="1.5"/><path d="M24 14v20M14 24h20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></div><div class="cc-label">{{ copy.card2Label }}</div><div class="cc-en">{{ copy.card2Sub }}</div><div class="cc-desc">{{ copy.card2Desc }}</div></div>
      </div>
      <div class="culture-divider"><span>{{ copy.divider1 }}</span></div>
      <div class="value-block"><div class="value-text"><h3 class="value-title">{{ copy.valueTitle }}</h3><span class="value-en">{{ copy.valueSub }}</span><p class="value-desc">{{ copy.valueDesc }}</p></div></div>
      <div class="culture-divider"><span>{{ copy.divider2 }}</span></div>
      <div class="spirit-grid">
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>{{ copy.s1Title }}</h3><span class="sc-en">{{ copy.s1Sub }}</span><p>{{ copy.s1Desc }}</p></div>
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>{{ copy.s2Title }}</h3><span class="sc-en">{{ copy.s2Sub }}</span><p>{{ copy.s2Desc }}</p></div>
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>{{ copy.s3Title }}</h3><span class="sc-en">{{ copy.s3Sub }}</span><p>{{ copy.s3Desc }}</p></div>
      </div>
      <div class="culture-divider"><span>{{ copy.divider3 }}</span></div>
      <div class="spirit-grid two-col">
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>{{ copy.m1Title }}</h3><span class="sc-en">{{ copy.m1Sub }}</span><p>{{ copy.m1Desc }}</p></div>
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>{{ copy.m2Title }}</h3><span class="sc-en">{{ copy.m2Sub }}</span><p>{{ copy.m2Desc }}</p></div>
      </div>
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






.culture-page { background: #fff; }







.container { max-width: 1000px; margin: 0 auto; padding: 0 20px; }
.section { padding: 70px 0; }

/* Intro */
.intro-section { background: #fff; text-align: center; padding-top: 80px; padding-bottom: 20px; }
.intro-text { color: #777; font-size: 0.95rem; line-height: 2; max-width: 800px; margin: 0 auto; letter-spacing: 0.5px; }

/* Culture section */
.culture-section { padding-top: 40px; }
.culture-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 50px; }
.culture-card.primary { padding: 45px 35px; background: #fafaf8; border: 1px solid #eae8e3; text-align: center; transition: all 0.4s; }
.culture-card.primary:hover { border-color: #c9a84c; background: #fff; transform: translateY(-3px); }
.cc-icon { color: #c9a84c; width: 48px; height: 48px; margin: 0 auto 16px; opacity: 0.7; }
.cc-label { font-size: 1.3rem; color: #1a1a1a; font-weight: 300; letter-spacing: 3px; margin-bottom: 4px; }
.cc-en { font-size: 0.68rem; color: #bbb; letter-spacing: 2px; display: block; margin-bottom: 14px; }
.cc-desc { color: #666; font-size: 0.92rem; line-height: 1.8; }

/* Divider */
.culture-divider { text-align: center; margin: 40px 0; position: relative; }
.culture-divider::before { content: ''; position: absolute; top: 50%; left: 0; right: 0; height: 1px; background: #e8e8e3; }
.culture-divider span { position: relative; display: inline-block; padding: 0 24px; background: #fff; color: #c9a84c; font-size: 0.78rem; letter-spacing: 4px; }

/* Core Value */
.value-block { text-align: center; padding: 50px 30px; margin-bottom: 20px; background: #fafaf8; border: 1px solid #eae8e3; }
.value-title { font-size: 1.4rem; font-weight: 300; color: #1a1a1a; letter-spacing: 3px; margin-bottom: 4px; }
.value-en { font-size: 0.68rem; color: #bbb; letter-spacing: 2px; display: block; margin-bottom: 16px; }
.value-desc { color: #666; font-size: 0.92rem; line-height: 2; max-width: 650px; margin: 0 auto; }

/* Spirit grid */
.spirit-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 20px; }
.spirit-grid.two-col { grid-template-columns: 1fr 1fr; max-width: 660px; margin-left: auto; margin-right: auto; }
.spirit-card { padding: 35px 25px; background: #fafaf8; border: 1px solid #eae8e3; text-align: center; transition: all 0.4s; }
.spirit-card:hover { border-color: #c9a84c; background: #fff; transform: translateY(-3px); }
.sc-icon { color: #c9a84c; width: 40px; height: 40px; margin: 0 auto 14px; opacity: 0.6; }
.spirit-card h3 { font-size: 1rem; color: #1a1a1a; font-weight: 400; letter-spacing: 2px; margin-bottom: 3px; }
.sc-en { font-size: 0.65rem; color: #bbb; letter-spacing: 2px; display: block; margin-bottom: 12px; }
.spirit-card p { color: #666; font-size: 0.85rem; line-height: 1.9; }

@media (max-width: 768px) {
  .culture-grid { grid-template-columns: 1fr; }
  .spirit-grid { grid-template-columns: 1fr; }
  .spirit-grid.two-col { grid-template-columns: 1fr; }
  
}

.page-hero { position: relative; padding: 0; text-align: center; overflow: hidden; height: 40vh; min-height: 320px; display: flex; align-items: center; justify-content: center; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.3)); z-index: 1; }
.hero-content { position: relative; z-index: 2; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 15px; }
.page-hero h1 { font-size: 3rem; font-weight: 300; color: #fff; margin-bottom: 12px; letter-spacing: 5px; }
.page-hero p { color: rgba(255,255,255,0.5); font-size: 1rem; }
</style>