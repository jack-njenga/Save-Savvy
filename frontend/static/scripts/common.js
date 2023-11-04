function apiGetReady(){
    // const url = "http://127.0.0.1:5005/api/v1/"
    const url = "http://164.90.136.53:5005/api/v1/"

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            var key = Object.keys(data);
            const logo = document.querySelector(".logo img")
            if (data[key] == "SUCCESS") {
                // console.log(logo);
                logo.id = "ready";
                console.log("API: ", data[key]);
            }
            else {
                logo.id = "not-ready";
                console.log("API: ", "FAILED");
            }
        })
        .catch(error => {
            console.log("API: ", "FAILED");
            console.log("Error:", error);
        });
}
apiGetReady();
