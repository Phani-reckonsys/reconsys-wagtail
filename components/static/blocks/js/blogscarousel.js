const carousalImageWrapper = document.querySelector(".carousal-image-wrapper");
const carousalContentWrapper = document.querySelector(".carousal-content-wrapper");

const carousalLeftArrow = document.querySelector(".carousal-left-arrow");
const carousalRightArrow = document.querySelector(".carousal-right-arrow");

const carouselIndicator =document.querySelectorAll(".indicator");
const carouselDescription = document.querySelector(".numbering");

let activeCorouselIndex = 0;
let blogsHeroInterval

const changeCorousel = (index) => {
    activeCorouselIndex = (index + 3) % 3;
    let translate = (activeCorouselIndex%3) * -33.3;
    carousalImageWrapper.style.transform = `translateX(${translate}%)`;
    carousalContentWrapper.style.transform = `translateX(${translate}%)`;

    carouselIndicator.forEach((indicator) => {indicator.classList.remove("active")});
    carouselIndicator[activeCorouselIndex].classList.add("active");

    carouselDescription.innerHTML = `0${activeCorouselIndex+1}/03`;
}
for(let [i, indicator] of carouselIndicator.entries()){
    indicator.addEventListener('click' , ()=> {
        changeCorousel(i);
        stopBlogsHeroInterval();
        startBlogsHeroInterval();
    })
  }
carousalRightArrow.addEventListener("click", ()=>{
    changeCorousel(activeCorouselIndex+1);
    stopBlogsHeroInterval();
    startBlogsHeroInterval();
})

carousalLeftArrow.addEventListener("click", ()=>{
    changeCorousel(activeCorouselIndex-1);
    stopBlogsHeroInterval();
    startBlogsHeroInterval();
})
startBlogsHeroInterval();
function startBlogsHeroInterval(){
    blogsHeroInterval = setInterval(() => changeCorousel(activeCorouselIndex + 1), 4000);
}

function stopBlogsHeroInterval(){
    clearInterval(blogsHeroInterval);
}
