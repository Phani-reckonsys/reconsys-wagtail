const homeTestimonialsMain = document.querySelector(".testimonials-main");
const homeTestimonialContainer = document.querySelector(".testimonials-container");
const homeTestimonialButton = document.querySelector(".hometestimonial-button");
const homeTestimonialButtonText = document.querySelector(".hometestimonial-button-text");

homeTestimonialButton.addEventListener("click", () => {
    if(homeTestimonialContainer.classList.contains("viewfour")){
        homeTestimonialContainer.classList.remove("viewfour");
        homeTestimonialsMain.classList.remove("viewfour");
        homeTestimonialButtonText.textContent = "View More"
        
    }else{
        homeTestimonialContainer.classList.add("viewfour");
        homeTestimonialsMain.classList.add("viewfour");
        homeTestimonialButtonText.textContent = "View Less"
    }
})