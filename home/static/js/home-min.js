const industriesLeftArrow=document.querySelector(".industries-corousel-left-arrow"),industriesRightArrow=document.querySelector(".industries-corousel-Right-arrow");let caseStudiesInterval;const carousalImageWrapper=document.querySelector(".case-study-card"),carousalContentWrapper=document.querySelector(".cards-wrapper"),carousalLeftArrow=document.querySelector(".caseStudies-left-arrow"),carousalRightArrow=document.querySelector(".caseStudies-right-arrow"),carouselIndicator=document.querySelectorAll(".indicator");let corouselIndex=0;const moveToCorouselIndex=e=>{corouselIndex=(e+3)%3;let r=corouselIndex%3*-100/3;carousalImageWrapper.style.transform=`translateX(${r}%)`,carousalContentWrapper.style.transform=`translateX(${r}%)`};function startCaseStudiesCarouselInterval(){caseStudiesInterval=setInterval((()=>{moveToCorouselIndex(corouselIndex+1)}),5e3)}function stopCaseStudiesCarouselInterval(){clearInterval(caseStudiesInterval)}let sectorCardInterval;startCaseStudiesCarouselInterval(),carousalRightArrow.addEventListener("click",(()=>{moveToCorouselIndex(corouselIndex+1),stopCaseStudiesCarouselInterval(),startCaseStudiesCarouselInterval()})),carousalLeftArrow.addEventListener("click",(()=>{moveToCorouselIndex(corouselIndex-1),stopCaseStudiesCarouselInterval(),startCaseStudiesCarouselInterval()}));const sectorCardWrapper=document.querySelector(".sector-card-group-wrapper"),sectorCards=document.querySelector(".sector-card-group").children;let currentSectorCardIndex=0;const scrollToSectorCard=e=>{e=(e+sectorCards.length)%sectorCards.length,currentSectorCardIndex=e;const r=sectorCards[e].offsetLeft-sectorCardWrapper.offsetLeft;sectorCardWrapper.scrollTo({left:r,behavior:"smooth"})};startSectorCardInterval();const sectorCardsLeftButton=document.getElementById("industries-corousel-left-arrow");sectorCardsLeftButton.addEventListener("click",(()=>{scrollToSectorCard(currentSectorCardIndex-1),stopSectorCardInterval(),startSectorCardInterval()}));const sectorCardsRightButton=document.getElementById("industries-corousel-right-arrow");function startSectorCardInterval(){sectorCardInterval=setInterval((()=>{scrollToSectorCard(currentSectorCardIndex+1)}),5e3)}function stopSectorCardInterval(){clearInterval(sectorCardInterval)}sectorCardsRightButton.addEventListener("click",(()=>{scrollToSectorCard(currentSectorCardIndex+1),stopSectorCardInterval(),startSectorCardInterval()}));