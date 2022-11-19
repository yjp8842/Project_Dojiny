const likeForms = document.querySelectorAll('.like-img-button')

likeForms.forEach(form => {
  form.addEventListener('click', function (event) {
    event.preventDefault()
    // console.log(event)
    const behindId = event.target.dataset.behindId
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/behinds/${behindId}/likes/`,
    })
      .then(response => {
        const isLiked = response.data.isLiked
        const likeImgBtn = document.querySelector(`.like-img-button-${behindId}`)
        if (isLiked === true) {
          likeImgBtn.setAttribute('src', "/static/images/heart.png")
        } else {
          likeImgBtn.setAttribute('src', "/static/images/love.png")
        }
        const likeCount = response.data.like_user_count
        console.log(likeCount)
        const likePTag = document.querySelector(`#like-count-${behindId}`)
        likePTag.innerText = likeCount
      })
      .catch(err => {
        console.log(err)
      })
    })
  })