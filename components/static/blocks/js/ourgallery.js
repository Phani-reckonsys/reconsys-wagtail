document
  .addEventListener("DOMContentLoaded", (event) => {
    gsap.registerPlugin(ScrollTrigger);
    console.log("test 2");

    const sections = document.querySelectorAll(".gallery-wrapper");

    // const anim = gsap.to(sections, {
    //   xPercent: -100 * (sections.length - 1),
    //   ease: "none",
    //   scrollTrigger: {
    //     trigger: ".life-at-reckonsys-main",
    //     start: "top top",
    //     // markers: true,
    //     pin: true,
    //     scrub: 1,
    //     // base vertical scrolling on how wide the container is so it feels more natural.
    //     end: () => "+=" + document.querySelector(".life-at-reckonsys-main").offsetWidth,
    //   },
    // });

    // for(let [index, section] of sections.entries)

    //     gsap.timeline({ repeat: -1 }).to(section, {
    //         x: 5000 * (),
    //         duration: 100,
    //         progress: 1,
    //         ease: "none",

    // });
sections.forEach( section => gsap.timeline({ repeat: -1 }).to(section, {
      scrollTo: 500,
      x: -5000,
      duration: 100,
      progress: 1,
      ease: "linear",
    }));

    // window.addEventListener("wheel", () => auto.kill());
  });
