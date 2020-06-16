//needs tones.js
function playTopNote(){
    tones.play("C#", 5);
}

function playBottomNote(){
    tones.play("A", 4);
}

function playBothNotes(){
    tones.play("C#", 5);
    tones.play("A", 4);
}

function playNote(noteName, octave){

}

function playTwoNotes(noteName1, octave1, noteName2, octave2){

}

function checkAnswer(event){
    answer = document.getElementById("answer-result");
    // if (event.target.innerHTML == interval) {
    //     answer.style.color = "green";
    //     answer.innerHTML = "Correct!";
    // }
    // else {
    //     answer.style.color = "red";
    //     answer.innerHTML = "Incorrect...";
    // }
}
function init() {
    //interval = "major third";
    topButton = document.getElementById("top-note-button");
    bottomButton = document.getElementById("bottom-note-button");
    bothButton = document.getElementById("both-notes-button");

    topButton.addEventListener("click", playTopNote);
    bottomButton.addEventListener("click", playBottomNote);
    bothButton.addEventListener("click", playBothNotes);
    answers = document.getElementsByClassName("interval-button");
    for(var i = 0; i < answers.length; i++){
        answers[i].addEventListener("click", checkAnswer);
    }

    tones.type = "sine";
    tones.release = 200;
}

document.addEventListener("DOMContentLoaded", init);
