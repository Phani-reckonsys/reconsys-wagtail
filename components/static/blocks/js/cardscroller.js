document.addEventListener("DOMContentLoaded", () => {
    const checks = document.querySelectorAll(".right");
    
    checks.forEach((check) => {
      if (check.classList.contains("active")) {
        console.log("working");
  
        let sectorCardInterval;
        const sectorCardWrapper = document.querySelector(".cardscroller-body");
        const sectorCards = document.querySelector(".engagement-cards-wrapper").children;
  
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
  
        const startSectorCardInterval = () => {
          sectorCardInterval = setInterval(() => {
            scrollToSectorCard(currentSectorCardIndex + 1);
          }, 5000);
        };
  
        const stopSectorCardInterval = () => {
          clearInterval(sectorCardInterval);
        };
  
        startSectorCardInterval();
  
        const sectorCardsLeftButton = document.querySelector(".carousal-outline-btn-left");
        if (sectorCardsLeftButton) {
          sectorCardsLeftButton.addEventListener("click", () => {
            scrollToSectorCard(currentSectorCardIndex - 1);
            stopSectorCardInterval();
            startSectorCardInterval();
          });
        }
  
        const sectorCardsRightButton = document.querySelector(".carousal-outline-btn-right");
        if (sectorCardsRightButton) {
          sectorCardsRightButton.addEventListener("click", () => {
            scrollToSectorCard(currentSectorCardIndex + 1);
            stopSectorCardInterval();
            startSectorCardInterval();
          });
        }
      }
    });
  });
  