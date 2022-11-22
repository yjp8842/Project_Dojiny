const openMenu = document.querySelector('#show-menu')
const hideMenuIcon = document.querySelector('#hide-menu')
const sideMenu = document.querySelector('#nav-menu')

openMenu.addEventListener('click', function(event) {
   sideMenu.classList.add('active')
})

hideMenuIcon.addEventListener('click', function(event) {
  sideMenu.classList.remove('active')
})