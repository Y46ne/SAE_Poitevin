<script setup>
import { computed, ref } from 'vue'

const homeElement = document.getElementById('home-data')
const home = homeElement ? JSON.parse(homeElement.textContent) : { name: '', blocks: [] }
const selectedBlock = ref(null)

const blocks = computed(() => home.blocks || [])

function selectBlock(block) {
  selectedBlock.value = selectedBlock.value?.id === block.id ? null : block
}
</script>

<template>
  <main class="home">
    <header class="hero">
      <p class="eyebrow">Stade Poitevin Tennis</p>
      <h1>{{ home.name }}</h1>
      <p>Le tennis au coeur de Poitiers.</p>
    </header>

    <section v-if="blocks.length" class="blocks" aria-label="À la une">
      <article v-for="block in blocks" :key="block.id" class="block">
        <button type="button" class="block-button" @click="selectBlock(block)">
          <span class="block-type">{{ block.type }}</span>
          <strong>{{ block.title || 'À la une' }}</strong>
          <span v-if="block.subtitle">{{ block.subtitle }}</span>
        </button>
        <pre v-if="selectedBlock?.id === block.id">{{ block.settings }}</pre>
      </article>
    </section>
    <p v-else class="empty-state">Les actualités du club arrivent bientôt.</p>
  </main>
</template>
