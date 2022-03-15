/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
console.log("console");
function openNav() {
  console.log("clicked");
  const openBtnValue = document.getElementById("openBtn").value;
  if (openBtnValue == "open") {
    document.getElementById("sidebar").style.width = "250px";
    document.getElementById("openBtn").value = "close";
    document.getElementById("openBtn").innerText = "Close";
  } else if (openBtnValue == "close") {
    document.getElementById("sidebar").style.width = "70px";
    document.getElementById("openBtn").value = "open";
    document.getElementById("openBtn").innerText = "Open";
  }
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */

// deleting leads
function deleteLead() {
  console.log("delete");
  let del;
  let id = document.getElementById("i.id");
  console.log(id);

  let prompt = "Are you sure you want to delete!\nEither OK or Cancel.";
  if (confirm(prompt) == true) {
    console.log("deleted");
  }
}
