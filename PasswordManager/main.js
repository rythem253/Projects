/**
 * This file is designated to have the login page GUI backend.
 */

function createUsername_Password() {

    const newUsername = document.getElementById("createUsername").value;
    const newPassword = document.getElementById("createPassword").value;
    return {newUsername, newPassword};
}

//This function gets the value of the entered username and password and return
//the value
function getUsername_Password() {

    const username = document.getElementById("usernameInput").value;
    const password = document.getElementById("passwordInput").value;
    return {username, password};
}

const createBtn = document.getElementById("createAccountBtn");

if (createBtn) {
    createBtn.addEventListener("click", function () {
    const createData = createUsername_Password();
    localStorage.setItem(createData.newUsername, createData.newPassword);
    alert("Account created");
    window.location = "login.html";
    });
}


//Once most of GUI and front end will be done, this function will be split into many
//The encryption will have to check and match new logins. Most likely use a hashtable or linked list
const loginBtn = document.getElementById("loginBtn");

if (loginBtn) {

    loginBtn.addEventListener("click", function() {

    const data = getUsername_Password();
    const storedPassword = localStorage.getItem(data.username);

        if (data.username === "" || data.password === "") {
            alert("Please fill in both fields");
        } else if 
            (storedPassword === null) {
            alert("User not exist");
        } else if 
            (storedPassword === data.password) {
            window.location = "dashboard.html";
        } else {
            alert("IDK");
        }
    }); 
}
    

