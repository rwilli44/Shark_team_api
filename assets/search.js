"set strict";

/* CONSTANTS */

const SEARCH_CATEGORY = document.querySelector("#search-category");
const SEARCH_TERM = document.querySelector("#search-term");
const SEARCH_BUTTON = document.querySelector("#search-button");
const RESULTS_DIV = document.querySelector("#results");
const FORM = document.querySelector("form");

/* FUNCTIONS */

/**
 * This function adds the details of a book to the results div by accessing
 * the required parameters of the dictionary.
 * @param {object} book
 */
function showBook(book) {
  // Get existing innerHTML of the div in case multiple books are being added
  let inner_text = RESULTS_DIV.innerHTML;
  let to_add = `<p> <strong>${book.titre_ouvrage}</strong>, ${book.auteur_ouvrage}<br>Résumé : ${book.description_ouvrage}<br>Catégorie : ${book.categorie_ouvrage}<br>Prix : ${book.prix_ouvrage}</p>`;

  // Concatenate the new book result to any previously added books
  inner_text += to_add;

  // Update the div
  RESULTS_DIV.innerHTML = inner_text;
}

/**
 * This function calls the librairie API. If results are found, it calls showBook to add
 * each result, otherwise it shows a No results found message.
 * @param {string} search_cat
 * @param {string} search_word
 */
async function getResult(search_cat, search_word) {
  // Add the category and search term to the API url
  // the API server with uvicorn must be running
  let url =
    "http://127.0.0.1:8000/recherche_unitaire/?critere=" +
    search_cat.toLowerCase() +
    "&val=" +
    search_word.toLowerCase();

  // If no text is entered in the search bar, show a message
  if (search_word.length == 0) {
    RESULTS_DIV.innerHTML = `<p>Merci de remplir la barre de recherche.</p>`;
    return None;
  }

  // Fetch the API result with cross-origin requests
  // allowed as both are hosted locally
  fetch(url, { mode: "cors" })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // Reset the results div in case previous results are showing
      RESULTS_DIV.innerHTML = "";
      // If books are found, show in the results div
      if (data.length > 0) {
        let books = data;
        for (let i in books) {
          showBook(books[i]);
        }
      } else {
        // If no results are found
        RESULTS_DIV.innerHTML = `<p>Aucune résultat trouvé.</p>`;
      }
    })
    .catch((error) => {
      // In case of an API error, display a message indicating the problem
      RESULTS_DIV.innerHTML =
        "<p> Erreur : le catalogue de la librairie n'est pas disponible. Merci de réessayer ultérieurement.</p>" +
        error;
    });
}

/* EVEN LISTENERS */

FORM.addEventListener("submit", (e) => {
  // Prevent the page from refreshing
  e.preventDefault();
  // Get search results if user hits enter
  getResult(SEARCH_CATEGORY.value, SEARCH_TERM.value);
});

SEARCH_BUTTON.addEventListener("click", () => {
  // Get search results when search button is clicked
  getResult(SEARCH_CATEGORY.value, SEARCH_TERM.value);
});
