(function (factory) {
  typeof define === 'function' && define.amd ? define(factory) :
    factory()
})((function () {
  'use strict'

  let themeStorageKey = 'pycorisTheme'
  let defaultTheme = 'light'
  let selectedTheme
  let params = new Proxy(new URLSearchParams(window.location.search), {
    get: function get (searchParams, prop) {
      return searchParams.get(prop)
    },
  })

  if (!!params.theme) {
    localStorage.setItem(themeStorageKey, params.theme)
    selectedTheme = params.theme
  } else {
    let storedTheme = localStorage.getItem(themeStorageKey)
    selectedTheme = storedTheme ? storedTheme : defaultTheme
  }

  function applyTheme(theme) {
    const darkThemeElements = document.querySelectorAll('.dark-theme')
    const darkThemeHideElements = document.querySelectorAll('.dark-theme-hide')
    const lightThemeHideElements = document.querySelectorAll('.light-theme-hide')

    if (theme === 'dark') {
      document.body.setAttribute('data-bs-theme', theme)
      darkThemeElements.forEach(el => el.classList.add('bg-dark'))
      darkThemeHideElements.forEach(el => el.classList.add('d-none'))
      lightThemeHideElements.forEach(el => el.classList.remove('d-none'))
    } else {
      document.body.removeAttribute('data-bs-theme')
      darkThemeElements.forEach(el => el.classList.remove('bg-dark'))
      darkThemeHideElements.forEach(el => el.classList.remove('d-none'))
      lightThemeHideElements.forEach(el => el.classList.add('d-none'))
    }
  }

  applyTheme(selectedTheme)
}))
