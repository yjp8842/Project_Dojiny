const searchBtn = document.querySelector('#search-btn')
const modalScreen = document.querySelector('#modal')
const searchInput2 = document.querySelector('#search-input')
const resultBox2 = document.querySelector('#result-Box')
    
searchBtn.addEventListener('click', (e) => {
  searchInput2.value = ''
  resultBox2.innerHTML = ``
  modalScreen.style.display = "block"
})

modalScreen.addEventListener("click", (e) => {
  const evTarget = e.target
  if (evTarget.classList.contains("modal-box")) {
    modalScreen.style.display = "none"
  }
})