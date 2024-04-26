const showMoreBtn = document.querySelector(".ourwork-display .outline-btn");
let ourWorkCardVisibleCount = 8;
const ourWorkCards = document.querySelectorAll(".our-works-card");
function setOurWorksCardCount(count) {
  ourWorkCardVisibleCount = count;
  for (const [index, card] of ourWorkCards.entries()) {
    if (index < count) {
      card.classList.remove("hidecard");
    } else {
      card.classList.add("hidecard");
    }
  }
  console.log(count);
  console.log(ourWorkCards);
}

setOurWorksCardCount(8);
showMoreBtn.addEventListener("click", () => {
  if (ourWorkCardVisibleCount > 20) setOurWorksCardCount(8);
  else setOurWorksCardCount(50);
});
