// елемент слайдера, чтобы не отображь его при отсутствии фото
const sliderElem = document.querySelector(".newsPost__slider");
// стрелки
const leftArrowElem = document.querySelector(".newsPost__slider_navLeft");
const rightArrowElem = document.querySelector(".newsPost__slider_navRight");
//  массив фото
const imagesElem = document.querySelectorAll(".newsPost__slider_img");
// элемент для фобавления номера текущего фото
let numberElem = document.querySelector(".newsPost__slider_navNumber");

let index = 0;

console.log(imagesElem);

// блокировка сладера при отсутствии фото
if (imagesElem.length < 1) {
  sliderElem.classList.add("newsPost__slider_NotActive");
}

numberElem.textContent = index + 1 + " из " + imagesElem.length;
// начальное отображение первой фотографи
imagesElem[0].classList.remove("newsPost__slider_imgHidden");

//  событие нажатие на стрелку вправо
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

//  событие нажатие на стрелку влево
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
