// This file makes my project into a desktop application
// Although my project can also work on web
const { app, BrowserWindow } = require("electron");

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600
    });

    win.loadFile("login.html");
}

app.whenReady().then(createWindow);
