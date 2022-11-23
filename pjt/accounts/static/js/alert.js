const submitBtn = document.querySelector('.submit')
const loginAlert = document.querySelector('#login-alert')

// searchBtn.addEventListener('click', (e) => {
//   modalScreen.style.display = "block"
// })

// modalScreen.addEventListener("click", e => {
//   const evTarget = e.target
//   if (evTarget.classList.contains("modal-box")) {
//     modalScreen.style.display = "none"
//   }
// });

const login = document.querySelector('.login-alert-modal')

submitBtn.addEventListener('click', (e) => {
  e.preventDefault()
  if (login.innerHTML === '올바른 유저네임 또는 올바른 비밀번호를 입력하세요.') {
    loginAlert.style.display = "block"
  } 
  if (login.innerHTML === '올바른 비밀번호를 입력하세요.') {
    loginAlert.style.display = 'block'
  }
})