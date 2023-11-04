
// const signInData = {
//     firstName: "",
//     lastName: "",
//     email: "",
//     age: 0,
//     gender: "",
//     pwd: "******",
//     signed: false,
//     timestamp: new Date().getTime()
// }
function getCookie(name) {
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) {
            return cookieValue;
        }
    }
    return null;
}

const redSignIn = document.querySelector("div.accounts");
const user = document.querySelector("div.logged-in");
const userLogo = document.querySelector("div.logged-in img");
const startButton = document.querySelector("button#start");
const signInChoice = document.querySelector("form#signin-choice")
const signInForm = document.querySelector("form#sign-in");
const signIn = document.querySelector("button#start-signin");
const createAccount = document.querySelector("button#start-create-account");
const createAccountForm = document.querySelector("form#create-account");
const skip = document.querySelector("button#start-skip");

const signInSubmit = document.querySelector("button#signin");
const startLink = document.getElementById('startLink');

function start() {
    // console.log(startButton);
    var signed = getCookie('signed') === 'true';
    const timeSession = getCookie('timestamp');
    const currentTimestamp = new Date().getTime();
    // check the currentTimestamp - timeSession if its > 5 mins  di something
    if (signed === true) {
        // alert("signed in");
        if (timeSession) {
            const timeSessionNumber = parseFloat(timeSession);
            const timeDifference = currentTimestamp - timeSessionNumber;
            // 300000 =  5 mins
            if (timeDifference > 300000) {
                document.cookie = `signed=${false}`;
                // signed = false;
                console.log('Session expired. Logging out...');
                // start()
            }
            else {
                console.log('Session is up and running');
            }
        } else {
            console.log('timeSession cookie is not set.\n Setting it up');
            var nw =  new Date().getTime()
            document.cookie = `timestamp=${nw}`;
        }

        startButton.textContent = "Explore";
        window.location.href = "http://164.90.136.53:5000/display";
    }
    else {
        // alert("sign in Please");
        startButton.style.display = 'none';
        signInChoice.style.display = 'block';
        signIn.addEventListener('click', function(event) {
            // alert("yea");
            event.preventDefault();
            signInChoice.style.display = 'none';
            signInForm.style.display = 'block';
            // signingIn();
        });
        createAccount.addEventListener('click', function(event) {
            // alert("create account");
            accountData = {}

            event.preventDefault()
            signInChoice.style.display = 'none';
            signInForm.style.display = 'none';
            createAccountForm.style.display = 'block';
            createAccountForm.style.width = '450px';
            createAccountForm.addEventListener('submit', function(event) {
                event.preventDefault();
                var firstName = document.getElementById("first_name");
                var lastName = document.getElementById("Last_name");
                var email = document.getElementById("email");
                var birthDate = document.getElementById("dob");
                var gender = document.getElementById("gender");
                var newPwd = document.getElementById("password");
                var confirmPwd = document.getElementById("confirm-password");

                accountData = {
                    "first_name": firstName.value,
                    "last_name": lastName.value,
                    "email": email.value,
                    "dob": birthDate.value,
                    "gender": gender.value,
                    "password": newPwd.value
                };
                data = JSON.stringify(accountData);
                console.log(accountData);
                // api POST request fro here

                url = "http://164.90.136.53:5005/api/v1/users/";

                fetch(url, {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: data
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        createAccountForm.style.display = 'none';
                        startButton.style.display = 'block';

                        popup = document.querySelector("div.success-popup");
                        popup.style.display = "block"
                        console.log(popup);
                        popup.classList.add("open-popup");
                        // startButton.style.display = "none";

                        signNow = document.querySelector("button#sign-now");
                        // console.log(signNow);
                        signNow.addEventListener('click', function(event) {
                            popup.classList.remove("open-popup");
                            startButton.style.display = 'none';
                            signInForm.style.display = 'block';
                        });
                    })
                    .catch(error => {
                        console.log("Error:", error);
                    });

            })
        });
        skip.addEventListener('click', function(event) {
            // alert("skip");
            event.preventDefault();
            signInChoice.style.display = 'none';
            // createAccountForm.style.display = 'block';
            startButton.style.display = 'block';
            document.cookie = `signed=${true}`;
        });
    }
}

function signingIn() {
    const signInData = {
        firstName: "",
        lastName: "",
        email: "",
        age: 0,
        gender: "",
        pwd: "******",
        signed: false,
        timestamp: new Date().getTime()
    }
    signInfo = {}
    signInForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("pwd").value;
        // console.log(`Name: ${username}\nPwd: ${password}`);
        // from here make GET request to api
        signInfo["email"] = username;
        signInfo["password"] = password;
        // console.log(signInfo);
        // alert("Signing in now!");
        url = "http://164.90.136.53:5005/api/v1/user"

        fetch(url, {
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(signInfo)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            let status = false;
            keys = Object.keys(data);
            // console.log(keys);
            for (const key of keys) {
                // console.log(key)
                if (["email", "first_name", "last_name"].includes(key)) {status=true}
                else if (["user"].includes(key)) {
                    if (data[key] === "forgot_pwd") {
                        status = "forgotPwd";
                    }
                    if (data[key] === false) {
                        status = false;
                    }
                }
            }
            console.log(status);
            if (status === true) {
                signInData.firstName = data["first_name"];
                signInData.lastName = data["last_name"];
                signInData.email = data["email"];
                signInData.gender = data["gender"]
                signInData.signed = true;

                // set signin cookies to the broswer using SignInData
                document.cookie = `firstName=${signInData.firstName}`;
                document.cookie = `lastName=${signInData.lastName}`;
                document.cookie = `email=${signInData.email}`;
                document.cookie = `gender=${signInData.gender}`;
                document.cookie = `signed=${signInData.signed ? 'true' : 'false'}`;
                document.cookie = `timestamp=${signInData.timestamp}`;

                startButton.textContent = "Explore";

                // console.log(redSignIn);
                // console.log(user);
                // console.log(userLogo);
                redSignIn.style.display = "none";
                if (["male", "Male"].includes(signInData.gender)) {
                    userLogo.src = "../static/images/male-acc";
                }
                else if (["female", "Female"].includes(signInData.gender)) {
                    userLogo.src = "../static/images/female-acc";
                }
                else if (["lgbtq", "LGBTQ"].includes(signInData.gender)) {
                    userLogo.src = "../static/images/lgbtq.jpg"
                }
                else {
                    userLogo.src = "../static/images/other.png"
                }
                userLogo.style.display = "block";
                user.style.display = "inline-block";
                signInForm.style.display = "none";
                startButton.style.display = "block";

            }
            else if (status === false) {
                alert("You don't have an account yet");
            }
            else {
                alert("Incorrect password");
            }
        })
        .catch(error => {
            console.log("Error:", error);
        });


        })
}
signingIn();
