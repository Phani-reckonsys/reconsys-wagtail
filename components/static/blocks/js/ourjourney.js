document.addEventListener("DOMContentLoaded", (event) => {
  console.log("test");
  gsap.registerPlugin(ScrollTrigger);

  const ourjourneyCards = gsap.utils.toArray(".our-journey-card");
  const ourjourneyWrapper = document.querySelector(".our-journey-card-wrapper");
  const { scrollWidth, clientWidth } = ourjourneyWrapper;

  // Check the difference between scroll width and window width.
  // If window is larger, set ratio to 0.
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
      // scroller: ".our-journey-card-container",
    },
  });

  // ScrollTrigger.create({
  //   trigger: ".our-journey-card-wrapper",
  //   start: "50% 50%",
  //   end: `+=${scrollRatio * clientWidth}`,
  //   pin: ".line-slider",
  //   // markers: true,
  // });

  // gsap.to(".line-slider", {
  //   pin: true,
  //   scrollTrigger: {
  //     trigger: ".our-journey-card-wrapper",
  //     pin: true,
  //     scrub: 0.5,
  //     start: "50% 50%",
  //     markers: true,
  //     // scroller: ".our-journey-card-container",
  //   },
  // });
});
