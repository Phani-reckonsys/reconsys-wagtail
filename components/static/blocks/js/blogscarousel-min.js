const carousalImageWrapper=document.querySelector(".carousal-image-wrapper"),carousalContentWrapper=document.querySelector(".carousal-content-wrapper"),carousalLeftArrow=document.querySelector(".carousal-left-arrow"),carousalRightArrow=document.querySelector(".carousal-right-arrow"),carouselIndicator=document.querySelectorAll(".indicator"),carouselDescription=document.querySelector(".numbering");let activeCorouselIndex=0;const changeCorousel=e=>{activeCorouselIndex=(e+3)%3;let r=activeCorouselIndex%3*-33.3;carousalImageWrapper.style.transform=`translateX(${r}%)`,carousalContentWrapper.style.transform=`translateX(${r}%)`,carouselIndicator.forEach((e=>{e.classList.remove("active")})),carouselIndicator[activeCorouselIndex].classList.add("active"),carouselDescription.innerHTML=`0${activeCorouselIndex+1}/03`};for(let[e,r]of carouselIndicator.entries())r.addEventListener("click",(()=>{changeCorousel(e)}));carousalRightArrow.addEventListener("click",(()=>{changeCorousel(activeCorouselIndex+1)})),carousalLeftArrow.addEventListener("click",(()=>{changeCorousel(activeCorouselIndex-1)})),setInterval((()=>changeCorousel(activeCorouselIndex+1)),4e3);