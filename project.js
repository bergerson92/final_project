/* global bootstrap: false */
/* removed the script in layout.html and put it in the html directly at the top wihtin the <script></script>*/
(() => {
    'use strict'
    const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(tooltipTriggerEl => {
      new bootstrap.Tooltip(tooltipTriggerEl)
    })
  })()
