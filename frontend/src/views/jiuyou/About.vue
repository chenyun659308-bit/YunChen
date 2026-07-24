<script setup>
const honors = [
  { t: '中国家电协会会员' }, { t: '慈溪市家电联合会成员' },
  { t: '浙江省工商企业信用A级' }, { t: '守合同重信用单位' },
  { t: '浙江省名牌产品' }, { t: '宁波市知名商标' },
  { t: '慈溪出口名牌' }, { t: 'ISO9001质量管理体系认证' }
]
</script>
<template>
  <div class="about-page">
    <section class="page-hero"><div class="hero-bg"></div><div class="hero-overlay"></div><div class="hero-content"><span class="breadcrumb">首页 / 关于我们</span><h1>关于我们</h1><p>专注电风扇与取暖器</p></div></section>

    <!-- Company intro -->
    <section class="section"><div class="container"><div class="section-header"><span class="section-tag">ABOUT JIUYOU</span><h2 class="section-title">{{ t('about_hero_title') }}</h2></div>
      <div class="intro-text">
        <p class="intro-p">浙江久友电器科技有限公司成立于2001年，前身为宁波市久友塑料制品有限公司和慈溪市久友电器制造厂，是一家专注于电风扇和取暖器两大系列产品的研究、开发、生产及销售的创新企业。产品通过CCC、GS、CE、EMC、KETI、UL、ETL及ROHS认证，产品出口于欧洲、中东、非洲、南美等40多个国家和地区，以及国内销售至10多个省市自治区。已成为宁波市小家电电风扇和取暖器生产主打企业之一，并且电风扇出口量连续几年稳居慈溪市电风扇生产企业前列。</p>
      </div>
    </div></section>

    <!-- Philosophy -->
    <section class="section philosophy-section"><div class="container"><div class="section-header"><span class="section-tag">PHILOSOPHY</span><h2 class="section-title">{{ t('about_phil_title') }}</h2></div>
      <div class="phil-grid"><div class="phil-card"><span class="phil-num">01</span><h3>产品创新</h3><p>始终坚持产品创新，诚信立业的经营原则，着力打造安全、舒适、健康的产品。拥有雄厚的产品开发能力和模具制造技术，产品质量稳定，价格合理，深受国内外客户的好评。</p></div>
      <div class="phil-card"><span class="phil-num">02</span><h3>质量为先</h3><p>自2002年获得ISO9001:2000质量管理体系认证以来，全体员工本着"以质量求生存，以创新求发展"的生产方针，齐心协力，实现企业快速、稳定地发展。</p></div>
      <div class="phil-card"><span class="phil-num">03</span><h3>合作共赢</h3><p>以"包容、创新、高效、共赢"的{{ t('about_phil_title') }}赢得了客户一致的满意，增进了彼此之间长远的合作和信任。</p></div></div>
    </div></section>

    <!-- Honors -->
    <section class="section honor-section"><div class="container"><div class="section-header"><span class="section-tag">HONORS</span><h2 class="section-title">{{ t('about_honor_title') }}</h2></div>
      <div class="honor-list"><div v-for="h in honors" :key="h.t" class="honor-item"><span class="honor-dot"></span><span>{{ h.t }}</span></div></div>
    </div></section>

    <!-- Responsibility -->
    <section class="section resp-section"><div class="container"><div class="section-header"><span class="section-tag">RESPONSIBILITY</span><h2 class="section-title">{{ t('about_resp_title') }}</h2></div>
      <div class="resp-content"><p>公司一直致力于加强内部管理，制定有高要求的《售后服务规定》，重视加强员工素质教育，充实技术队伍，拥有先进生产设备，开展技术改造，狠抓产品开发，注重知识产权保护，严把产品质量关，历年企业的产值利税稳中有升，顾客满意度不断提高。</p>
      <p>有感于企业的发展得益于党的政策，致富不忘国家，企业自觉增强诚信纳税的道德观念，树立纳税报国的爱国主义精神，争做诚信纳税的时代楷模。同时，努力构建和谐企业，主动承担社会责任，积极参与社会保险和慈善公益事业，照章纳税，规范经营，做好环境保护，加强安全生产，更好地为消费者服务。为促进企业持续发展，积极为地方经济作贡献，浙江久友电器科技有限公司不断向新的高度攀登。</p></div>
    </div></section>
  </div>
</template>
<style scoped>
.about-page { background: #fff; }
.page-hero { position: relative; height: 50vh; min-height: 350px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; background: url(https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1920&h=700&fit=crop) center/cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(0,0,0,0.8),rgba(0,0,0,0.4)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; }
.breadcrumb { color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; }
.hero-content h1 { font-size: 3rem; color: #fff; font-weight: 300; margin: 15px 0; letter-spacing: 4px; }
.hero-content p { color: rgba(255,255,255,0.5); font-size: 1.05rem; }
.container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
.section { padding: 80px 0; }
.section-header { text-align: center; margin-bottom: 50px; }
.section-tag { color: #c9a84c; font-size: 0.72rem; letter-spacing: 3px; }
.section-title { font-size: 2rem; font-weight: 300; color: #1a1a1a; margin: 10px 0; letter-spacing: 2px; }

.intro-text { max-width: 900px; margin: 0 auto; }
.intro-p { color: #555; line-height: 2; font-size: 0.95rem; text-indent: 2em; }

.philosophy-section { background: #f8f8f6; }
.phil-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 25px; }
.phil-card { padding: 40px 30px; background: #fff; border: 1px solid #e8e8e3; transition: all 0.3s; }
.phil-card:hover { border-color: #c9a84c; }
.phil-num { font-size: 2.5rem; color: rgba(201,168,76,0.15); font-weight: 600; display: block; margin-bottom: 15px; }
.phil-card h3 { color: #1a1a1a; font-size: 1.1rem; font-weight: 400; margin-bottom: 12px; letter-spacing: 1px; }
.phil-card p { color: #888; font-size: 0.85rem; line-height: 1.8; }

.honor-section { background: #fff; }
.honor-list { display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; max-width: 800px; margin: 0 auto; }
.honor-item { display: flex; align-items: center; gap: 10px; padding: 14px 24px; background: #f8f8f6; color: #555; font-size: 0.88rem; border: 1px solid #e8e8e3; }
.honor-dot { width: 6px; height: 6px; background: #c9a84c; flex-shrink: 0; }

.resp-section { background: #f8f8f6; }
.resp-content { max-width: 900px; margin: 0 auto; }
.resp-content p { color: #555; line-height: 2; font-size: 0.92rem; margin-bottom: 20px; text-indent: 2em; }

@media (max-width:768px) { .phil-grid { grid-template-columns: 1fr; } .honor-list { flex-direction: column; align-items: center; } }
</style>