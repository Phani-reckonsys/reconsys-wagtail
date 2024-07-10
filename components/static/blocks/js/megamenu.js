// service mega menu interactivity part starts
const servicebtn = document.getElementsByClassName("navitems-links")[1];
console.log(servicebtn);
const serviceModal = document.getElementById("services-modal");
const closeModal = document.getElementById("close-btn");

servicebtn.children[0].href="#";
servicebtn.children[0].removeAttribute('href');
servicebtn.children[0].style.cursor ="pointer";
servicebtn.addEventListener("click", (event) => {
    serviceModal.style.transform = "translateY(0)";
});

closeModal.addEventListener("click", (event) => {
    serviceModal.style.transform = "translateY(-100%)";
});
//service mega menu interactivity part ends
