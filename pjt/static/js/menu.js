function moviesPage() {
  window.location.href = 'http://127.0.0.1:8000/movies/'
}

function behindPage() {
  window.location.href = 'http://127.0.0.1:8000/behinds/'
}


const userid = document.querySelector('#userid').innerText

function myPage() {
  window.location.href = `http://127.0.0.1:8000/mypage/${userid}/profile/`
}