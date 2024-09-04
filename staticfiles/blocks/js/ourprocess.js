document.addEventListener("DOMContentLoaded", () => {
  gsap.registerPlugin(ScrollTrigger);

  const ourjourneyCards = gsap.utils.toArray(".our-process-card");
  const ourjourneyCardsWidth = gsap.utils.toArray(".our-process-card-width");
  const ourjourneyWrapper = document.querySelector(".our-process-card-wrapper");
  const ourjourneyWidth = document.querySelector(".our-process-card-width");

  if (ourjourneyWrapper && ourjourneyWidth) {
    const { scrollWidth, clientWidth } = ourjourneyWrapper;
    const scrollRatio = Math.max((scrollWidth - clientWidth) / clientWidth, 0);

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
  }

  const sliderMarker = document.querySelector(".slider-marker");
  if (sliderMarker && ourjourneyWrapper) {
    gsap.to(sliderMarker, {
      width: "100%",
      scrollTrigger: {
        trigger: ourjourneyWrapper,
        start: "top left",
        end: "+=3000",
        scrub: 1,
      },
    });
  }

  const flag = document.querySelector(".indicator-flag");
  if (flag && ourjourneyWrapper) {
    gsap.to(flag, {
      left: "98%",
      scrollTrigger: {
        trigger: ourjourneyWrapper,
        start: "top left",
        end: "+=3000",
        scrub: 1,
      },
    });
  }
});
