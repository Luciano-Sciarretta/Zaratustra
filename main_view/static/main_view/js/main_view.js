
function showResults(data, input, resultsUl) {
  resultsUl.innerHTML = "";

  if (data.length === 0) {
    const li = document.createElement("li")
    li.textContent = 'No matches';
    li.classList.add("no-results");
    resultsUl.appendChild(li)

  } else {
    data.forEach(book => {
      const li = document.createElement("li")
      li.textContent = book.title
      li.classList.add("result-item")
      resultsUl.style.display = "block"
      resultsUl.appendChild(li)
      resultsUl.style.display = "block"
      // click en un resultado

      li.addEventListener("click", async () => {
        input.value = book.title;
        if (book.id) {
          window.location.href = `/store/${book.id}/`;
        }
      })
    });

  }
}

//     submit de la barra de búsqueda     //

function submitInput(input, submitButton) {

  submitButton.addEventListener("click", async () => {
    const bookId = input.dataset.id
    if (bookId) {
      const result = await fetch(`store/${bookId}/`)
      console.log("Result", result)
      window.location.href = `/store/${bookId}/`;
    }
  })
}


document.addEventListener("DOMContentLoaded", () => {
  gsap.from("#main-popup", { duration: 2, y: "70%", opacity: 0, ease: "power2.out" });


  const input = document.querySelector(".my-search-input")
  const resultsUl = document.querySelector("#search-results")
  const submitButton = document.querySelector(".search-button")

  input.addEventListener("input", async () => {
    const query = input.value.trim()

    if (query.length > 0) {
      try {
        const response = await fetch(`search_books/?q=${query}`);
        const data = await response.json()
        showResults(data, input, resultsUl)
      }
      catch (error) {
        console.error("Error en la búsqueda", error)
        resultsUl.style.display = "block"
        resultsUl.textContent = "There was an issue with the search, please try again later."
      }
    } else {
      resultsUl.textContent = ""
    }

  })
  submitInput(input, submitButton)

})









