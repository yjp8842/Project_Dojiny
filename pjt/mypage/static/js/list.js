
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
const star5form = document.querySelector('#star5-form')
const star4form = document.querySelector('#star4-form')
const star3form = document.querySelector('#star3-form')
const star2form = document.querySelector('#star2-form')
const star1form = document.querySelector('#star1-form')

var fiveList = 0
var fourList = 0
var threeList = 0
var twoList = 0
var oneList = 0

formArr = [star5form, star4form, star3form, star2form, star1form]

formArr.forEach(form => {
  if (form != null) {
    form.addEventListener('submit', event => {
      event.preventDefault()
      const userId = event.target.dataset.userId
      var stars = event.target.dataset.stars
      var starsList = event.target.dataset.starsList
      var starList = null
      if (event.submitter.value === 'next'){
        if (starsList === 'fiveList'){
          fiveList += 1
          starList = fiveList
        }
        if (starsList === 'fourList'){
          fourList += 1
          starList = fourList
        }
        if (starsList === 'threeList'){
          threeList += 1
          starList = threeList
        }
        if (starsList === 'twoList'){
          twoList += 1
          starList = twoList
        }
        if (starsList === 'oneList'){
          oneList += 1
          starList = oneList
        }
      }
      else {
        if (starsList === 'fiveList'){
          if (fiveList !== 0){
          fiveList -= 1
          starList = fiveList
        }else {
          starList = 0
        }
      }
        if (starsList === 'fourList'){
          if (fourList !== 0){
            fourList -= 1
            starList = fourList
          }else {
            starList = 0
          }
        }
        if (starsList === 'threeList'){
          if (threeList !== 0){
            starList = threeList
          }else {
            starList = 0
          }
        }
        if (starsList === 'twoList'){
          if (twoList !== 0){
            starList = twoList
          }else {
            starList = 0
          }
        }
        if (starsList === 'oneList'){
          if (oneList !== 0){
            starList = oneList
          }else {
            starList = 0
          }
        }
      }

      content_data = {
        'stars': stars,
        'starList': starList,
        'starsList': starsList
      }
      console.log(content_data)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/mypage/${userId}/likemovies/`,
        headers: {'X-CSRFToken': csrftoken},
        data: JSON.stringify(content_data),
      })
      .then((res) => {
        const imgListStar = document.querySelector(`#img-list-star${stars}`)
        imgListStar.innerHTML = ``
        resdatas = res.data
        if (res.data[0].status === 'over') {
          console.log('over')
          const returnstarlist = res.data[0].returnstarlist
          if (returnstarlist === 'fiveList'){
            fiveList -= 1
          }
          if (returnstarlist === 'fourList'){
            fourList -= 1
          }
          if (returnstarlist === 'threeList'){
            threeList -= 1
          }
          if (returnstarlist === 'twoList'){
            twoList -= 1
          }
          if (returnstarlist === 'oneList'){
            oneList -= 1
          }
        }

        resdatas.forEach((data) => {
          imgListStar.innerHTML += `
          <img src="https://image.tmdb.org/t/p/w500${data.poster_url}" alt="movie img" class="movie-img">
          `
        })

      })
      .catch((res) => {
        console.log(res)
      })
    })

  }
});
  