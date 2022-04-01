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



// --------------------------------------------------------------
// Today's Date
// --------------------------------------------------------------


var today = new Date();
        var currentDate = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        // document.getElementById("currentDate").value = date;

console.log(currentDate);
currentDate= currentDate.toString();

function findWeek(currentDate){

    console.log(currentDate);

    var week_list = [
        ["2022-3-31","2022-4-1","2022-4-2","2022-4-3","2022-4-4","2022-4-5","2022-4-6"]
        ,
        ["2022-4-7","2022-4-8","2022-4-9","2022-4-10","2022-4-11","2022-4-12","2022-4-13","2022-4-14","2022-4-15","2022-4-16","2022-4-17","2022-4-18","2022-4-19"]
        ,
        ["2022-4-20","2022-4-21","2022-4-22","2022-4-23","2022-4-24","2022-4-25","2022-4-26"]
        ,
        ["2022-4-27","2022-4-28","2022-4-29","2022-4-30","2022-5-1","2022-5-2","2022-5-3","2022-5-4"]
        ,
        ["2022-5-5","2022-5-6","2022-5-7","2022-5-8","2022-5-9","2022-5-10","2022-5-11"]
        ,
        ["2022-5-12","2022-5-13","2022-5-14","2022-5-15","2022-5-16","2022-5-17","2022-5-18"]
        ,
        ["2022-5-19","2022-5-20","2022-5-21","2022-5-22","2022-5-23","2022-5-24"]
        ,
        ["2022-5-25","2022-5-26","2022-5-27","2022-5-28","2022-5-29","2022-5-30","2022-5-31","2022-6-1"]
        ,
        ["2022-6-2","2022-6-3","2022-6-4","2022-6-5","2022-6-6","2022-6-7","2022-6-8"]
    ]
    week_id = ""
    for(var i = 0;i<week_list.length; i++) {
        for(var j = 0;j<week_list[i].length; j++) {
            if(currentDate == week_list[i][j]){
                week_id = i+1
                console.log(week_id)
                return week_id
            }
        }
    }
}
var this_week = findWeek(currentDate);
document.getElementById("currentDate").innerText = date;
