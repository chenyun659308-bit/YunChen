<template>
  <div class="culture-page">
    <section class="page-hero"><div class="hero-bg"></div><div class="hero-overlay"></div><div class="hero-content"><span class="breadcrumb">首页 / 企业文化</span><h1>企业文化</h1><p>以文化凝聚力量，用创新引领未来</p></div></section>

    <section class="section intro-section"><div class="container"><p class="intro-text">企业文化是企业的灵魂，是推动企业发展的不竭动力。久友电器以"包容、创新、高效、共赢"为核心价值观，致力于为全球家庭打造舒适、安全、健康的居家生活体验。</p></div></section>

    <section class="section culture-section"><div class="container">
      <div class="culture-grid">
        <div class="culture-card primary"><div class="cc-icon"><svg viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="22" stroke="currentColor" stroke-width="1.5"/><path d="M16 24l5 5 11-11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></div><div class="cc-label">使命</div><div class="cc-en">Mission</div><div class="cc-desc">为人类打造舒适居家生活</div></div>
        <div class="culture-card primary"><div class="cc-icon"><svg viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="22" stroke="currentColor" stroke-width="1.5"/><path d="M24 14v20M14 24h20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></div><div class="cc-label">愿景</div><div class="cc-en">Vision</div><div class="cc-desc">打造两季小家电出口企业带头人</div></div>
      </div>

      <div class="culture-divider"><span>核心理念</span></div>

      <div class="value-block"><div class="value-text"><h3 class="value-title">核心价值观</h3><span class="value-en">Core Values</span><p class="value-desc">仰德以求精进，盈利为人谋福。为家电而生、为社会而存、为员工而富、为用户而强</p></div></div>

      <div class="culture-divider"><span>企业精神 · 理念 · 宗旨</span></div>

      <div class="spirit-grid">
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>企业精神</h3><span class="sc-en">Enterprise Spirit</span><p>塑造团队，培养人才，产品创新，追求品质，爱岗敬业，互信互助，诚信共赢</p></div>
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>企业理念</h3><span class="sc-en">Enterprise Philosophy</span><p>诚心创新，造行业精品，真诚合作，塑品牌形象</p></div>
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>企业宗旨</h3><span class="sc-en">Enterprise Purpose</span><p>用高新技术和设计理念，不断创新，着力打造安全、舒适、健康的产品产业</p></div>
      </div>

      <div class="culture-divider"><span>经营 · 产品理念</span></div>

      <div class="spirit-grid two-col">
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>经营理念</h3><span class="sc-en">Management Concept</span><p>包容、创新、高效</p></div>
        <div class="spirit-card"><div class="sc-icon"><svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.2"/><path d="M14 20l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div><h3>产品理念</h3><span class="sc-en">Product Concept</span><p>专业、精细、创新</p></div>
      </div>
    </div></section>
  </div>
</template>
<style scoped>
.culture-page { background: #fff; }
.page-hero { position: relative; height: 50vh; min-height: 350px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; background: url(https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1920&h=600&fit=crop) center/cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(0,0,0,0.8),rgba(0,0,0,0.4)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 12px; }
.hero-content h1 { font-size: 3.2rem; color: #fff; font-weight: 300; margin-bottom: 12px; letter-spacing: 5px; }
.hero-content p { color: rgba(255,255,255,0.5); }
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
  .hero-content h1 { font-size: 2.2rem; }
}
</style>