/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
console.log("console");
function openNav() {
  console.log("clicked");
  const openBtnValue = document.getElementById("openBtn").value;
  let sidebarArr = ["Profile", "dashboard", "Leads"];
  if (openBtnValue == "open") {
    console.log("working");
    document.getElementById("sidebar").style.width = "200px";
    document.getElementById("openBtn").value = "close";
    // document.getElementById("openBtn").innerText = "Close";
    document.getElementById("dashboard").innerText = "dashboard";
    document.getElementById("Profile").innerText = "Profile";
    document.getElementById("Leads").innerText = "Leads";
    document.getElementById("Customers").innerText = "Customers";
    document.getElementById("Tasks").innerText = "Tasks";
    document.getElementById("VideoCon").innerText = "VideoCon";
    document.getElementById("LogOut").innerText = "LogOut";
    for (let i = 0; i < sidebarArr.length; i++) {
      console.log(sidebarArr[i]);
    }
  } else if (openBtnValue == "close") {
    document.getElementById("sidebar").style.width = "70px";
    document.getElementById("openBtn").value = "open";
    // document.getElementById("openBtn").innerText = "Open";
    document.getElementById("dashboard").innerHTML = "";
    document.getElementById("Profile").innerText = "";
    document.getElementById("Leads").innerText = "";
    document.getElementById("Customers").innerText = "";
    document.getElementById("Tasks").innerText = "";
    document.getElementById("VideoCon").innerText = "";
    document.getElementById("LogOut").innerText = "";
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
