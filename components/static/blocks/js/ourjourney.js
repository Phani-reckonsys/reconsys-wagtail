document.addEventListener("DOMContentLoaded", (event) => {
  console.log("test");
  gsap.registerPlugin(ScrollTrigger);

  const ourjourneyCards = gsap.utils.toArray(".our-journey-card");
  const ourjourneyCardsWidth = gsap.utils.toArray(".our-journey-card-width");
  const ourjourneyWrapper = document.querySelector(".our-journey-card-wrapper");
  const ourjourneyWidth = document.querySelector(".our-journey-card-width");

  const { scrollWidth, clientWidth } = ourjourneyWrapper;
  console.log(scrollWidth);
  console.log(clientWidth);

  const scrollRatio = Math.max((scrollWidth - clientWidth) / clientWidth, 0);
  console.log(scrollRatio);
  gsap.to(ourjourneyWidth, {
    x: -scrollWidth + clientWidth,
    scrollTrigger: {
      trigger: ourjourneyWrapper,
      pin: true,
      scrub: 1,
      end: "+=3000",
      markers: false,
    },
  });
});
const sliderMarker = document.querySelector(".slider-marker");
const ourjourneyWrapper2 = document.querySelector(".our-journey-card-wrapper");
gsap.to(sliderMarker, {
  width: "100%",
  scrollTrigger: {
    trigger: ourjourneyWrapper2,
    start: "top left",
    end: "+=3000",
    scrub: 1,
  },
});
const flag = document.querySelector(".indicator-flag");
const ourjourneyWrapper3 = document.querySelector(".our-journey-card-wrapper");
gsap.to(flag, {
  left: "98%",
  scrollTrigger: {
    trigger: ourjourneyWrapper3,
    start: "top left",
    end: "+=3000",
    scrub: 1,
  },
});
