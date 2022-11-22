const recent = document.querySelector('#recent')
const popular = document.querySelector('#popular')
const popularForm = document.querySelector("#popular-form")
const recentForm = document.querySelector("#recent-form")

recent.addEventListener('click', (e) => {
  const select = e.target.innerText
  if (select === '최신순') {
    recentForm.classList.remove('not-visible')
    popularForm.classList.add('not-visible')
    popular.classList.add('deactivate')
    recent.classList.remove('deactivate')
  }
})

popular.addEventListener('click', (e) => {
  const select = e.target.innerText
  if (select === '인기순') {
    recentForm.classList.add('not-visible')
    popularForm.classList.remove('not-visible')
    popular.classList.remove('deactivate')
    recent.classList.add('deactivate')
  }
})