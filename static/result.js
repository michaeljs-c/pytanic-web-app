function changeBG(pred, image) {
    if (pred == 1){
        document.getElementById("pred").innerHTML = "SURVIVED &#128516;"
        document.getElementById("pred").style.color = "green"
        document.getElementById("img").src = image
    }
    else if (pred == 0) {
        document.getElementById("pred").innerHTML = "Dead  &#128517;"
        document.getElementById("pred").style.color = "red"
        document.getElementById("img").src = image
        
        document.body.style.backgroundColor = "black"
    }
    else {
        document.body.style.backgroundColor = "green"
    }
}

