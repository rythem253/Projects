/**
 * This file is designated to create and store new accounts into the database.
 */
const createdUsername = document.getElementById("createUsername").value;
const createdPassword = document.getElementById("createPassword").value;


document.getElementById("createAccountBtn").addEventListener("click", function() {
   alert(createdUsername);
   alert(createdPassword);
});
