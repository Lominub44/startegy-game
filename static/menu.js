document.getElementById("host-btn").addEventListener("click", hostGame);
document.getElementById("join-btn").addEventListener("click", joinGame);
document.getElementById("start-btn").addEventListener("click", startGame);
document.getElementById("exit-btn").addEventListener("click", exitGame);

function hostGame() {
    var gameName = document.getElementById("game-name").value;
    // Logik für das Hosting des Spiels hier einfügen
    console.log("Spiel gehostet: " + gameName);
}

function joinGame() {
    var gameCode = document.getElementById("game-code").value;
    // Logik für das Beitritt zum Spiel hier einfügen
    console.log("Spiel beigetreten: " + gameCode);
}

function startGame() {
    // Logik für das Starten des Spiels hier einfügen
    console.log("Spiel gestartet!");
}

function exitGame() {
    // Logik für das Verlassen des Spiels hier einfügen
    console.log("Spiel verlassen!");
}
