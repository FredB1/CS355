/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
var header = document.getElementById("main-head");
var textBox = document.getElementById("main-text");
function myNavigator() {
    header.innerText = "Navigator"
    textBox.innerHTML = "Your app name is: " + navigator.appName + "<br> Your product is: " + navigator.product + "<br> Your appVersion is: " + navigator.appVersion + "<br> Your userAgent is: " +
        navigator.userAgent + "<br> Your platform is: " + navigator.platform + "<br> Your language is: " + navigator.language
}
function myWindow() {
    header.innerText = "Window"
    textBox.innerHTML = "Your window inner height is: " + window.innerHeight + "<br> Your window inner width is: " + window.innerWidth
}
function myScreen() {
    header.innerText = "Screen"
    textBox.innerHTML = "Your screen width is: " + screen.width + "<br> Your screen height is: " + screen.height + "<br> Your screen's available width is: " + screen.availWidth + "<br> Your screen's available height is: " +
        screen.availHeight + "<br> Your screen's color depth is: " + screen.colorDepth + "<br> Your screen's pixel depth is: " + screen.pixelDepth
}
function myLocation() {
    header.innerText = "Location"
    textBox.innerHTML = "Your href is: " + location.href + "<br> Your host name is: " + location.hostname + "<br>Your path name is: " + location.pathname + "<br>Your protocol is: " + location.protocol
}
function myGeolocation() {
    header.innerText = "Geolocation"
    //textBox.innerHTML = "Your latitude is: " + navigator.geolocation.getCurrentPosition()
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        textBox.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    textBox.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
}
