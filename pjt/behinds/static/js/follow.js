
const forms = document.querySelectorAll('#follow-form')
// console.log(form)
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
forms.forEach(form => {
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    // console.log(event)
    const userId = event.target.dataset.userId

    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/${userId}/follow/`,
      headers: {'X-CSRFToken': csrftoken},
    })
      .then(response => {
        // 팔로우 버튼 토글
        // console.log(response)
        const followBtns = document.querySelectorAll(`#follow-form > #like-button-${userId}`)

        followBtns.forEach(followBtn => {
          const isFollowed = response.data.isFollowed
          if (isFollowed === true) {
            followBtn.innerText = '언팔로우'
          } else {
            followBtn.innerText = '팔로우'
          }
        })
      })
  })
})