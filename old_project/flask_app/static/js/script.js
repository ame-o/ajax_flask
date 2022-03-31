// https://api.dictionaryapi.dev/api/v2/entries/en/<word>
console.log("hello hello...");

var card = document.querySelector('.card');
card.addEventListener('click', function () {
    card.classList.toggle('is-flipped');
});

async function call_word() {
    var response = await fetch("https://api.dictionaryapi.dev/api/v2/entries/en/adjacent");
    var word = await response.json();
    console.log(word);
    link = word[0].phonetics[0].audio
    pronounciation = document.getElementById("pronounciation")
    pronounciation.src = link
}


