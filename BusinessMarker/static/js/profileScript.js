let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

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
   closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the icons class
 }
 else {
   closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the icons class
 }
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
