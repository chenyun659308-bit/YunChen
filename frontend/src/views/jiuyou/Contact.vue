<script setup>
import { computed, ref } from 'vue'
import { useI18n } from '../../i18n.js'

const { locale } = useI18n()

const zhText = {
  crumb: '首页 / 在线留言',
  heroTitle: '在线留言',
  heroDesc: '您的声音，我们用心倾听',
  formTitle: '留言咨询',
  formDesc: '欢迎留下您的需求与建议，久友客服将在24小时内与您联系。',
  name: '姓名 *', namePh: '请输入您的姓名',
  phone: '手机号 *', phonePh: '请输入您的手机号码',
  email: '邮箱', emailPh: '请输入您的邮箱地址',
  subject: '主题 *', subjectPh: '请输入留言主题',
  content: '留言内容 *', contentPh: '请详细描述您的需求或建议...',
  submit: '提交留言',
  sidebarTitle: '联系方式',
  addrLabel: '公司地址',
  address: '浙江省慈溪市新浦镇上舍村',
  hotlineLabel: '服务热线',
  emailLabel: '电子邮箱',
  hoursLabel: '工作时间',
  hours1: '周一至周五 8:30-18:00',
  hours2: '周六 9:00-17:00',
  success: '留言提交成功！我们将尽快与您联系。',
  networkError: '网络错误，请检查连接后重试'
}

const enText = {
  crumb: 'Home / Contact Us',
  heroTitle: 'Contact Us',
  heroDesc: 'Your voice matters to us',
  formTitle: 'Send a Message',
  formDesc: 'Leave your needs and suggestions, our team will contact you within 24 hours.',
  name: 'Name *', namePh: 'Please enter your name',
  phone: 'Phone *', phonePh: 'Please enter your phone number',
  email: 'Email', emailPh: 'Please enter your email address',
  subject: 'Subject *', subjectPh: 'Please enter a subject',
  content: 'Message *', contentPh: 'Please describe your needs or suggestions...',
  submit: 'Submit',
  sidebarTitle: 'Contact Information',
  addrLabel: 'Company Address',
  address: 'Shangshe Village, Xinpu Town, Cixi, Zhejiang',
  hotlineLabel: 'Service Hotline',
  emailLabel: 'Email',
  hoursLabel: 'Business Hours',
  hours1: 'Monday-Friday 8:30-18:00',
  hours2: 'Saturday 9:00-17:00',
  success: 'Your message has been submitted. We will contact you soon.',
  networkError: 'Network error. Please check your connection and try again.'
}

const copy = computed(() => locale.value === 'en' ? enText : zhText)

const form = ref({ name: "", phone: "", email: "", title: "", content: "" })
async function submit() {
  const en = locale.value === 'en'
  try {
    const r = await fetch("/api/contact/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form.value)
    })
    if (r.ok) {
      alert(en ? enText.success : zhText.success)
      form.value = { name: "", phone: "", email: "", title: "", content: "" }
    } else {
      const d = await r.json()
      const prefix = en ? 'Submission failed: ' : '提交失败：'
      const fallback = en ? 'Please try again later.' : '请稍后重试'
      alert(prefix + (d.detail || fallback))
    }
  } catch {
    alert(en ? enText.networkError : zhText.networkError)
  }
}
</script>
<template>
  <div class="contact-page">
    <section class="page-hero"><div class="hero-bg"><img src="https://images.unsplash.com/photo-1423666639041-f56000c27a9a?w=1920&h=500&fit=crop" alt=""></div><div class="hero-overlay"></div><div class="hero-content" style="position:relative;z-index:1;"><span class="breadcrumb">{{ copy.crumb }}</span><h1>{{ copy.heroTitle }}</h1><p>{{ copy.heroDesc }}</p></div></section>
    <section class="section"><div class="container">
      <div class="contact-grid">
        <div class="contact-form-wrap"><h2>{{ copy.formTitle }}</h2><p class="form-desc">{{ copy.formDesc }}</p>
          <form @submit.prevent="submit" class="form">
            <div class="form-row"><div class="form-group"><label>{{ copy.name }}</label><input v-model="form.name" :placeholder="copy.namePh" required></div><div class="form-group"><label>{{ copy.phone }}</label><input v-model="form.phone" :placeholder="copy.phonePh" required></div></div>
            <div class="form-group"><label>{{ copy.email }}</label><input v-model="form.email" type="email" :placeholder="copy.emailPh"></div>
            <div class="form-group"><label>{{ copy.subject }}</label><input v-model="form.title" :placeholder="copy.subjectPh" required></div>
            <div class="form-group"><label>{{ copy.content }}</label><textarea v-model="form.content" rows="6" :placeholder="copy.contentPh" required></textarea></div>
            <button type="submit" class="submit-btn">{{ copy.submit }}</button>
          </form>
        </div>
        <div class="contact-sidebar">
          <h2>{{ copy.sidebarTitle }}</h2>
          <div class="info-card"><div class="info-item"><span class="info-icon">📍</span><div><h3>{{ copy.addrLabel }}</h3><p>{{ copy.address }}</p></div></div></div>
          <div class="info-card"><div class="info-item"><span class="info-icon">📞</span><div><h3>{{ copy.hotlineLabel }}</h3><p>400-888-1998</p></div></div></div>
          <div class="info-card"><div class="info-item"><span class="info-icon">✉️</span><div><h3>{{ copy.emailLabel }}</h3><p>service@jiuyou.com</p></div></div></div>
          <div class="info-card"><div class="info-item"><span class="info-icon">🕐</span><div><h3>{{ copy.hoursLabel }}</h3><p>{{ copy.hours1 }}<br>{{ copy.hours2 }}</p></div></div></div>
        </div>
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






.contact-page { background: #fff; }







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

.page-hero { position: relative; padding: 0; text-align: center; overflow: hidden; height: 40vh; min-height: 320px; display: flex; align-items: center; justify-content: center; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.3)); z-index: 1; }
.hero-content { position: relative; z-index: 2; }
.breadcrumb { display: block; color: rgba(201,168,76,0.6); font-size: 0.78rem; letter-spacing: 2px; margin-bottom: 15px; }
.page-hero h1 { font-size: 3rem; font-weight: 300; color: #fff; margin-bottom: 12px; letter-spacing: 5px; }
.page-hero p { color: rgba(255,255,255,0.5); font-size: 1rem; }
</style>
