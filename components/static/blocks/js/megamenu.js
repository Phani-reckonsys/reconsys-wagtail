// service mega menu interactivity part starts
const servicebtn = document.getElementById("services-btn");
const serviceModal = document.getElementById("services-modal");
const closeModal = document.getElementById("close-btn");


servicebtn.addEventListener("click", (event) => {
    serviceModal.style.transform = "translateY(0)";
});

closeModal.addEventListener("click", (event) => {
    serviceModal.style.transform = "translateY(-100%)";
});
//service mega menu interactivity part ends