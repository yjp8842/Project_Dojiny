const loadForm = document.querySelector('#load-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
const movieList = document.querySelector('.movie-list')

var pageCount = null

loadForm.addEventListener('submit', function(event) {
  event.preventDefault()
  pageCount += 1
  var content_data = {
    'pageCount': pageCount,
  }
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/movies/`,
    headers: {'X-CSRFToken': csrftoken},
    data: JSON.stringify(content_data),
  })
  .then((res) => {
    console.log(res)  
    movies = res.data
    console.log(typeof(movies))
    for (let i=0; i<20; i++) {
      movie = movies[i]
      movieList.innerHTML += `
      <a href="{% url 'movies:detail' movie.pk %}" class="movie-a">
        <img src="https://image.tmdb.org/t/p/w500${movie.poster_url}" alt="movie img" class="movie-img">
        <div class="info">${movie.title}</div>
      </a>
      `
    }
  })
  .catch((err) => {
    console.log(err)
  })
})