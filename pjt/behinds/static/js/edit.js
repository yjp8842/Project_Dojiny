const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
// 수정 폼 불러오기 토글

const updateBtns = document.querySelectorAll(`.update-form`)
updateBtns.forEach(updateBtn => {
  updateBtn.addEventListener('submit', function (event) {
    event.preventDefault()
    // const commentContent = event.target.dataset.commentContent
    const commentId = event.target.dataset.commentId
    const commentScroll = document.querySelector('.comment-scroll')
    const commentContent = document.querySelector(`#comment-${commentId}`).innerText
    const targetTextDiv = document.querySelector(`#edit-div${commentId}`)
    const targetTextArea = document.querySelector(`#edit-area${commentId}`)
    const updateBtnAxios = document.querySelector(`.update-form-axios${commentId}`)
    targetTextArea.value = commentContent
    commentScroll.style.display = 'none'
    targetTextDiv.setAttribute('style','display:block;')
    updateBtn.setAttribute('style','display:none;')
    updateBtnAxios.setAttribute('style','display:block;')
    console.log(commentContent)
  })
})

const cancelBtns = document.querySelectorAll('.edit-cancel')
cancelBtns.forEach(cancelBtn => {
  cancelBtn.addEventListener('click', function(event) {
    event.preventDefault()
    const commentId = event.target.dataset.commentId
    // const commentContent = event.target.dataset.commentContent
    const commentScroll = document.querySelector('.comment-scroll')
    const commentContent = document.querySelector(`#comment-${commentId}`).innerText
    const targetTextDiv = document.querySelector(`#edit-div${commentId}`)
    const updateBtnAxios = document.querySelector(`.update-form-axios${commentId}`)
    const updateBtn = document.querySelector(`.update-form${commentId}`)
    const targetTextArea = document.querySelector(`#edit-area${commentId}`)
    targetTextArea.value = commentContent
    commentScroll.style.display = 'block'
    targetTextDiv.setAttribute('style','display:none;')
    updateBtnAxios.setAttribute('style','display:none;')
    updateBtn.setAttribute('style','display:block;')
    
  })
})

const updateBtnAxioses = document.querySelectorAll(`.udpate-form-axios`)
updateBtnAxioses.forEach(updateBtnAxios => {
  updateBtnAxios.addEventListener('submit', function (event) {
    event.preventDefault()
    const behindId = event.target.dataset.behindId
    const commentId = event.target.dataset.commentId
    const targetTextArea = document.querySelector(`#edit-area${commentId}`)
    const updateBtn = document.querySelector(`.update-form${commentId}`)
    if (targetTextArea.value === "") {
      return alert('내용을 입력해 주세요')
    }

    var content_data = {
      'behindId': behindId,
      'content': targetTextArea.value,
      'commentId': commentId,
      'csrftoken': csrftoken,
    }
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/behinds/${behindId}/comment_update/${commentId}/`,
      headers: {'X-CSRFToken': csrftoken},
      data: JSON.stringify(content_data),
    })
    .then(response => {
      // const commentContent = event.target.dataset.commentContent
      const commentScroll = document.querySelector('.comment-scroll')
      const targetTextDiv = document.querySelector(`#edit-div${commentId}`)
      const targetTextArea = document.querySelector(`#edit-area${commentId}`)
      targetTextArea.innerText = ''
      const updateBtnAxios = document.querySelector(`.update-form-axios${commentId}`)
      targetTextDiv.setAttribute('style','display:none;')
      updateBtn.setAttribute('style','display:block;')
      updateBtnAxios.setAttribute('style','display:none;')
      commentScroll.style.display = 'block'

      const data = response.data
      const commentTag = document.querySelector(`#comment-${ commentId }`)
      targetTextArea.innerText = data.editedContent
      commentTag.innerText = data.editedContent

    })
    .catch(error => {
      console.log(error)
    })
  })
})