<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { products as staticProducts } from '../../data/products.js'
import { useI18n } from '../../i18n.js'

const route = useRoute()
const router = useRouter()
const { locale } = useI18n()
const id = computed(() => Number(route.params.id))
const product = ref(null)
const related = ref([])
const loaded = ref(false)

function imageUrl(p, from = '', to = '') {
  const src = p.image_url || p.image || ''
  if (from && to && typeof src === 'string') return src.replace(from, to)
  return src
}

async function loadProduct() {
  const targetId = id.value
  loaded.value = false
  let list = []
  try {
    const res = await fetch('/api/products/')
    if (res.ok) {
      const data = await res.json()
      if (Array.isArray(data)) list = data
    }
  } catch (e) {
    /* fall back to static products when API is unavailable */
  }
  if (!list.length) list = staticProducts
  const found = list.find(p => Number(p.id) === targetId) || null
  product.value = found
  related.value = found
    ? list.filter(p => p.category === found.category && Number(p.id) !== targetId).slice(0, 4)
    : []
  loaded.value = true
}
onMounted(loadProduct)
watch(id, loadProduct)

function goDetail(id) { router.push('/product/' + id) }

const catEnMap = {
  '全部产品': 'All Products',
  '冷暖净风器': 'Air Purifier & Heater',
  '电风扇': 'Electric Fans',
  '暖风机': 'Heaters',
  '小太阳': 'Sun Heaters'
}
const specMap = {
  '150m³/h新风': '150 m³/h Fresh Air',
  '28dB低噪': '28dB Low Noise',
  'APP控制': 'APP Control',
  'APP远程控制': 'APP Remote Control',
  'CADR 600m³/h': 'CADR 600 m³/h',
  'CADR 80m³/h': 'CADR 80 m³/h',
  'HEPA过滤': 'HEPA Filtration',
  'HEPA高效过滤': 'High-Efficiency HEPA Filter',
  'PM2.5/甲醛显示': 'PM2.5/Formaldehyde Display',
  'PM2.5去除99.9%': '99.9% PM2.5 Removal',
  'USB供电': 'USB Powered',
  'WiFi智能控制': 'WiFi Smart Control',
  '三重过滤': 'Triple Filtration',
  '五重过滤': 'Five-Stage Filtration',
  '倾倒断电': 'Tilt Cut-off',
  '全热交换': 'Full Heat Exchange',
  '冷暖一体': 'Heating & Cooling Combo',
  '壁挂安装': 'Wall-Mounted Installation',
  '多档风速': 'Multiple Wind Speeds',
  '安全防护': 'Safety Protection',
  '快速制热': 'Fast Heating',
  '快速发热': 'Fast Heat-up',
  '智能控温': 'Intelligent Temperature Control',
  '智能温控': 'Smart Temperature Control',
  '杀菌率99.9%': '99.9% Sterilization',
  '桌面设计': 'Desktop Design',
  '滤芯更换提醒': 'Filter Replacement Reminder',
  '睡眠模式26dB': 'Sleep Mode 26dB',
  '空气质量监测': 'Air Quality Monitoring',
  '紫外线消毒': 'UV Sterilization',
  '节能环保': 'Energy Efficient',
  '节能省电': 'Energy Saving',
  '负离子净化': 'Negative Ion Purification',
  '适用10-20㎡': 'Suitable for 10-20 m²',
  '适用20-40㎡': 'Suitable for 20-40 m²',
  '适用50-90㎡': 'Suitable for 50-90 m²',
  '适用医疗场所': 'Suitable for Medical Use',
  '静音运行': 'Quiet Operation'
}
const descMap = {
  '集制冷、制热、净化于一体，高效HEPA滤网，智能温控系统，低至28dB静音运行。': 'Integrated cooling, heating and purification with high-efficiency HEPA filter, smart temperature control and operation as quiet as 28dB.',
  '壁挂式安装，150m³/h新风量，全热交换芯节能省电，三重过滤系统，PM2.5去除率99.9%。': 'Wall-mounted with 150 m³/h fresh air, full heat exchange core for energy savings, triple filtration and 99.9% PM2.5 removal.',
  'CADR值600m³/h，适用面积50-90㎡，五重过滤系统，实时PM2.5/甲醛/VOCs显示，睡眠模式仅26dB。': 'CADR 600 m³/h for 50-90 m² spaces, five-stage filtration with real-time PM2.5/formaldehyde/VOCs display and 26dB sleep mode.',
  '医用级紫外线消毒+HEPA过滤，有效杀灭99.9%细菌病毒，负离子净化。': 'Medical-grade UV sterilization plus HEPA filtration eliminates 99.9% of bacteria and viruses with negative ion purification.',
  '精致小巧桌面设计，CADR值80m³/h，适用面积10-20㎡，USB供电，静音运行。': 'Compact desktop design with CADR 80 m³/h for 10-20 m², USB powered and quiet operation.',
  '电风扇，多档风速，静音运行，节能环保。': 'Electric fan with multiple wind speeds, quiet operation and energy efficiency.',
  '暖风机，快速制热，智能控温，安全防护。': 'Fan heater with fast heating, intelligent temperature control and safety protection.',
  '小太阳取暖器，快速发热，安全倾倒断电，节能省电。': 'Sun heater with fast heat-up, tilt cut-off safety and energy saving.'
}
const uiCopy = computed(() => locale.value === 'en' ? {
  homeLabel: 'Home',
  productPage: 'Products',
  onSale: 'On Sale',
  warranty: '3-Year Warranty',
  warrantyLabel: 'Warranty',
  model: 'Model',
  series: 'Series',
  status: 'Status',
  features: 'Product Features',
  back: 'Back to Products',
  specs: 'Specifications',
  specParam: 'Spec ',
  related: 'Related Products',
  notFound: 'Product Not Found',
  backTo: 'Back to Products'
} : {
  homeLabel: '首页',
  productPage: '产品中心',
  onSale: '在售',
  warranty: '整机三年',
  warrantyLabel: '保修期限',
  model: '产品型号',
  series: '产品系列',
  status: '产品状态',
  features: '产品特点',
  back: '← 返回产品中心',
  specs: '技术规格',
  specParam: '规格参数 ',
  related: '相关产品',
  notFound: '产品未找到',
  backTo: '返回产品中心'
})
function displayCat(cat) { return locale.value === 'en' ? (catEnMap[cat] || cat) : cat }
function displaySpec(s) { return locale.value === 'en' ? (specMap[s] || s) : s }
function displayDesc(d) { return locale.value === 'en' ? (descMap[d] || d) : d }
function descText(p) {
  const raw = locale.value === 'en' ? (p.desc_en || p.desc) : p.desc
  return locale.value === 'en' ? (descMap[raw] || raw) : raw
}
function itemName(p) {
  return locale.value === 'en' ? (p.name_en || p.name) : p.name
}
const specList = computed(() => {
  const p = product.value
  if (!p) return []
  if (locale.value === 'en') {
    if (Array.isArray(p.specs_en) && p.specs_en.length) return p.specs_en
    return (p.specs || []).map(displaySpec)
  }
  return p.specs || []
})
</script>
<template>
  <div class="detail-page" v-if="product">
    <section class="hero-section"><div class="hero-bg"><img :src="imageUrl(product, 'w=600&h=400', 'w=1200&h=700')" :alt="itemName(product)"></div><div class="hero-overlay"></div><div class="hero-content"><span class="breadcrumb"><router-link to="/" class="crumb-home">{{ uiCopy.homeLabel }}</router-link> / {{ uiCopy.productPage }} / {{ itemName(product) }}</span><h1>{{ itemName(product) }}</h1><span class="hero-cat">{{ displayCat(product.category) }}</span></div></section>

    <section class="section"><div class="container">
      <div class="detail-layout">
        <div class="detail-image"><img :src="imageUrl(product, 'w=600&h=400', 'w=800&h=600')" :alt="itemName(product)"></div>
        <div class="detail-info">
          <h2>{{ itemName(product) }}</h2>
          <span class="detail-cat">{{ displayCat(product.category) }}</span>
          <p class="detail-desc" v-if="product.category !== '冷暖净风器'">{{ descText(product) }}</p>
          <div class="detail-features" v-if="product.category !== '冷暖净风器'"><h3>{{ uiCopy.features }}</h3><ul><li v-for="s in specList" :key="s">{{ s }}</li></ul></div>
          <div class="detail-meta"><div><h4>{{ uiCopy.model }}</h4><p>{{ product.name.split(' ')[0] }}</p></div><div><h4>{{ uiCopy.series }}</h4><p>{{ displayCat(product.category) }}</p></div><div><h4>{{ uiCopy.status }}</h4><p>{{ uiCopy.onSale }}</p></div><div><h4>{{ uiCopy.warrantyLabel }}</h4><p>{{ uiCopy.warranty }}</p></div></div>
          <button class="back-btn" @click="router.push('/products')">{{ uiCopy.back }}</button>
        </div>
      </div>
    </div></section>

    <section class="section specs-section" v-if="product.category !== '冷暖净风器'"><div class="container"><div class="section-header"><span class="section-tag">SPECIFICATIONS</span><h2 class="section-title">{{ uiCopy.specs }}</h2></div>
      <div class="specs-table"><div v-for="(s,i) in specList" :key="i" class="spec-row"><span class="spec-label">{{ uiCopy.specParam }}{{ i+1 }}</span><span class="spec-value">{{ s }}</span></div></div>
    </div></section>

    <section class="section related-section" v-if="related.length"><div class="container"><div class="section-header"><span class="section-tag">RELATED</span><h2 class="section-title">{{ uiCopy.related }}</h2></div>
      <div class="related-grid"><div v-for="p in related" :key="p.id" class="related-card" @click="goDetail(p.id)"><img :src="imageUrl(p)" :alt="itemName(p)"><h3>{{ itemName(p) }}</h3></div></div>
    </div></section>
  </div>
  <div class="not-found" v-else-if="loaded"><h2>{{ uiCopy.notFound }}</h2><router-link to="/products">{{ uiCopy.backTo }}</router-link></div>
</template>

<style scoped>
.detail-page { background: #fff; }
.hero-section { position: relative; height: 55vh; min-height: 380px; overflow: hidden; display: flex; align-items: center; justify-content: center; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(0,0,0,0.75),rgba(0,0,0,0.3)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; }
.breadcrumb { color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; }
.hero-content h1 { font-size: 2.8rem; color: #fff; font-weight: 300; margin: 15px 0; letter-spacing: 3px; }
.hero-cat { display: inline-block; padding: 5px 18px; border: 1px solid rgba(201,168,76,0.4); color: #c9a84c; font-size: 0.78rem; letter-spacing: 2px; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.section { padding: 70px 0; }
.section-header { text-align: center; margin-bottom: 50px; }
.section-tag { color: #c9a84c; font-size: 0.72rem; letter-spacing: 3px; }
.section-title { font-size: 2rem; font-weight: 300; color: #1a1a1a; margin: 10px 0; letter-spacing: 2px; }
.detail-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: start; }
.detail-image img { width: 100%; display: block; }
.detail-info h2 { font-size: 1.8rem; font-weight: 300; color: #1a1a1a; margin-bottom: 10px; }
.detail-cat { color: #c9a84c; font-size: 0.82rem; letter-spacing: 1px; }
.detail-desc { color: #666; line-height: 1.9; font-size: 0.92rem; margin: 20px 0; }
.detail-features h3 { font-size: 1rem; color: #1a1a1a; margin-bottom: 12px; font-weight: 400; letter-spacing: 1px; }
.detail-features ul { list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.detail-features li { padding: 8px 12px; background: #f8f8f6; color: #555; font-size: 0.82rem; }
.detail-meta { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 25px 0; padding: 20px; background: #f8f8f6; }
.detail-meta h4 { color: #999; font-size: 0.75rem; letter-spacing: 1px; margin-bottom: 5px; }
.detail-meta p { color: #1a1a1a; font-size: 0.9rem; }
.back-btn { padding: 12px 30px; background: none; border: 1px solid #c9a84c; color: #c9a84c; font-size: 0.82rem; cursor: pointer; transition: all 0.3s; font-family: inherit; letter-spacing: 1px; }
.back-btn:hover { background: #c9a84c; color: #fff; }
.specs-section { background: #f8f8f6; }
.specs-table { max-width: 700px; margin: 0 auto; }
.spec-row { display: flex; justify-content: space-between; padding: 15px 20px; border-bottom: 1px solid #e8e8e3; }
.spec-label { color: #888; font-size: 0.85rem; }
.spec-value { color: #1a1a1a; font-size: 0.85rem; }
.related-section { background: #fff; }
.related-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; }
.related-card { cursor: pointer; border: 1px solid #e8e8e3; transition: all 0.3s; }
.related-card:hover { border-color: #c9a84c; }
.related-card { background: #f8f8f6; }
.related-card img { width: 100%; height: 200px; object-fit: contain; display: block; padding: 15px; }
.related-card h3 { padding: 15px; color: #333; font-size: 0.85rem; font-weight: 400; }
.not-found { text-align: center; padding: 100px 20px; }
.not-found h2 { color: #1a1a1a; margin-bottom: 20px; font-weight: 300; }
.not-found a { color: #c9a84c; }
@media (max-width:768px) { .detail-layout { grid-template-columns: 1fr; } .related-grid { grid-template-columns: 1fr 1fr; } .detail-features ul { grid-template-columns: 1fr; } }

.page-hero { position: relative; padding: 0; text-align: center; overflow: hidden; height: 40vh; min-height: 320px; display: flex; align-items: center; justify-content: center; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.3)); z-index: 1; }
.hero-content { position: relative; z-index: 2; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 15px; }
.page-hero h1 { font-size: 3rem; font-weight: 300; color: #fff; margin-bottom: 12px; letter-spacing: 5px; }
.page-hero p { color: rgba(255,255,255,0.5); font-size: 1rem; }
</style>
