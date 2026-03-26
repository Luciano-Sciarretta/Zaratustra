
function showResults(data, input, resultsUl) {
  resultsUl.innerHTML = "";
  resultsUl.style.display = "none";

  if (data.length === 0) {
    const li = document.createElement("li")
    li.textContent = 'No matches';
    li.classList.add("no-results");
    resultsUl.appendChild(li)
    resultsUl.style.display = "block";

  } else {
    data.forEach(book => {
      const li = document.createElement("li")
      li.innerHTML = `${book.title} - ${book.author}`
      li.classList.add("result-item")
      resultsUl.style.display = "block"
      resultsUl.appendChild(li)
    
      // click en un resultado
      li.addEventListener("click", async () => {
        input.value = book.title;

        if (book.id) {
          window.location.href = `/store/${book.slug}/`;
        }
        
      })
    });

  }
}


document.addEventListener("DOMContentLoaded", () => {
  gsap.from("#main-popup", { duration: 2, y: "70%", opacity: 0, ease: "power2.out" });

  let debounceTimer;
  const input = document.querySelector(".my-search-input")
  const resultsUl = document.querySelector("#search-results")
  const submitButton = document.querySelector(".search-button")

  input.addEventListener("input",  () => {
    const query = input.value.trim()

    //Limpio el timer cada vez que se dispara el evento
    clearTimeout(debounceTimer)

    if (query.length > 2) {

      debounceTimer = setTimeout(async function() {

      try {
        const response = await fetch(`search_books/?q=${query}`);
        if (!response.ok) throw new Error("Error en el servidor");

        const data = await response.json()
        // console.log("Data desde  el servidor:", data)
        showResults(data, input, resultsUl)
      }
      catch (error) {
        console.error("Error en la búsqueda", error)
        resultsUl.style.display = "block"
        resultsUl.textContent = "There was an issue with the search, please try again later."
      }
   }, 300)
    } else {
      resultsUl.textContent = ""
    }

  })
  // submitInput(input, submitButton)

})









