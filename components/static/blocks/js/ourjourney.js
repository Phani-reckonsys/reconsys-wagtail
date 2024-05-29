document.addEventListener("DOMContentLoaded", (event) => {
  console.log("test");
  gsap.registerPlugin(ScrollTrigger);

  const ourjourneyCards = gsap.utils.toArray(".our-journey-card");
  const ourjourneyWrapper = document.querySelector(".our-journey-card-wrapper");
  const { scrollWidth, clientWidth } = ourjourneyWrapper;
  const scrollRatio = Math.max((scrollWidth - clientWidth) / clientWidth, 0);

  gsap.to(ourjourneyWrapper, {
    xPercent:  - scrollRatio * 100,
    scrollTrigger: {
      trigger: ourjourneyWrapper,
      pin: true,
      scrub: 0.5,
      end: "+=" + (scrollRatio*clientWidth),
      start: "50% 50%",
      markers: false,
    },
  });
});
