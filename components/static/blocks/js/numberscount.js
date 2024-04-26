const items = document.querySelectorAll(".stats");

// gsap.from(items, {
//   textContent: 0,
//   duration: 4,
//   ease: Power1.easeIn,
//   snap: { textContent: 1 },
//   stagger: 1,
//   // onUpdate: textContent.replace(/\B(?=(\d{3})+(?!\d))/g, ","),
// });

gsap.from(items, {
    scrollTrigger:{
        trigger: ".services-stats-section",
        start:"top center",
    },
  textContent: 0,
  duration: 2,
  ease: Power1.easeIn,
  snap: { textContent: 1 },
  stagger: 0.2,
  // onUpdate: textContent.replace(/\B(?=(\d{3})+(?!\d))/g, ","),
});