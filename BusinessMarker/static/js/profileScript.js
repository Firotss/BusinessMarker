let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");
let logo = document.querySelector(".logo_name");
let checkBtn = false;
closeBtn.addEventListener("click", ()=>{
  sidebar.classList.toggle("open");
  menuBtnChange();//calling the function(optional)
});

searchBtn.addEventListener("click", ()=>{ // Sidebar open when you click on the search iocn
  sidebar.classList.toggle("open");
  menuBtnChange(); //calling the function(optional)
});

// following are the code to change sidebar button(optional)
function menuBtnChange() {
 if(sidebar.classList.contains("open")){
   logo.style.display = "block";
   checkBtn = true;
   closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the icons class
 }
 else {
  setTimeout(displayNone, 500);
  
  checkElements = document.querySelectorAll("li.showMenu")
  if(checkElements != null)
  {
    checkElements.forEach(element => {
      let event = new Event("click");
      element.querySelector(".tab").dispatchEvent(event);
    });
  }
  checkBtn = false;
  closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the icons class
 }
}
function displayNone() {
  logo.style.display = "none";
}
const tabBtn = document.querySelectorAll(".tab");
const tab = document.querySelectorAll(".tabShow");

function tabs(panelIndex) {
  tab.forEach(function(node) {
    node.style.display = "none";
  });
  tab[panelIndex].style.display = "block";
}
tabs(2);

function checkType(type){
  if(type == "api" || type == "local")
  {
    document.getElementsByClassName("sub-menu")[1].id = type;
    document.getElementsByClassName("sub-menu")[1].querySelectorAll("li a").forEach(element => {
      element.style.background = "rgb(8, 8, 8)";
      element.style.color = "#fff";
    });
    document.getElementsByClassName("sub-menu")[1].querySelectorAll("li").forEach(element => {
      if (element.className == type){
        element.querySelectorAll("a")[0].style.background = "#fff";
        element.querySelectorAll("a")[0].style.color = "rgb(8, 8, 8)";
      }
    });
  }
  else
  {
    document.getElementsByClassName("sub-menu")[0].id = type;
    document.getElementsByClassName("sub-menu")[0].querySelectorAll("li a").forEach(element => {
      element.style.background = "rgb(8, 8, 8)";
      element.style.color = "#fff";
    });
    document.getElementsByClassName("sub-menu")[0].querySelectorAll("li").forEach(element => {
      if (element.className == type){
        element.querySelectorAll("a")[0].style.background = "#fff";
        element.querySelectorAll("a")[0].style.color = "rgb(8, 8, 8)";
      }
    });
  }
}
checkType("local")
checkType("restaurant")
let arrow = document.querySelectorAll(".tab");
arrow.forEach(element => {
  element.addEventListener("click", (e)=>{
    if(checkBtn == true)
    {
      let arrowParent = e.target.parentElement.parentElement;
      arrowParent.classList.toggle("showMenu");
      arrowParent = e.target.parentElement;
      arrowParent.classList.toggle("showMenu");
    }
  });
});
  