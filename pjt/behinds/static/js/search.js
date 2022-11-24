const searchInput = document.querySelector('#search-input')
const csrftokenS = document.querySelector('[name=csrfmiddlewaretoken]').value
const resultBox = document.querySelector('#result-Box')

searchInput.addEventListener('keydown', function (event) {
  if (event.code === "Enter") {
    event.preventDefault()
  }
})
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
    url: `http://127.0.0.1:8000/behinds/`,
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
            <div style='width: 90%; max-height: fit-content; margin-top:15px; margin-bottom:2px; padding: 15px; background-color: white; border-radius: 20px; box-shadow: 5px 5px #5d5d5d; border: 2px solid black;'>
              <p style='text-decoration: underline;'>${result.username} 감독</p>
              <p style='font-size: small;'>${result.title}</p>
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