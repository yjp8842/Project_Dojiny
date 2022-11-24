window.onload = function () {
  const createAlert = document.querySelector('#create-alert')

  if (document.querySelector('.create-alert-modal p') !== null) {
    const create = document.querySelector('.create-alert-modal p')
    if(create.innerHTML === '제목은 최대 50자까지 작성이 가능합니다.') {
      createAlert.style.display = 'block'
      setTimeout(() => {
        createAlert.style.display = 'none'
      }, 1500)
    }
    if(create.innerHTML === '본문을 입력해 주세요') {
      createAlert.style.display = 'block'
      setTimeout(() => {
        createAlert.style.display = 'none'
      }, 1500)
    }
    if(create.innerHTML === '제목을 입력해 주세요') {
      createAlert.style.display = 'block'
      setTimeout(() => {
        createAlert.style.display = 'none'
      }, 1500)
    }
  }
}