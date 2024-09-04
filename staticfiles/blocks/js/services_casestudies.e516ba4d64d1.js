 // CaseStudies Section Corousel
 document.addEventListener("DOMContentLoaded", (event) => {
 let caseStudiesInterval;
 const carousalImageWrapper = document.querySelector(".case-study-card");
 const carousalContentWrapper = document.querySelector(".cards-wrapper-main");
 console.log(carousalContentWrapper);
 console.log(carousalImageWrapper);
 const carousalLeftArrow = document.querySelector(".caseStudies-left-arrow");
 const carousalRightArrow = document.querySelector(".caseStudies-right-arrow");
 const carousalStudyCards = document.querySelectorAll(".case-study-card");
 const carousalStudyCardsLength = carousalStudyCards.length;
 console.log(carousalContentWrapper);
 carousalContentWrapper.style.width = `${carousalStudyCards.length*100}%`;


 let corouselIndex = 0;
 
 const moveToCorouselIndex = (index) => {
   corouselIndex = (index + carousalStudyCardsLength) % carousalStudyCardsLength;
   let translateX = ((corouselIndex % carousalStudyCardsLength) * -100) / carousalStudyCardsLength;
   carousalImageWrapper.style.transform = `translateX(${translateX}%)`;
   carousalContentWrapper.style.transform = `translateX(${translateX}%)`;
 };


 startCaseStudiesCarouselInterval();
 carousalRightArrow.addEventListener("click", () => {
   moveToCorouselIndex(corouselIndex + 1);
   stopCaseStudiesCarouselInterval();
   startCaseStudiesCarouselInterval()
 });
 
 carousalLeftArrow.addEventListener("click", () => {
   moveToCorouselIndex(corouselIndex - 1);
   stopCaseStudiesCarouselInterval();
   startCaseStudiesCarouselInterval()
 });

 function startCaseStudiesCarouselInterval() {
   caseStudiesInterval = setInterval(() => {
       moveToCorouselIndex(corouselIndex + 1);
   }, 5000);
}

// Function to stop the interval
function stopCaseStudiesCarouselInterval() {
   clearInterval(caseStudiesInterval);
}

 })