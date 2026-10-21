import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
// Pas de serveur de dev Vite : le bundle est servi par Django depuis /static/frontend/.
export default defineConfig({
  plugins: [vue()],
  base: '/static/frontend/',
  publicDir: false,
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  build: {
    outDir: '../backend/static/frontend',
    emptyOutDir: true,
    rollupOptions: {
      input: fileURLToPath(new URL('./src/main.js', import.meta.url)),
      output: {
        entryFileNames: 'app.js',
        assetFileNames: 'app.[ext]',
      },
    },
  },
})
