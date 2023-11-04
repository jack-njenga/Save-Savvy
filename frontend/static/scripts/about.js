
const img = document.querySelector("section img#me");

function changeImg () {
    console.log(img.src);
    if (img.src.includes("me")) {
        img.src = "../static/images/red.jpg";
    }
    else {
        img.src = "../static/images/me.jpg";
    }
}