// service mega menu interactivity part starts

const technologybtn = document.getElementsByClassName("navitems-links")[2];
console.log(technologybtn);
const technologyModal = document.getElementById("technology-modal");
const closeTechnologyModal = document.getElementById("close-technology-btn");

technologybtn.children[0].href="#";
technologybtn.children[0].removeAttribute('href');
technologybtn.children[0].style.cursor ="pointer";
technologybtn.addEventListener("click", (event) => {
    technologyModal.style.transform = "translateY(0)";
});

closeTechnologyModal.addEventListener("click", (event) => {
    technologyModal.style.transform = "translateY(-100%)";
});
//service mega menu interactivity part ends
