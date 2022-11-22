const showIcon = document.querySelector('#show-menu')
const hideIcon = document.querySelector('#hide-menu')
const backIcon = document.querySelector('#back-page')

showIcon.addEventListener('click', (e) => {
  backIcon.setAttribute('style', 'display: none;')
})

hideIcon.addEventListener('click', (e) => {
  backIcon.setAttribute('style', 'display: flex;')
})