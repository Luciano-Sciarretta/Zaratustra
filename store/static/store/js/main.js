document.addEventListener("DOMContentLoaded", function () {
  const AUTHOR = document.getElementById('id_author')

  AUTHOR.addEventListener('input', async function (e) {
    const inputValue = AUTHOR.value
    const response = await fetch(`/store/api/authors/search/?q=${encodeURIComponent(inputValue)}`)

    const data = await response.json()
    const suggestionsList = document.getElementById('suggestions-list')

    suggestionsList.innerHTML = ''
    for (let i = 0; i < data.authors.length; i++) {
      let author = data.authors[i]['name']
      let li = document.createElement('li')
      li.textContent = author
      suggestionsList.appendChild(li)
      suggestionsList.style.display = 'block'
      li.addEventListener('click', function() {
        AUTHOR.value = author
        suggestionsList.style.display = 'none'  
        
        


      })
    }


  })


})