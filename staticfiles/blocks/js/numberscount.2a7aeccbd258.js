const items = document.querySelectorAll(".stats");

gsap.from(items, {
    scrollTrigger:{
        trigger: ".services-stats-section",
        start:"top center",
    },
  textContent: 0,
  duration: 2,
  ease: Power1.easeIn,
  snap: { textContent: 1 },
});