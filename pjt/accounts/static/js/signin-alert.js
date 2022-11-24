window.onload = function () {
  const loginAlert = document.querySelector('#login-alert')
  
  if (document.querySelector('.login-alert-modal p') !== null) {
    const login = document.querySelector('.login-alert-modal p')
    if (login.innerHTML === '올바른 유저네임 또는 올바른 비밀번호를 입력하세요.') {
      loginAlert.style.display = "block"
      setTimeout(() => {
        loginAlert.style.display = 'none'
      }, 1500)
    } 
    if (login.innerHTML === '올바른 비밀번호를 입력하세요.') {
      loginAlert.style.display = 'block'
      setTimeout(() => {
        loginAlert.style.display = 'none'
      }, 1500)
    }
  }
}