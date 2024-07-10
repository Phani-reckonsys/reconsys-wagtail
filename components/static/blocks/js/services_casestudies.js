 // CaseStudies Section Corousel
 let caseStudiesInterval;
 const carousalImageWrapper = document.querySelector(".case-studies-section .case-study-card");
 const carousalContentWrapper = document.querySelector(".case-studies-section .cards-wrapper-main");
 
 const carousalLeftArrow = document.querySelector(".case-studies-section .caseStudies-left-arrow");
 const carousalRightArrow = document.querySelector(".case-studies-section .caseStudies-right-arrow");
 const carouselIndicator = document.querySelectorAll(".case-studies-section .indicator");
 const carousalStudyCards = document.querySelectorAll(".case-studies-section .case-study-card");
 const carousalStudyCardsLength = carousalStudyCards.length;
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