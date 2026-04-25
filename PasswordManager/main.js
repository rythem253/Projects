// This file will have all the backend logic to make my program alive

//This function gets the value of the entered username and password and return
//the value
function getUsername_Password() {
    const username = document.getElementById("usernameInput").value;
    const password = document.getElementById("passwordInput").value;

    return {username, password};
}

//Once most of GUI and front end will be done, this function will be split into many
//The encryption will have to check and match new logins. Most likely use a hashtable or linked list
document.getElementById("loginBtn").addEventListener("click", function () {
    const data = getUsername_Password();

    if (data.username === "" || data.password === "") {
        alert("Please fill in both fields");
    } else if (data.username === "master" || data.password === "123") {
        window.location.href = "page3.html";
    }
});

