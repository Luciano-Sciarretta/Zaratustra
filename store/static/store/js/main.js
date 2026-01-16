document.addEventListener("DOMContentLoaded", function () {
  const AUTHOR = document.getElementById('id_author')

  let timer;

  AUTHOR.addEventListener('input', function (e) {

    clearTimeout(timer)
    // console.log("Limpio el timer")

    timer = setTimeout(async () => {
      // console.log("comienza  el timer")
      const inputValue = AUTHOR.value
      const suggestionsList = document.getElementById('suggestions-list')
      if (inputValue.length == 0) {
        suggestionsList.innerHTML = ''
        suggestionsList.style.display = 'none';
        return
      }

      const response = await fetch(`/store/api/authors/search/?q=${encodeURIComponent(inputValue)}`)

      const data = await response.json()
      // console.log("Llega la respuesta del servidor")

      suggestionsList.innerHTML = ''
      for (let i = 0; i < data.authors.length; i++) {
        let author = data.authors[i]['name']
        let li = document.createElement('li')
        li.textContent = author
        suggestionsList.appendChild(li)
        suggestionsList.style.display = 'block'
        li.addEventListener('click', function () {
          AUTHOR.value = author
          suggestionsList.style.display = 'none'
        })
      }
    }, 500)
    // console.log("Termina el timer")
  })
})