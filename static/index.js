var male = ["Mr", "Sir"]
var female = ["Mrs", "Miss", "Ms", "Mme", "Lady", "Countess"]

function updateGender() {
    var title = document.getElementById("title").value
    
    if (male.includes(title)) {
        document.getElementById("male").checked = "checked"
    }
    else if (female.includes(title)) {
        document.getElementById("female").checked = "checked"
    }
}

function checkGender() {
    var title = document.getElementById("title").value

    if (document.getElementById("male").checked) {
        if (female.includes(title)) {
                alert("You're a " + title + " and also a male? Sounds a bit too gender fluid for 1912")
                document.getElementById("female").checked = "checked"
            }
    }
    else if (document.getElementById("female").checked) {
        if (male.includes(title)) {
                alert("You're a " + title + " and also a female? Sounds a bit too gender fluid for 1912")
                document.getElementById("male").checked = "checked"
            }
    }
}

var slider = document.getElementById("myRange");
var output = document.getElementById("fareOutput");
var multiplier = 30.84
var text = `Actual: $${slider.value}<br> Inflation Adjusted: $${slider.value * multiplier}`
output.innerHTML = text; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = `Actual: $${this.value}<br> Inflation Adjusted: $${Math.round(this.value * multiplier)}`;
}    
