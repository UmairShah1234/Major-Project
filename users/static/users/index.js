/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
console.log("console");
function openNav() {
  console.log("clicked");
  const openBtnValue = document.getElementById("openBtn").value;
  if (openBtnValue == 'open'){
    document.getElementById("sidebar").style.width = '250px';
    document.getElementById("openBtn").value = 'close';
    document.getElementById("openBtn").innerText = 'Close';
  }else if(openBtnValue == 'close'){
    document.getElementById("sidebar").style.width = '70px';
    document.getElementById("openBtn").value = 'open';
    document.getElementById("openBtn").innerText = 'Open';

  }
  }
  
  /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
