// 별 마우스 오버로 선택
const one = document.querySelector('#first')
const two = document.querySelector('#second')
const three = document.querySelector('#third')
const four = document.querySelector('#fourth')
const five = document.querySelector('#fifth')

const arr = [one, two, three, four, five]

const form = document.querySelector('#star-check-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

var countChecked = null

// 윈도우 시작하자마자 유저 평점 매기기
window.addEventListener("load", (event) => {
  const uservote = document.querySelector("#uservote").innerText
  handleStarSelect(`${uservote}`)
})

const handleStarSelect = (size) => {
  const children = form.children
  for (let i=0; i < children.length; i++ ) {
    if (i <= size) {
      children[i].classList.add('checked')
      countChecked = i
    }
    else{
      children[i].classList.remove('checked')
    }
  }
}

const handleStar = (selection) => {
  switch(selection) {
    case 'first' : {
      handleStarSelect(1)
      break
    }
    case 'second' : {
      handleStarSelect(2)
      break
    } 
    case 'third' : {
      handleStarSelect(3)
      break
    }
    case 'fourth' : {
      handleStarSelect(4)
      break
    }
    case 'fifth' : {
      handleStarSelect(5)
      break
    }
  }
}

function star(event) {
  handleStar(event.target.id)
}
function initstar() {
  const uservote = document.querySelector("#uservote").innerText
  handleStarSelect(`${uservote}`)
}

// 별 개수 동적으로 보이게 함
arr.forEach(item => 
  item.addEventListener('mouseover', star)
)
form.addEventListener('mouseout', initstar)

// 병가한 별의 개수를 바탕으로 평점 매기기

// 선택시 동작


form.addEventListener('submit', (event) => {
  event.preventDefault()

  const movieId = event.target.dataset.movieId
  const userId = event.target.dataset.userId
  var vote = countChecked

  handleStarSelect(vote)

  // 기존 이벤트 지우기
  arr.forEach(item => 
    item.removeEventListener('mouseover', star)
  )
  // 만약 다시 누르는 경우라면 투표 초기화
  form.removeEventListener('mouseout', initstar)

  if (Number(vote) === Number(document.querySelector("#uservote").innerText)){
    vote = 0
  }

  // 전달할 데이터 저장
  var content_data = {
    'movieId': movieId,
    'userId': userId,
    'vote': vote,
    'csrftoken': csrftoken,
  }

  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/movies/${movieId}/detail/${userId}/uservote`,
    headers: {'X-CSRFToken': csrftoken},
    data: JSON.stringify(content_data),
  })
    .then(response => {
      console.log(response)
      // 이벤트 다시 추가
      document.querySelector("#uservote").innerText = vote
      arr.forEach(item => 
        item.addEventListener('mouseover', star)
      )
      form.addEventListener('mouseout', initstar)


      })
      .catch(err => {
        console.log(err)
      })
})