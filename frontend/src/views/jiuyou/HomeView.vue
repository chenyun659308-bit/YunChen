<script setup>
import { computed } from 'vue'
import { useI18n } from '../../i18n.js'
import HomeZh from './Home.vue'
import HomeEn from './HomeEn.vue'

const { locale } = useI18n()
const activeHome = computed(() => locale.value === 'en' ? HomeEn : HomeZh)
</script>

<template>
  <component :is="activeHome" />
</template>
