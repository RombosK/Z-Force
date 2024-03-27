// allYouNeedisPost

let totalSum = document.querySelector(".allYouNeedisPost__totalSum").innerHTML;
let collectedSum = document.querySelector(
  ".allYouNeedisPost__collectedSum"
).innerHTML;
console.log(totalSum);
console.log(collectedSum);

totalSum = totalSum.replace(/[^0-9]/g, "");
collectedSum = collectedSum.replace(/[^0-9]/g, "");

console.log(totalSum);
console.log(collectedSum);

const percentages = ((collectedSum / totalSum) * 100).toFixed(2);

document.querySelector(".allYouNeedisPost__donationsProgress").style.width =
  percentages + "%";

const stillNeed = totalSum - collectedSum;
document.querySelector(".allYouNeedisPost__stillNeed").innerHTML =
  "Осталось собрать " + stillNeed;

const age =
  new Date().getFullYear() -
  document.querySelector(".allYouNeedisPost__age").innerHTML;

document.querySelector(".allYouNeedisPost__age").innerHTML = "Возраст: " + age;

// елемент слайдера, чтобы не отображь его при отсутствии фото
const sliderElem = document.querySelector(".allYouNeedisPost__slider");
// стрелки
const leftArrowElem = document.querySelector(
  ".allYouNeedisPost__slider_navLeft"
);
const rightArrowElem = document.querySelector(
  ".allYouNeedisPost__slider_navRight"
);
//  массив фото
const imagesElem = document.querySelectorAll(".allYouNeedisPost__slider_img");
// элемент для фобавления номера текущего фото
let numberElem = document.querySelector(".allYouNeedisPost__slider_navNumber");

let index = 0;

console.log(imagesElem);

// блокировка сладера при отсутствии фото
if (imagesElem.length < 1) {
  sliderElem.classList.add("allYouNeedisPost__slider_NotActive");
}

numberElem.textContent = index + 1 + " из " + imagesElem.length;
// начальное отображение первой фотографи
imagesElem[0].classList.remove("allYouNeedisPost__slider_imgHidden");

//  событие нажатие на стрелку вправо
rightArrowElem.addEventListener("click", () => {
  if (index >= imagesElem.length - 1) {
    imagesElem[index].classList.add("allYouNeedisPost__slider_imgHidden");
    index = 0;
    imagesElem[index].classList.remove("allYouNeedisPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  } else {
    imagesElem[index].classList.add("allYouNeedisPost__slider_imgHidden");
    index++;
    imagesElem[index].classList.remove("allYouNeedisPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  }
});

//  событие нажатие на стрелку влево
leftArrowElem.addEventListener("click", () => {
  if (index === 0) {
    imagesElem[index].classList.add("allYouNeedisPost__slider_imgHidden");
    index = imagesElem.length - 1;
    imagesElem[index].classList.remove("allYouNeedisPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  } else {
    imagesElem[index].classList.add("allYouNeedisPost__slider_imgHidden");
    index--;
    imagesElem[index].classList.remove("allYouNeedisPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  }
});

// function zoomIn() {

//   var image = document.querySelector('.allYouNeedisPost__slider_img ');
  
//   image.style.width = '200%';
//   image.style.height = '200%';
  
//   }
