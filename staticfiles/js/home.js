  //industries section corousel'
  const industriesLeftArrow = document.querySelector(
    ".industries-corousel-left-arrow"
  );
  const industriesRightArrow = document.querySelector(
    ".industries-corousel-Right-arrow"
  );
  
  // CaseStudies Section Corousel
  let caseStudiesInterval;
  const carousalImageWrapper = document.querySelector(".case-studies-section .case-study-card");
  const carousalContentWrapper = document.querySelector(".case-studies-section .cards-wrapper");
  
  const carousalLeftArrow = document.querySelector(".case-studies-section .caseStudies-left-arrow");
  const carousalRightArrow = document.querySelector(".case-studies-section .caseStudies-right-arrow");
  
  const carouselIndicator = document.querySelectorAll(".case-studies-section .indicator");
  const carousalStudyCards = document.querySelectorAll(".case-studies-section .case-study-card");
  carousalContentWrapper.style.width = `${carousalStudyCards.length*100}%`;

  let corouselIndex = 0;
  
  const moveToCorouselIndex = (index) => {
    corouselIndex = (index + 3) % 3;
    let translateX = ((corouselIndex % 3) * -100) / 3;
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
  
  // Sector Cards Section
  let sectorCardInterval;
  const sectorCardWrapper = document.querySelector(".sector-card-group-wrapper");
  const sectorCards = document.querySelector(".sector-card-group").children;
  
  let currentSectorCardIndex = 0;
  
  const scrollToSectorCard = (index) => {
    // Make sure the index does not go out of bounds.
    // Adding [sectorCards.length] because of js modulo giving negative.
    index = (index + sectorCards.length) % sectorCards.length;
    currentSectorCardIndex = index;
  
    const scrollLeftValue =
      sectorCards[index].offsetLeft - sectorCardWrapper.offsetLeft;
  
    sectorCardWrapper.scrollTo({ left: scrollLeftValue, behavior: "smooth" });
  };
  startSectorCardInterval();
  const sectorCardsLeftButton = document.getElementById(
    "industries-corousel-left-arrow"
  );
  sectorCardsLeftButton.addEventListener("click", () => {
    scrollToSectorCard(currentSectorCardIndex - 1);
    stopSectorCardInterval();
    startSectorCardInterval();
  });
  const sectorCardsRightButton = document.getElementById(
    "industries-corousel-right-arrow"
  );
  sectorCardsRightButton.addEventListener("click", () => {
    scrollToSectorCard(currentSectorCardIndex + 1);
    stopSectorCardInterval();
    startSectorCardInterval();
  });
  function startSectorCardInterval(){
    sectorCardInterval = setInterval(() => {
    scrollToSectorCard(currentSectorCardIndex + 1);
  }, 5000);
  }
  function stopSectorCardInterval(){
    clearInterval(sectorCardInterval);
  }
  
  