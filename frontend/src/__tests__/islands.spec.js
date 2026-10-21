import { afterEach, describe, expect, it, vi } from 'vitest'
import { defineComponent, h } from 'vue'

import { mountIslands } from '../islands.js'

const Greeting = defineComponent({
  props: { name: { type: String, default: 'inconnu' } },
  setup(props) {
    return () => h('p', `Bonjour ${props.name}`)
  },
})

describe('mountIslands', () => {
  let apps = []

  afterEach(() => {
    apps.forEach((app) => app.unmount())
    apps = []
    document.body.innerHTML = ''
    vi.restoreAllMocks()
  })

  it('mounts the component with props read from json_script', () => {
    document.body.innerHTML = `
      <div data-vue="Greeting" data-props="greeting-data">Version sans JS</div>
      <script id="greeting-data" type="application/json">{"name": "Poitiers"}</script>
    `

    apps = mountIslands({ Greeting })

    expect(apps).toHaveLength(1)
    expect(document.querySelector('[data-vue]').textContent).toBe('Bonjour Poitiers')
  })

  it('uses default props without data-props', () => {
    document.body.innerHTML = '<div data-vue="Greeting"></div>'

    apps = mountIslands({ Greeting })

    expect(document.querySelector('[data-vue]').textContent).toBe('Bonjour inconnu')
  })

  it('does nothing on a page without islands', () => {
    document.body.innerHTML = '<main><p>Page Django</p></main>'

    apps = mountIslands({ Greeting })

    expect(apps).toHaveLength(0)
    expect(document.body.textContent).toContain('Page Django')
  })

  it('skips unknown islands and keeps their HTML', () => {
    const warn = vi.spyOn(console, 'warn').mockImplementation(() => {})
    document.body.innerHTML = '<div data-vue="Missing">Version sans JS</div>'

    apps = mountIslands({ Greeting })

    expect(apps).toHaveLength(0)
    expect(warn).toHaveBeenCalledWith('Îlot Vue inconnu : Missing')
    expect(document.body.textContent).toContain('Version sans JS')
  })
})
