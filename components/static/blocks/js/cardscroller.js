let screenwidth = window.innerWidth;
const outerWrapper = document.querySelector(".cardscroller-body").offsetWidth;
const innerWrappers = document.querySelectorAll(".engagement-cards-wrapper");
const innerWrappersCount = document.querySelectorAll(
  ".engagement-cards-wrapper"
).length;
console.log(screenwidth);
console.log(innerWrappers);
console.log(outerWrapper);

innerWrappers.forEach((innerWrapper, i) => {
  const cardScrollerButton = innerWrappers[
    i
  ].parentElement.parentElement.querySelector(".cardscroller-buttons");
  if (outerWrapper < innerWrapper.offsetWidth) {
    console.log("active");
    cardScrollerButton.classList.add("active");
  }
  const sectorCards = innerWrapper.children;
  const sectorCardWrapper = innerWrapper.parentElement;
  let currentSectorCardIndex = 0;
  const scrollToSectorCard = (index) => {
    // Make sure the index does not go out of bounds.
    // Adding [sectorCards.length] because of js modulo giving negative.
    index = (index + sectorCards.length) % sectorCards.length;
    currentSectorCardIndex = index;
    const scrollLeftValue =
      sectorCards[index].offsetLeft - sectorCardWrapper.offsetLeft;
    console.log(sectorCards[index].offsetLeft);
    console.log(sectorCardWrapper.offsetLeft);

    sectorCardWrapper.scrollTo({ left: scrollLeftValue, behavior: "smooth" });
    console.log(index);
  };
  let sectorCardInterval;
  const startSectorCardInterval = () => {
    sectorCardInterval = setInterval(() => {
      scrollToSectorCard(currentSectorCardIndex + 1);
    }, 5000);
  };

  const stopSectorCardInterval = () => {
    clearInterval(sectorCardInterval);
  };

  startSectorCardInterval();
  const sectorCardsLeftButton =
    innerWrapper.parentElement.parentElement.querySelector(
      ".carousal-outline-btn-left"
    );
  if (sectorCardsLeftButton) {
    sectorCardsLeftButton.addEventListener("click", () => {
      scrollToSectorCard(currentSectorCardIndex - 1);
      stopSectorCardInterval();
      startSectorCardInterval();
    });
  }

  const sectorCardsRightButton =
    innerWrapper.parentElement.parentElement.querySelector(
      ".carousal-outline-btn-right"
    );
  if (sectorCardsRightButton) {
    sectorCardsRightButton.addEventListener("click", () => {
      scrollToSectorCard(currentSectorCardIndex + 1);
      stopSectorCardInterval();
      startSectorCardInterval();
    });
  }
});
