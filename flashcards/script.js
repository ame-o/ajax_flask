// https://api.dictionaryapi.dev/api/v2/entries/en/<word>

var card = document.querySelector('.card');
card.addEventListener('click', function () {
    card.classList.toggle('is-flipped');
});

async function call_word() {
    var spelling = document.getElementById("spelling")
    console.log(spelling.innerText);
    var response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${spelling.innerText}`);
    var word = await response.json();
    console.log(word);
    link = word[0].phonetics[0].audio
    pronounciation = document.getElementById("pronounciation")
    pronounciation.src = link
    // return link
}
call_word();

