import { createApp } from 'vue'

/**
 * Monte un composant Vue sur chaque élément `[data-vue]` de la page.
 *
 * Exemple dans un template Django :
 *   <div data-vue="OpenTimeline" data-props="timeline-data">contenu sans JS</div>
 *   {{ timeline|json_script:"timeline-data" }}
 *
 * `data-vue` donne le nom du composant, `data-props` l'id du `json_script`
 * qui contient un objet de props. Le contenu de l'élément est remplacé au montage.
 *
 * @param {Record<string, import('vue').Component>} components composants disponibles, par nom
 * @param {ParentNode} [root] zone où chercher les îlots
 * @returns {import('vue').App[]} applications montées
 */
export function mountIslands(components, root = document) {
  const apps = []

  for (const element of root.querySelectorAll('[data-vue]')) {
    const name = element.dataset.vue
    const component = components[name]
    if (!component) {
      console.warn(`Îlot Vue inconnu : ${name}`)
      continue
    }

    const app = createApp(component, readProps(element.dataset.props))
    app.mount(element)
    apps.push(app)
  }

  return apps
}

/**
 * @param {string | undefined} id id de l'élément `json_script`
 * @returns {Record<string, unknown>}
 */
function readProps(id) {
  const dataElement = id ? document.getElementById(id) : null
  return dataElement ? JSON.parse(dataElement.textContent) : {}
}
