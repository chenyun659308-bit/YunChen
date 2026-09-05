<script setup>
import { computed } from 'vue'
import { useI18n } from '../../i18n.js'

const { t, locale } = useI18n()

const zhCopy = {
  crumb: '首页 / 关于我们',
  heroTitle: '关于我们',
  heroDesc: '专注电风扇与取暖器',
  intro: '浙江久友电器科技有限公司成立于2001年，前身为宁波市久友塑料制品有限公司和慈溪市久友电器制造厂，是一家专注于电风扇和取暖器两大系列产品的研究、开发、生产及销售的创新企业。产品通过CCC、GS、CE、EMC、KETI、UL、ETL及ROHS认证，产品出口于欧洲、中东、非洲、南美等40多个国家和地区，以及国内销售至10多个省市自治区。已成为宁波市小家电电风扇和取暖器生产主打企业之一，并且电风扇出口量连续几年稳居慈溪市电风扇生产企业前列。',
  phil: [
    { n: '01', title: '产品创新', desc: '始终坚持产品创新，诚信立业的经营原则，着力打造安全、舒适、健康的产品。拥有雄厚的产品开发能力和模具制造技术，产品质量稳定，价格合理，深受国内外客户的好评。' },
    { n: '02', title: '质量为先', desc: '自2002年获得ISO9001:2000质量管理体系认证以来，全体员工本着"以质量求生存，以创新求发展"的生产方针，齐心协力，实现企业快速、稳定地发展。' },
    { n: '03', title: '合作共赢', desc: '以"包容、创新、高效、共赢"的理念赢得了客户一致的满意，增进了彼此之间长远的合作和信任。' }
  ],
  honors: [
    '中国家电协会会员', '慈溪市家电联合会成员', '浙江省工商企业信用A级', '守合同重信用单位',
    '浙江省名牌产品', '宁波市知名商标', '慈溪出口名牌', 'ISO9001质量管理体系认证'
  ],
  resp: [
    '公司一直致力于加强内部管理，制定有高要求的《售后服务规定》，重视加强员工素质教育，充实技术队伍，拥有先进生产设备，开展技术改造，狠抓产品开发，注重知识产权保护，严把产品质量关，历年企业的产值利税稳中有升，顾客满意度不断提高。',
    '有感于企业的发展得益于党的政策，致富不忘国家，企业自觉增强诚信纳税的道德观念，树立纳税报国的爱国主义精神，争做诚信纳税的时代楷模。同时，努力构建和谐企业，主动承担社会责任，积极参与社会保险和慈善公益事业，照章纳税，规范经营，做好环境保护，加强安全生产，更好地为消费者服务。为促进企业持续发展，积极为地方经济作贡献，浙江久友电器科技有限公司不断向新的高度攀登。'
  ]
}

const enCopy = {
  crumb: 'Home / About Us',
  heroTitle: 'About Us',
  heroDesc: 'Fans & Heaters Expert',
  intro: 'Founded in 2001, Zhejiang JiuYou Electric Technology Co., Ltd. evolved from Ningbo JiuYou Plastic Products Co., Ltd. and Cixi JiuYou Electric Appliance Factory. It is an innovative enterprise dedicated to the research, development, production and sales of electric fans and heaters. Our products are certified by CCC, GS, CE, EMC, KETI, UL, ETL and ROHS, exported to more than 40 countries and regions across Europe, the Middle East, Africa and South America, and sold in over 10 provinces across China. The company has become one of the leading small-appliance fan and heater manufacturers in Ningbo, with electric fan exports ranking among the top Cixi producers for consecutive years.',
  phil: [
    { n: '01', title: 'Product Innovation', desc: 'We consistently pursue product innovation and integrity-driven business principles to create safe, comfortable and healthy products. Strong development and mold-making capabilities deliver stable quality at reasonable prices, earning praise from domestic and international customers.' },
    { n: '02', title: 'Quality First', desc: 'Since obtaining ISO9001:2000 quality management certification in 2002, all employees have followed the principle of "survive by quality, grow by innovation" to achieve rapid and steady development.' },
    { n: '03', title: 'Win-Win Cooperation', desc: 'With an inclusive, innovative, efficient and win-win philosophy, we have earned consistent customer satisfaction and built long-term cooperation and trust.' }
  ],
  honors: [
    'Member of China Home Appliance Association', 'Member of Cixi Home Appliance Federation',
    'Zhejiang AAA Enterprise Credit', 'Contract-Abiding & Credit-Worthy Unit',
    'Zhejiang Famous Brand Product', 'Ningbo Well-Known Trademark',
    'Cixi Export Famous Brand', 'ISO9001 Quality Management System Certified'
  ],
  resp: [
    'The company continuously strengthens internal management with strict after-sales service regulations, invests in employee education and technical teams, adopts advanced production equipment, carries out technical upgrades, emphasizes product development and intellectual property protection, and strictly controls product quality. Output, profits and customer satisfaction have steadily improved over the years.',
    'Grateful for the development opportunities created by national policies, the company pays taxes in good faith and actively fulfills its social responsibilities. It builds a harmonious workplace, participates in social insurance and charitable causes, complies with regulations, protects the environment, and strengthens production safety to better serve consumers while contributing to sustainable development and the local economy.'
  ]
}

const copy = computed(() => locale.value === 'en' ? enCopy : zhCopy)
</script>
<template>
  <div class="about-page">
    <section class="page-hero"><div class="hero-bg"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1920&h=500&fit=crop" alt=""></div><div class="hero-overlay"></div><div class="hero-content" style="position:relative;z-index:1;"><span class="breadcrumb">{{ copy.crumb }}</span><h1>{{ copy.heroTitle }}</h1><p>{{ copy.heroDesc }}</p></div></section>

    <!-- Company intro -->
    <section class="section"><div class="container"><div class="section-header"><span class="section-tag">ABOUT JIUYOU</span><h2 class="section-title">{{ t('about_hero_title') }}</h2></div>
      <div class="intro-text">
        <p class="intro-p">{{ copy.intro }}</p>
      </div>
    </div></section>

    <!-- Philosophy -->
    <section class="section philosophy-section"><div class="container"><div class="section-header"><span class="section-tag">PHILOSOPHY</span><h2 class="section-title">{{ t('about_phil_title') }}</h2></div>
      <div class="phil-grid">
        <div v-for="p in copy.phil" :key="p.n" class="phil-card"><span class="phil-num">{{ p.n }}</span><h3>{{ p.title }}</h3><p>{{ p.desc }}</p></div>
      </div>
    </div></section>

    <!-- Honors -->
    <section class="section honor-section"><div class="container"><div class="section-header"><span class="section-tag">HONORS</span><h2 class="section-title">{{ t('about_honor_title') }}</h2></div>
      <div class="honor-list"><div v-for="h in copy.honors" :key="h" class="honor-item"><span class="honor-dot"></span><span>{{ h }}</span></div></div>
    </div></section>

    <!-- Responsibility -->
    <section class="section resp-section"><div class="container"><div class="section-header"><span class="section-tag">RESPONSIBILITY</span><h2 class="section-title">{{ t('about_resp_title') }}</h2></div>
      <div class="resp-content"><p v-for="(r, i) in copy.resp" :key="i">{{ r }}</p></div>
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






.about-page { background: #fff; }







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

.page-hero { position: relative; padding: 0; text-align: center; overflow: hidden; height: 40vh; min-height: 320px; display: flex; align-items: center; justify-content: center; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.3)); z-index: 1; }
.hero-content { position: relative; z-index: 2; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 15px; }
.page-hero h1 { font-size: 3rem; font-weight: 300; color: #fff; margin-bottom: 12px; letter-spacing: 5px; }
.page-hero p { color: rgba(255,255,255,0.5); font-size: 1rem; }
</style>