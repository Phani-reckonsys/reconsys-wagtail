const showMoreBtn = document.querySelector(".ourwork-display .outline-btn");
const showMoreBtnText = document.querySelector(".ourwork-display .outline-btn h4");
let ourWorkCardVisibleCount = 8;
const ourWorkCards = document.querySelectorAll(".our-works-card");
function setOurWorksCardCount(count) {
  ourWorkCardVisibleCount = count;
  for (const [index, card] of ourWorkCards.entries()) {
    if (index < count) {
      card.classList.remove("hidecard");
      showMoreBtnText.textContent = "Show Less"
    } else {
      card.classList.add("hidecard");
      showMoreBtnText.textContent = "show more"
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
