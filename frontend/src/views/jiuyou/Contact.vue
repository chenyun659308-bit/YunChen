<script setup>
import { ref } from 'vue'
const form = ref({ name: "", phone: "", email: "", title: "", content: "" })
async function submit() {
  try {
    const r = await fetch("/api/contact/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form.value)
    })
    if (r.ok) {
      alert("留言提交成功！我们将尽快与您联系。")
      form.value = { name: "", phone: "", email: "", title: "", content: "" }
    } else {
      const d = await r.json()
      alert("提交失败：" + (d.detail || "请稍后重试"))
    }
  } catch { alert("网络错误，请检查连接后重试") }
}
</script>
<template>
  <div class="contact-page">
    <section class="page-hero"><div class="hero-bg"></div><div class="hero-overlay"></div><div class="hero-content"><span class="breadcrumb">首页 / {{ t('contact_hero') }}</span><h1>{{ t('contact_hero') }}</h1><p>您的声音，我们用心倾听</p></div></section>
    <section class="section"><div class="container">
      <div class="contact-grid">
        <div class="contact-form-wrap"><h2>{{ t('contact_form_title') }}</h2><p class="form-desc">{{ t('contact_form_desc') }}</p>
          <form @submit.prevent="submit" class="form">
            <div class="form-row"><div class="form-group"><label>姓名 *</label><input v-model="form.name" placeholder="请输入您的姓名" required></div><div class="form-group"><label>手机号 *</label><input v-model="form.phone" placeholder="请输入您的手机号码" required></div></div>
            <div class="form-group"><label>邮箱</label><input v-model="form.email" type="email" placeholder="请输入您的邮箱地址"></div>
            <div class="form-group"><label>主题 *</label><input v-model="form.title" placeholder="请输入留言主题" required></div>
            <div class="form-group"><label>留言内容 *</label><textarea v-model="form.content" rows="6" placeholder="请详细描述您的需求或建议..." required></textarea></div>
            <button type="submit" class="submit-btn">{{ t('contact_submit') }}</button>
          </form>
        </div>
        <div class="contact-sidebar">
          <h2>联系方式</h2>
          <div class="info-card"><div class="info-item"><span class="info-icon">📍</span><div><h3>公司地址</h3><p>广东省佛山市顺德区北滘镇久友大道1号</p></div></div></div>
          <div class="info-card"><div class="info-item"><span class="info-icon">📞</span><div><h3>服务热线</h3><p>400-888-1998</p></div></div></div>
          <div class="info-card"><div class="info-item"><span class="info-icon">✉️</span><div><h3>电子邮箱</h3><p>service@jiuyou.com</p></div></div></div>
          <div class="info-card"><div class="info-item"><span class="info-icon">🕐</span><div><h3>工作时间</h3><p>周一至周五 8:30-18:00<br>周六 9:00-17:00</p></div></div></div>
        </div>
      </div>
    </div></section>
  </div>
</template>

<style scoped>
.contact-page { background: #fff; }
.page-hero { position: relative; height: 40vh; min-height: 300px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.hero-bg { position: absolute; inset: 0; background: url(https://images.unsplash.com/photo-1423666639041-f56000c27a9a?w=1920&h=600&fit=crop) center/cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(0,0,0,0.8),rgba(0,0,0,0.4)); z-index: 1; }
.hero-content { position: relative; z-index: 2; text-align: center; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 15px; }
.hero-content h1 { font-size: 2.8rem; color: #fff; font-weight: 300; margin-bottom: 12px; letter-spacing: 4px; }
.hero-content p { color: rgba(255,255,255,0.5); }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.section { padding: 80px 0; }
.contact-grid { display: grid; grid-template-columns: 1.5fr 1fr; gap: 50px; }
.contact-form-wrap h2, .contact-sidebar h2 { font-size: 1.8rem; font-weight: 300; color: #1a1a1a; margin-bottom: 15px; letter-spacing: 2px; }
.form-desc { color: #888; margin-bottom: 30px; font-size: 0.9rem; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.form-group { margin-bottom: 20px; }
.form-group label { display: block; color: #555; font-size: 0.82rem; margin-bottom: 8px; }
.form-group input, .form-group textarea { width: 100%; padding: 12px 15px; border: 1px solid #e0e0db; color: #1a1a1a; font-size: 0.85rem; outline: none; transition: border 0.3s; font-family: inherit; background: #fff; }
.form-group input:focus, .form-group textarea:focus { border-color: #c9a84c; }
.form-group textarea { resize: vertical; }
.submit-btn { padding: 14px 50px; background: #c9a84c; color: #fff; border: none; font-size: 0.85rem; cursor: pointer; letter-spacing: 2px; transition: all 0.3s; font-family: inherit; }
.submit-btn:hover { background: #b8942e; }
.contact-sidebar { padding: 0; }
.info-card { padding: 20px; border: 1px solid #e8e8e3; margin-bottom: 15px; }
.info-item { display: flex; gap: 12px; }
.info-icon { font-size: 1.3rem; flex-shrink: 0; margin-top: 2px; }
.info-item h3 { color: #1a1a1a; font-size: 0.85rem; font-weight: 400; margin-bottom: 4px; }
.info-item p { color: #888; font-size: 0.82rem; line-height: 1.5; }
@media (max-width:768px) { .contact-grid { grid-template-columns: 1fr; } .form-row { grid-template-columns: 1fr; } }
</style>
