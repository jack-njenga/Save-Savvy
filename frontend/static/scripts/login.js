userLogoDiv = document.querySelector("div.logged-in");
const userLog = document.querySelector("div.logged-in img");
const SignIn = document.querySelector("div.accounts");
const userName = document.querySelector("div.logged-in b")

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

const firstName = getCookie('firstName');
const lastName = getCookie('lastName');
const email = getCookie('email');
const gender = getCookie('gender');
const signed = getCookie('signed') === 'true';

if (signed) {

    console.log(`First Name: ${firstName}`);
    console.log(`Last Name: ${lastName}`);
    console.log(`Email: ${email}`);
    console.log(`Gender: ${gender}`);

    SignIn.style.display = "none";
    // console.log(userLog);
    if (["male", "Male"].includes(gender)) {
        userLog.src = "../static/images/male-acc";
    }
    else if (["female", "Female"].includes(gender)) {
        userLog.src = "../static/images/female-acc";
    }
    else if (["lgbtq", "LGBTQ"].includes(gender)) {
        userLog.src = "../static/images/lgbtq.jpg"
    }
    else {
        userLog.src = "../static/images/other.png"
    }
    userName.textContent = firstName;
    // console.log(userName);
    userLogoDiv.style.display = "block";
    userLog.style.display = "block";
}
else {
    console.log("(login) Please login");
    SignIn.style.display = "block";
    userLogoDiv.style.display = "none";
    userLog.style.display = "none";
}
// console.log(`First Name: ${firstName}`);