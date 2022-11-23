const searchInput = document.querySelector('#search-input')
const csrftokenS = document.querySelector('[name=csrfmiddlewaretoken]').value

// 결과 띄우는 창만 수정하면 됨
const resultBox = document.querySelector('#result-Box')

searchInput.addEventListener('keyup', function (event) {
  // const allBehinds = event.target.dataset.behindContent

  const inputContent = event.target.value

  if (resultBox.classList.contains('not-visible')){
    resultBox.classList.remove('not-visible')
  }

  var content_data = {
    'inputContent': inputContent,
    'csrftoken': csrftokenS,
  }
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/movies/`,
    headers: {'X-CSRFToken': csrftokenS},
    data: JSON.stringify(content_data),
  })
  .then((res) => {
    const searchResult = res.data.searchResult
    console.log(searchResult)
    resultBox.innerHTML += ``
    if (Array.isArray(searchResult)){
      resultBox.innerHTML = ``
      searchResult.forEach(result => {
        resultBox.innerHTML += `
          <a href='http://127.0.0.1:8000/behinds/${result.pk}/detail/' class='link'>
            <div style='margin-top:2px; margin-bottom:2px; color:black'>
              <div>
                <p>${result.username} | ${result.title}</p>
              </div>
            </div>
          </a>
        `
      })
    }
    else{
      console.log('no results')
      if (searchResult.length > 0){
        resultBox.innerHTML = `<b>${searchResult}</b>`
      }
      else{
        resultBox.classList.add('not-visible')
      }
    }

  })
  .catch((err) => {
    console.log(err)
  })
})