const searchInput = document.querySelector('#search-input')
const searchBtn = document.querySelector('#search')

const formBox = document.querySelector('#form-box')
const formList = document.querySelector('#form-list')
const director = document.querySelector('#director')

searchBtn.addEventListener('click', function (event) {
  const inputData = searchInput.value
  console.log(director.innerText)
  console.log(inputData)
})