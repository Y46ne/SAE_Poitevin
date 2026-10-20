import { mount } from '@vue/test-utils'
import { beforeEach, describe, expect, it } from 'vitest'

import App from '../App.vue'

describe('App', () => {
  beforeEach(() => {
    document.body.innerHTML =
      '<div id="home-data">{"name":"Accueil","blocks":[{"id":1,"type":"info","title":"Actualités","subtitle":"","settings":{}}]}</div>'
  })

  it('renders the homepage data supplied by Django', () => {
    const wrapper = mount(App)

    expect(wrapper.text()).toContain('Accueil')
    expect(wrapper.text()).toContain('Actualités')
  })
})
