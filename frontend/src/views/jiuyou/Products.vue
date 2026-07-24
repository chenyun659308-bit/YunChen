<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { products, categories } from '../../data/products.js'

const route = useRoute()
const router = useRouter()
const searchQ = ref(route.query.q || '')
const activeCat = ref(route.query.cat || '全部产品')
const currentPage = ref(1)
const perPage = 8

const filtered = computed(() => {
  let result = products
  if (activeCat.value !== '全部产品') result = result.filter(p => p.category === activeCat.value)
  if (searchQ.value.trim()) {
    const q = searchQ.value.trim().toLowerCase()
    result = result.filter(p => p.name.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q) || p.category.includes(q))
  }
  return result
})
const totalPages = computed(() => Math.ceil(filtered.value.length / perPage))
const paged = computed(() => filtered.value.slice((currentPage.value - 1) * perPage, currentPage.value * perPage))
const expandedCats = ref({})
const catProducts = computed(() => {
  const map = {}
  products.filter(p => p.category).forEach(p => { if (!map[p.category]) map[p.category] = []; map[p.category].push(p) })
  return Object.entries(map)
})
function toggleCat(cat) {
  if (expandedCats.value[cat] === undefined) expandedCats.value[cat] = true
  expandedCats.value[cat] = !expandedCats.value[cat]
}

function setCat(cat) { activeCat.value = cat; currentPage.value = 1; router.replace({ query: { cat: cat !== '全部产品' ? cat : undefined } }) }
function goDetail(id) { router.push('/product/' + id) }
function prevPage() { if (currentPage.value > 1) currentPage.value-- }
function nextPage() { if (currentPage.value < totalPages.value) currentPage.value++ }
</script>
<template>
  <div class="products-page">
    <section class="page-hero"><div class="hero-content"><span class="breadcrumb">首页 / {{ t('pro_hero') }}</span><h1>{{ t('pro_hero') }}</h1><p>{{ t('pro_hero_desc') }}</p></div></section>
    <div class="container main-layout">
      <!-- Left sidebar catalog -->
      <aside class="sidebar">
        <h3 class="sidebar-title">{{ t('pro_catalog') }}</h3>
        <div v-for="[cat, items] in catProducts" :key="cat" class="sidebar-group">
          <h4 class="sidebar-cat" @click="setCat(cat)">
            <span class="cat-label">{{ cat }}</span>
            <span class="toggle-icon" @click.stop="toggleCat(cat)">{{ expandedCats[cat] ? '−' : '+' }}</span>
          </h4>
          <transition name="collapse">
            <ul v-show="expandedCats[cat]" class="sidebar-list"><li v-for="p in items" :key="p.id" class="sidebar-item" @click="goDetail(p.id)">{{ l(p, "name") }}</li></ul>
          </transition>
        </div>
      </aside>
      <!-- Right content -->
      <main class="main-content">
        <div class="toolbar"><div class="search-box"><input v-model="searchQ" placeholder="搜索产品名称" class="search-input"><button @click="currentPage=1" class="search-btn">搜索</button></div><span class="result-count">共 {{ filtered.length }} {{ t('pro_count') }}</span></div>
        <div v-if="paged.length === 0" class="empty-state"><p>没有找到匹配的产品</p></div>
        <div v-else class="product-grid"><div v-for="p in paged" :key="p.id" class="product-card"><div class="product-img"><img :src="p.image" :alt="p.name"></div><div class="product-info"><h3>{{ l(p, "name") }}</h3><button class="detail-btn" @click="goDetail(p.id)">{{ t('pro_detail') }}</button></div></div></div>
        <!-- Pagination -->
        <div class="pagination" v-if="totalPages > 1"><button class="page-btn" :disabled="currentPage===1" @click="prevPage">{{ t('pro_prev') }}</button><button v-for="p in totalPages" :key="p" :class="['page-btn', { active: p === currentPage }]" @click="currentPage = p">{{ p }}</button><button class="page-btn" :disabled="currentPage===totalPages" @click="nextPage">{{ t('pro_next') }}</button></div>
      </main>
    </div>
  </div>
</template>
<style scoped>
.products-page { background: #fff; }
.page-hero { background: #1a1a1a; padding: 70px 0; text-align: center; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 12px; }
.page-hero h1 { font-size: 2.8rem; font-weight: 300; color: #fff; margin-bottom: 10px; letter-spacing: 4px; }
.page-hero p { color: rgba(255,255,255,0.45); font-size: 1rem; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.main-layout { display: flex; gap: 40px; padding: 40px 20px; align-items: flex-start; }

/* Sidebar */
.sidebar { width: 240px; flex-shrink: 0; position: sticky; top: 120px; }
.sidebar-title { font-size: 1rem; font-weight: 400; color: #1a1a1a; margin-bottom: 25px; padding-bottom: 12px; border-bottom: 2px solid #c9a84c; letter-spacing: 2px; }
.sidebar-group { margin-bottom: 20px; }
.sidebar-cat { display: flex; align-items: center; justify-content: space-between; font-size: 0.88rem; color: #c9a84c; cursor: pointer; font-weight: 400; margin-bottom: 8px; padding: 6px 10px; background: #f8f8f6; transition: all 0.2s; letter-spacing: 1px; }
.sidebar-cat:hover { background: rgba(201,168,76,0.1); }
.cat-label { flex: 1; }
.toggle-icon { font-size: 1rem; color: #c9a84c; line-height: 1; user-select: none; width: 20px; text-align: center; transition: transform 0.2s; }
.toggle-icon:hover { opacity: 0.7; }
.sidebar-list { list-style: none; padding: 0; margin: 0; overflow: hidden; }
.sidebar-item { padding: 6px 10px 6px 18px; color: #888; font-size: 0.8rem; cursor: pointer; transition: all 0.2s; border-left: 1px solid #e8e8e3; }
.sidebar-item:hover { color: #1a1a1a; border-left-color: #c9a84c; padding-left: 22px; }
 
.collapse-enter-active, .collapse-leave-active { transition: all 0.25s ease; overflow: hidden; }
.collapse-enter-from, .collapse-leave-to { opacity: 0; max-height: 0; padding-top: 0; padding-bottom: 0; }
.collapse-enter-to, .collapse-leave-from { opacity: 1; max-height: 300px; }

/* Main */
.main-content { flex: 1; min-width: 0; }
.toolbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 1px solid #e8e8e3; gap: 15px; }
.search-box { display: flex; border: 1px solid #e0e0db; }
.search-input { padding: 10px 14px; border: none; font-size: 0.82rem; outline: none; font-family: inherit; width: 220px; color: #1a1a1a; }
.search-btn { padding: 10px 20px; background: #c9a84c; color: #fff; border: none; font-size: 0.78rem; cursor: pointer; letter-spacing: 1px; transition: all 0.3s; }
.search-btn:hover { background: #b8942e; }
.result-count { color: #999; font-size: 0.82rem; white-space: nowrap; }
.empty-state { text-align: center; padding: 80px 0; color: #bbb; }

.product-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 25px; }
.product-card { border: 1px solid #e8e8e3; transition: all 0.3s; }
.product-card:hover { border-color: #c9a84c; }
.product-img { position: relative; height: 220px; overflow: hidden; background: #f8f8f6; }
.product-img img { width: 100%; height: 100%; object-fit: contain; transition: transform 0.5s; padding: 10px; }
.product-card:hover .product-img img { transform: scale(1.05); }
.product-cat { position: absolute; top: 12px; left: 0; padding: 4px 14px; background: #c9a84c; color: #fff; font-size: 0.72rem; letter-spacing: 1px; }
.product-info { padding: 20px; }
.product-info h3 { color: #1a1a1a; font-size: 1rem; font-weight: 400; margin-bottom: 18px; }
.product-specs { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 15px; }
.spec-tag { padding: 2px 8px; border: 1px solid #e0e0db; color: #888; font-size: 0.68rem; }
.detail-btn { width: 100%; padding: 10px; background: transparent; border: 1px solid #c9a84c; color: #c9a84c; font-size: 0.8rem; cursor: pointer; letter-spacing: 2px; transition: all 0.3s; font-family: inherit; }
.detail-btn:hover { background: #c9a84c; color: #fff; }

/* Pagination */
.pagination { display: flex; justify-content: center; gap: 5px; margin-top: 40px; }
.page-btn { padding: 8px 16px; border: 1px solid #e0e0db; background: #fff; color: #666; cursor: pointer; font-size: 0.8rem; transition: all 0.2s; font-family: inherit; }
.page-btn:hover, .page-btn.active { border-color: #c9a84c; color: #c9a84c; }
.page-btn:disabled { opacity: 0.4; cursor: default; }

@media (max-width: 768px) {
  .main-layout { flex-direction: column; }
  .sidebar { width: 100%; position: static; margin-bottom: 20px; }
  .product-grid { grid-template-columns: 1fr; }
  .toolbar { flex-direction: column; align-items: stretch; }
  .search-box { width: 100%; }
  .search-input { width: 100%; }
}
</style>
