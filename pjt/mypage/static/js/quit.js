const quitAccount = document.querySelector('#quit-account')
const quitAlert = document.querySelector('#quit-alert')
const submitBtn = document.querySelector('#quit-btn')
const cancelBtn = document.querySelector('#cancel')

quitAccount.addEventListener('click', (e) => {
  e.preventDefault()
  quitAlert.style.display = "block"
})

submitBtn.addEventListener('click', (e) => {
  submitBtn.setAttribute('type', 'submit')
})

quitAlert.addEventListener('click', (e) => {
  const eTarget = e.target
  if (eTarget.classList.contains("quit-alert")) {
    quitAlert.style.display = "none"
  }
})

cancelBtn.addEventListener('click', (e) => {
  quitAlert.style.display = "none"
})