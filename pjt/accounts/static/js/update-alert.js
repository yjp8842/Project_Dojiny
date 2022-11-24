window.onload = function () {
  const updateAlert = document.querySelector('#update-alert')
  
  if (document.querySelector('.update-alert-modal p') !== null) {
    const update = document.querySelector('.update-alert-modal p')
    if (update.innerHTML === '이미 존재하는 username 입니다.') {
      updateAlert.style.display = "block"
      setTimeout(() => {
        updateAlert.style.display = 'none'
      }, 1500)
    } 
    if (update.innerHTML === '올바른 형식의 이메일을 입력하세요') {
      updateAlert.style.display = 'block'
      setTimeout(() => {
        updateAlert.style.display = 'none'
      }, 1500)
    }
    if (update.innerHTML === '8자 이상의 연속되지 않은 비밀번호를 입력하세요') {
      updateAlert.style.display = 'block'
      setTimeout(() => {
        updateAlert.style.display = 'none'
      }, 1500)
    }
  }
}