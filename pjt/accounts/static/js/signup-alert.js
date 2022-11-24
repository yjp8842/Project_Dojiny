window.onload = function () {
  const loginAlert = document.querySelector('#login-alert')
  
  if (document.querySelector('.login-alert-modal p') !== null) {
    const login = document.querySelector('.login-alert-modal p')
    if (login.innerHTML === '이미 존재하는 username 입니다.') {
      loginAlert.style.display = "block"
      setTimeout(() => {
        loginAlert.style.display = 'none'
      }, 1500)
    } 
    if (login.innerHTML === '올바른 email을 입력해 주세요.') {
      loginAlert.style.display = 'block'
      setTimeout(() => {
        loginAlert.style.display = 'none'
      }, 1500)
    }
  }
}