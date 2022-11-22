const searchBtn = document.querySelector('#search-btn')
const modalScreen = document.querySelector('#modal')

searchBtn.addEventListener('click', (e) => {
  modalScreen.style.display = "block"
})

modalScreen.addEventListener("click", e => {
  const evTarget = e.target
  if (evTarget.classList.contains("modal-box")) {
      modalScreen.style.display = "none"
  }
});