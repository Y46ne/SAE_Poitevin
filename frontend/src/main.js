import './assets/main.css'

import { mountIslands } from './islands.js'

// Composants utilisables en îlots, par nom de `data-vue`.
// Ex. : import OpenTimeline from './components/open86/OpenTimeline.vue'
const components = {}

mountIslands(components)
