console.log(new Date());

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
  
  // Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();


//countdown timer
var countDownDate = new Date().getTime() + (3 * 60 * 60 * 1000);

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("demo").innerHTML = hours + ":"
  + minutes + ":" + seconds + "";

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);

// Quest_bank and skillset page js

  // Get the value of the "applied_for" parameter from the URL query string
const urlParams = new URLSearchParams(window.location.search);
const appliedFor = urlParams.get('applied_for');

// Set the selected option in the dropdown menu based on the "applied_for" parameter value
const appliedForDropdown = document.getElementById('applied_for');
if (appliedFor) {
  appliedForDropdown.value = appliedFor;
}
const filter_by = urlParams.get('filter_by');

// Set the selected option in the dropdown menu based on the "applied_for" parameter value
const filter_byDropdown = document.getElementById('filter_by');
if (filter_by) {
  filter_byDropdown.value = filter_by;
}

// loader

function showLoader() {
  var loader = document.querySelector(".loader");
  loader.style.display = "block";
}

function hideLoader() {
  var loader = document.querySelector(".loader");
  loader.style.display = "none";
}

window.addEventListener("load", function () {
  var links = document.querySelectorAll("a");
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener("click", function () {
      showLoader();
    });
  }
});

