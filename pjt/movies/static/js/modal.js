const searchBtn = document.querySelector('#search-btn')
const modalScreen = document.querySelector('#modal')
const movieList = document.querySelector('.box')

searchBtn.addEventListener('click', (e) => {
  movieList.classList.remove('display')
  movieList.style.display = 'none'
  modalScreen.style.display = "block"
})

modalScreen.addEventListener("click", e => {
  const evTarget = e.target
  if (evTarget.classList.contains("modal-box")) {
      modalScreen.style.display = "none"
  }
});