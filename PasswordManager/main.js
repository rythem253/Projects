// This file will have all the backend logic to make my program alive
function getUsername_Password() {
    const username = document.getElementById("usernameInput").value;
    const password = document.getElementById("passwordInput").value;

    return {username, password};
}

document.getElementById("loginBtn").addEventListener("click", function () {
    const data = getUsername_Password();

    if (data.username === "" || data.password === "") {
        alert("Please fill in both fields");
    } else {
        console.log("Username:", data.username);
        console.log("Password:", data.password);
        alert("Login capured");
    }
});