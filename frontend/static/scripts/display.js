const domain = "http://164.90.136.53"
const addItem = document.querySelector("#add-item");
const searchItem = document.querySelector("#search-item");
const resetItem = document.querySelector("#reset-item");
const itemArticles = document.querySelectorAll("article.-item");

// console.log(addItem);
addItem.addEventListener("click", function(event) {
    event.preventDefault()
    var inputElement = document.getElementById("item-input");
    var inputValue = inputElement.value;
    if (inputValue.length < 1) {alert("Please provide an item")}
    else {
        console.log(inputValue);
        url = domain + ":5005/api/v1/item";
        data = JSON.stringify({"item": inputValue});
        makeRequest(url, "POST", data, operation="new item");
        //refresh the page to get the changes

    }
});

function replaceArticles(items) {

    for (let i = 0; i < items.length; i++) {
        let item = items[i];
        let itemArt = $("<article class='-item'></article>");
        let type = item.type

        let aTags = `
        <a href="${domain}:5000/display/${item.type}">
        <img src="../static/item_images/${item.type}.jpg" alt="">
            <div class="info">
                <h3>${item.type.replace("+", " ")}</h3>
                <h4>${item.latest_update}ksh 14,998 - Ksh 25,999</h4>
                <p>0 days 3hrs 4min Ago</p>
            </div>
        </a>`;
        itemArt.html(aTags);
        $(".item").append(itemArt);
    }

}

function makeRequest(url, method, data, operation="none") {

    var loadingPopupHTML = `
        <div id="loading-popup">
            <img src="../static/images/loading-load.gif" alt="">
            <h3>Loading...</h3>
        </div>
    `;

    // Convert the HTML string into DOM elements
    var parser = new DOMParser();
    var loadingPopup = parser.parseFromString(loadingPopupHTML, 'text/html').body.firstChild;

    document.body.appendChild(loadingPopup);

    fetch(url, {
        method: method,
	// mode: 'same-origin',
        headers: {"Content-Type": "application/json"},
        body: data
    })
        .then(response => {
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		return response.json();
	})
        .then(data => {
            document.body.removeChild(loadingPopup);

            if (operation === "search") {
                // console.log("more than 1")
                // console.log(itemArticles);
                for (var i = 0; i < itemArticles.length; i++) {
                    itemArticles[i].remove();
                }
                //do some things
                replaceArticles(data)
            }
            if (operation === "new item") {
                location.reload();
            }
            // console.log(data);
        })
        .catch(error => {
            console.log("Error:", error);
	    console.log("data:", data);
            document.body.removeChild(loadingPopup);
        });
}

searchItem.addEventListener("click", function(event) {
    event.preventDefault()
    var selectElement = document.getElementById("item-select");
    var selectedOption = selectElement.selectedOptions[0];
    var val = selectedOption.textContent;
    console.log(val);

    url = domain + ":5005/api/v1/item";
    data = JSON.stringify({"item": val});

    for (var i = 0; i < itemArticles.length; i++) {
        var h3Text = itemArticles[i].querySelector("h3").textContent;
        // console.log(h3Text);
        if (h3Text != val) {
            itemArticles[i].style.display = "none";
        }
        else {
            itemArticles[i].style.display = "block";
        }
    }
    // makeRequest(url, "PUT", data, operation="search");

});

resetItem.addEventListener("click", function(event) {
    event.preventDefault()

    for (var i = 0; i < itemArticles.length; i++) {
        itemArticles[i].style.display = "block";
    }
});
