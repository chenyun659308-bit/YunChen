<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useI18n } from './i18n.js'

const route = useRoute()
const router = useRouter()
const menuOpen = ref(false)
const searchQuery = ref('')
const showDropdown = ref(false)
const { t, toggleLang, locale } = useI18n()

const navItems = [
  { path: '/', label: 'nav_home' },
  { path: '/about', label: 'nav_about' },
  { label: 'nav_products', dropdown: [
    { path: '/products', label: '全部产品' },
    { path: '/products?cat=冷暖净风器', label: '冷暖净风器' },
    { path: '/products?cat=电风扇', label: '电风扇' },
    { path: '/products?cat=暖风机', label: '暖风机' },
    { path: '/products?cat=小太阳', label: '小太阳' }
  ]},
  { path: '/culture', label: 'nav_culture' },
  { path: '/news', label: 'nav_news' },
  { path: '/downloads', label: 'nav_downloads' },
  { path: '/contact', label: 'nav_contact' }
]

function doSearch() {
  if (searchQuery.value.trim()) {
    router.push('/products?q=' + encodeURIComponent(searchQuery.value))
    searchQuery.value = ''
  }
}
function goDropdown(item) { router.push(item.path); showDropdown.value = false; menuOpen.value = false }
</script>

<template>
  <div class="app-wrapper">
    <div class="top-bar">
      <div class="container top-bar-inner">
        <div class="top-bar-left">
          <span class="top-bar-info">📞 {{ t('phone') }} &nbsp; 📧 {{ t('email') }} &nbsp; 📍 {{ t('address') }}</span>
        </div>
        <div class="top-bar-right">
          <span class="top-bar-text">{{ t('company') }} · {{ t('slogan') }}</span>
          <button class="lang-switch" @click="toggleLang">{{ locale === 'zh' ? 'EN' : '中文' }}</button>
        </div>
      </div>
    </div>

    <header class="navbar">
      <div class="container nav-inner">
        <router-link to="/" class="logo">
          <span class="logo-icon">{{ t('company') }}</span>
          <span class="logo-sub">JIUYOU ELECTRIC</span>
        </router-link>

        <nav class="nav-links" :class="{ open: menuOpen }">
          <template v-for="item in navItems" :key="item.label">
            <div v-if="item.dropdown" class="nav-dropdown" @mouseenter="showDropdown = true" @mouseleave="showDropdown = false">
              <router-link to="/products" class="nav-link" :class="{ active: route.path === '/products' }">{{ t(item.label) }} <span class="arrow">▾</span></router-link>
              <div class="dropdown-menu" v-show="showDropdown || menuOpen">
                <a v-for="sub in item.dropdown" :key="sub.path" class="dropdown-item" @click="goDropdown(sub)">{{ sub.label }}</a>
              </div>
            </div>
            <router-link v-else :to="item.path" class="nav-link" :class="{ active: route.path === item.path }" @click="menuOpen = false">{{ t(item.label) }}</router-link>
          </template>

          <div class="nav-search">
            <input v-model="searchQuery" @keyup.enter="doSearch" :placeholder="t('search_placeholder')" class="search-input">
            <button @click="doSearch" class="search-btn">{{ t('search_btn') }}</button>
          </div>
        </nav>

        <button class="menu-toggle" @click="menuOpen = !menuOpen"><span></span><span></span><span></span></button>
      </div>
    </header>

    <main class="main-content"><router-view /></main>

    <footer class="footer">
      <div class="container footer-grid">
        <div class="footer-brand"><h3>{{ t('company') }}</h3><p>{{ t('footer_about') }}</p><p class="footer-slogan">{{ t('footer_slogan') }}</p></div>
        <div class="footer-links"><h4>{{ t('footer_links') }}</h4><router-link to="/about">{{ t('nav_about') }}</router-link><router-link to="/culture">{{ t('nav_culture') }}</router-link><router-link to="/products">{{ t('nav_products') }}</router-link><router-link to="/news">{{ t('nav_news') }}</router-link></div>
        <div class="footer-links"><h4>{{ t('footer_service') }}</h4><router-link to="/downloads">{{ t('nav_downloads') }}</router-link><router-link to="/contact">{{ t('nav_contact') }}</router-link><a href="#">售后服务</a><a href="#">常见问题</a></div>
        <div class="footer-contact"><h4>{{ t('footer_contact') }}</h4><p>{{ t('address') }}</p><p>{{ t('footer_contact_title') }}：{{ t('phone') }}</p><p>📧 {{ t('email') }}</p><p>{{ t('company') }} · 始于2001</p></div>
      </div>
      <div class="footer-bottom"><div class="container"><p>{{ t('footer_copyright') }}</p></div></div>
    </footer>
  </div>
</template>

<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Noto Serif SC', 'Microsoft YaHei', -apple-system, sans-serif; background: #fff; color: #1a1a1a; -webkit-font-smoothing: antialiased; }
a { text-decoration: none; color: inherit; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.app-wrapper { min-height: 100vh; display: flex; flex-direction: column; }
.main-content { flex: 1; padding-top: 112px; }

.top-bar { background: #1a1a1a; position: fixed; top: 0; left: 0; right: 0; z-index: 1001; height: 38px; }
.top-bar-inner { display: flex; justify-content: space-between; align-items: center; height: 100%; }
.top-bar-left { display: flex; align-items: center; gap: 8px; }
.top-bar-right { display: flex; align-items: center; gap: 16px; }
.top-bar-text { color: rgba(255,255,255,0.45); font-size: 0.75rem; letter-spacing: 1px; }
.top-bar-info { color: #c9a84c; font-size: 0.78rem; letter-spacing: 0.5px; font-weight: 400; }
.lang-switch { background: none; border: 1px solid rgba(201,168,76,0.3); color: #c9a84c; font-size: 0.65rem; padding: 2px 10px; cursor: pointer; letter-spacing: 1px; transition: all 0.3s; font-family: inherit; }
.lang-switch:hover { background: rgba(201,168,76,0.1); }

.navbar { position: fixed; top: 38px; left: 0; right: 0; z-index: 1000; background: #fff; border-bottom: 1px solid #e8e8e3; height: 74px; display: flex; align-items: center; }
.nav-inner { display: flex; align-items: center; justify-content: space-between; width: 100%; height: 100%; }
.logo { display: flex; flex-direction: column; align-items: center; flex-shrink: 0; }
.logo-icon { font-size: 1.4rem; color: #1a1a1a; letter-spacing: 4px; font-weight: 600; }
.logo-sub { font-size: 0.5rem; color: #c9a84c; letter-spacing: 5px; margin-top: 2px; }
.nav-links { display: flex; align-items: center; height: 100%; gap: 0; }
.nav-link { display: inline-flex; align-items: center; padding: 0 22px; color: #666; font-size: 0.88rem; letter-spacing: 1px; white-space: nowrap; height: 100%; border-bottom: 2px solid transparent; transition: all 0.3s; }
.nav-link:hover, .nav-link.active { color: #1a1a1a; border-bottom-color: #c9a84c; }
.arrow { font-size: 0.6rem; margin-left: 2px; }
.nav-dropdown { display: inline-flex; align-items: center; height: 100%; position: relative; }
.dropdown-menu { position: absolute; top: 100%; left: 50%; transform: translateX(-50%); background: #fff; border: 1px solid #e8e8e3; min-width: 150px; z-index: 100; padding: 8px 0; }
.dropdown-item { display: block; padding: 10px 24px; color: #666; font-size: 0.85rem; cursor: pointer; text-align: center; transition: all 0.2s; letter-spacing: 1px; }
.dropdown-item:hover { color: #1a1a1a; background: #f8f8f6; }
.nav-search { display: inline-flex; align-items: center; margin-left: 8px; border: 1px solid #e0e0db; height: 34px; }
.search-input { width: 160px; padding: 0 10px; border: none; color: #1a1a1a; font-size: 0.8rem; outline: none; font-family: inherit; background: transparent; height: 100%; }
.search-input::placeholder { color: #bbb; font-size: 0.72rem; }
.search-btn { padding: 0 12px; background: none; border: none; border-left: 1px solid #e0e0db; color: #888; cursor: pointer; font-size: 0.75rem; letter-spacing: 1px; height: 100%; display: flex; align-items: center; transition: all 0.3s; }
.search-btn:hover { color: #c9a84c; background: #f8f8f6; }
.menu-toggle { display: none; flex-direction: column; gap: 5px; background: none; border: none; cursor: pointer; padding: 5px; }
.menu-toggle span { width: 22px; height: 1.5px; background: #1a1a1a; transition: all 0.3s; }

.footer { background: #1a1a1a; border-top: 2px solid #c9a84c; padding: 60px 0 0; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 40px; padding-bottom: 40px; }
.footer-brand h3 { font-size: 1.3rem; color: #c9a84c; margin-bottom: 15px; letter-spacing: 2px; }
.footer-brand p { color: rgba(255,255,255,0.45); font-size: 0.85rem; line-height: 1.8; }
.footer-slogan { color: rgba(201,168,76,0.5); font-size: 0.7rem; letter-spacing: 3px; margin-top: 15px; }
.footer-links h4, .footer-contact h4 { color: #fff; font-size: 0.9rem; margin-bottom: 20px; font-weight: 400; letter-spacing: 2px; }
.footer-links a { display: block; color: rgba(255,255,255,0.45); font-size: 0.85rem; margin-bottom: 12px; transition: color 0.3s; }
.footer-links a:hover { color: #c9a84c; }
.footer-contact p { color: rgba(255,255,255,0.45); font-size: 0.85rem; margin-bottom: 8px; line-height: 1.6; }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.06); padding: 20px 0; text-align: center; }
.footer-bottom p { color: rgba(255,255,255,0.2); font-size: 0.75rem; }

@media (max-width: 768px) {
  .nav-links { display: none; flex-direction: column; position: absolute; top: 74px; left: 0; right: 0; background: #fff; border-bottom: 1px solid #e8e8e3; padding: 10px 20px; height: auto; }
  .nav-links.open { display: flex; }
  .nav-link { padding: 12px 0; border-bottom: 1px solid #f0f0eb; width: 100%; height: auto; }
  .nav-dropdown { height: auto; display: block; width: 100%; }
  .nav-search { margin-left: 0; margin-top: 8px; width: 100%; }
  .search-input { width: 100%; }
  .menu-toggle { display: flex; }
  .top-bar-text { display: none; }
  .footer-grid { grid-template-columns: 1fr; gap: 30px; }
  .dropdown-menu { position: static; transform: none; border: none; border-left: 2px solid #c9a84c; margin-left: 18px; padding: 5px 0; }
}
</style>

