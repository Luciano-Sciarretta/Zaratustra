document.addEventListener("DOMContentLoaded", function () {
  const AUTHOR = document.getElementById('id_author')
  AUTHOR.addEventListener('input', async function (e) {
    const inputValue = AUTHOR.value
    // console.log('Usuario escribió:', inputValue)
    const response = await fetch(`/store/api/authors/search/?q=${encodeURIComponent(inputValue)}`)

    const data = await response.json()
    console.log("data:", data)
    for (let i = 0; i< data.authors.length; i++) {
      console.log("Author-name:", data.authors[i]['name'])
    }
    

  })


})