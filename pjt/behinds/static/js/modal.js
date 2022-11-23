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

// 감독 권한 여부에 따른 alert 띄우기
const createPage = document.querySelector('#create-page')
const createAlert = document.querySelector('#create-alert')
const alertBtn = document.querySelector('#alert-btn')

createPage.addEventListener('click', (e) => {
  // console.log(e.target.dataset.userAuth)
  const values = e.target.dataset.userAuth
  if (values === "False") {
    e.preventDefault()
    createAlert.style.display = "block"
  }
})

alertBtn.addEventListener("click", () => {
  createAlert.style.display = "none"
});

createAlert.addEventListener("click", e => {
  const evTarget = e.target
  if (evTarget.classList.contains("create-alert")) {
    createAlert.style.display = "none"
  }
});