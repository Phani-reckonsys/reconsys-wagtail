// hero section
const categoryHeadings = document.querySelectorAll(
    ".herosection .category-heading > *"
  );
  const mainHeadings = document.querySelectorAll(
    ".herosection .main-heading > *"
  );
  const headingIndicator = document.querySelectorAll(
    ".hero-carousel-indicator-group > *"
  );
  
  let currentHeading = 0;
  
  const setActiveHeading = (index) => {
    currentHeading = (index + 3) % 3;
    categoryHeadings.forEach((entry) => entry.classList.remove("active"));
    mainHeadings.forEach((entry) => entry.classList.remove("active"));
    headingIndicator.forEach((entry) => entry.classList.remove("active"));
  
    categoryHeadings[currentHeading].classList.add("active");
    mainHeadings[currentHeading].classList.add("active");
    headingIndicator[currentHeading].classList.add("active");
  };
  
  setInterval(() => setActiveHeading(currentHeading + 1), 5000);

  setActiveHeading(currentHeading);
  
  //industries section corousel'
  
  const industriesLeftArrow = document.querySelector(
    ".industries-corousel-left-arrow"
  );
  const industriesRightArrow = document.querySelector(
    ".industries-corousel-Right-arrow"
  );
  
  // CaseStudies Section Corousel
  const carousalImageWrapper = document.querySelector(".case-study-card");
  const carousalContentWrapper = document.querySelector(".cards-wrapper");
  
  const carousalLeftArrow = document.querySelector(".caseStudies-left-arrow");
  const carousalRightArrow = document.querySelector(".caseStudies-right-arrow");
  
  const carouselIndicator = document.querySelectorAll(".indicator");
  
  let corouselIndex = 0;
  
  const moveToCorouselIndex = (index) => {
    corouselIndex = (index + 3) % 3;
    let translateX = ((corouselIndex % 3) * -100) / 3;
    carousalImageWrapper.style.transform = `translateX(${translateX}%)`;
    carousalContentWrapper.style.transform = `translateX(${translateX}%)`;
  };
  
  carousalRightArrow.addEventListener("click", () => {
    moveToCorouselIndex(corouselIndex + 1);
  });
  
  carousalLeftArrow.addEventListener("click", () => {
    moveToCorouselIndex(corouselIndex - 1);
  });
  
  setInterval(() => {
    moveToCorouselIndex(corouselIndex + 1);
  }, 5000);
  
  // Sector Cards Section
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
  
  const sectorCardsLeftButton = document.getElementById(
    "industries-corousel-left-arrow"
  );
  sectorCardsLeftButton.addEventListener("click", () => {
    scrollToSectorCard(currentSectorCardIndex - 1);
  });
  const sectorCardsRightButton = document.getElementById(
    "industries-corousel-right-arrow"
  );
  sectorCardsRightButton.addEventListener("click", () => {
    scrollToSectorCard(currentSectorCardIndex + 1);
  });
  
  setInterval(() => {
    scrollToSectorCard(currentSectorCardIndex + 1);
  }, 5000);
  