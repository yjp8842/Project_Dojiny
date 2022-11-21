const fiveBefore = document.querySelector('.star5before')
const fourBefore = document.querySelector('.star4before')
const threeBefore = document.querySelector('.star3before')
const twoBefore = document.querySelector('.star2before')
const oneBefore = document.querySelector('.star1before')


const fiveNext = document.querySelector('.star5next')
const fourNext = document.querySelector('.star4next')
const threeNext = document.querySelector('.star3next')
const twoNext = document.querySelector('.star2next')
const oneNext = document.querySelector('.star1next')


const beforeArr = [fiveBefore, fourBefore, threeBefore, twoBefore, oneBefore]
const nextArr = [fiveNext, fourNext, threeNext, twoNext, oneNext]

var fiveList = null
var fourList = null
var threeList = null
var twoList = null
var oneList = null

nextArr.forEach(next => {
  if (next != null) {
    next.addEventListener('click', event => {
      console.log(event.target.dataset.movieStars)
  })
  }})

  // 비동기로 데이터 받아오기
  