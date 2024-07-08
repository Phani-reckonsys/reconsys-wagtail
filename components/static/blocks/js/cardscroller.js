let check = document.querySelector(".right");
if (check && check.id === "active"){
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
startSectorCardInterval();
const sectorCardsLeftButton = document.getElementById(
  "cardscroller-left-arrow"
);
sectorCardsLeftButton.addEventListener("click", () => {
  scrollToSectorCard(currentSectorCardIndex - 1);
  stopSectorCardInterval();
  startSectorCardInterval();
});
const sectorCardsRightButton = document.getElementById(
  "cardscroller-right-arrow"
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
}