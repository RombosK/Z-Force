const leftArrowElem = document.querySelector(".newsPost__slider_navLeft");
const rightArrowElem = document.querySelector(".newsPost__slider_navRight");

const imagesElem = document.querySelectorAll(".newsPost__slider_img");

let numberElem = document.querySelector(".newsPost__slider_navNumber");

let index = 0;

numberElem.textContent = index + 1 + " из " + imagesElem.length;

imagesElem[0].classList.remove("newsPost__slider_imgHidden");

rightArrowElem.addEventListener("click", () => {
  if (index >= imagesElem.length - 1) {
    imagesElem[index].classList.add("newsPost__slider_imgHidden");
    index = 0;
    imagesElem[index].classList.remove("newsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  } else {
    imagesElem[index].classList.add("newsPost__slider_imgHidden");
    index++;
    imagesElem[index].classList.remove("newsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  }
});

leftArrowElem.addEventListener("click", () => {
  if (index === 0) {
    imagesElem[index].classList.add("newsPost__slider_imgHidden");
    index = imagesElem.length - 1;
    imagesElem[index].classList.remove("newsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  } else {
    imagesElem[index].classList.add("newsPost__slider_imgHidden");
    index--;
    imagesElem[index].classList.remove("newsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  }
});
