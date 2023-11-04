
const selectOption = document.querySelector("select#filter-option");
imgElem = document.querySelector("img#price-lineplot")

selectOption.addEventListener("change", function() {
    var val = selectOption.value;
    console.log(val);

    var link = imgElem.src.split("-")[0];
    var deflt = link + "-updated_at.png";
    var newLink = link + "-" + val + ".png";
    if (val === "default") {
        imgElem.src = deflt;
    }
    else {imgElem.src = newLink;}
    // console.log(newLink);


});

