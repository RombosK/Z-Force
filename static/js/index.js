// убираем общую обертки для всех страниц
const containerMDElem = document.querySelector(".container-md");
containerMDElem.classList.remove("container-md");

// слейдер

// контейнер для конвейа фотограций
const sliderLineElem = document.querySelector(".index__slider_items");
// Массив изображений
const sliderItemsElem = document.querySelectorAll(".index__slider_item");
// левая стрелка
const arrowLeftElem = document.querySelector(".index__slider_arrowLeft");
// правая стрелка
const arrowRightElem = document.querySelector(".index__slider_arrowRight");

// let slider = [];

// const widthWindow = window.innerWidth;
// let flag = true;

// смещаем конвейр на 100vw
// sliderLineElem.style.left = "-" + 100 + "vw";

// перезаписываем массив фото в массив
// for (let i = 0; i < sliderItemsElem.length; i++) {
//   slider[i] = sliderItemsElem[i];
//   sliderItemsElem[i].remove();
// }

// document.querySelector(".index__slider_items").innerHTML = "";

let activeImage = 0;

function slider() {
  for (let i = 0; i < sliderItemsElem.length; i++) {
    sliderItemsElem[i].classList.add("index__slider_item-opasity");
  }
  sliderItemsElem[activeImage].classList.remove("index__slider_item-opasity");
}

slider();

arrowRightElem.addEventListener("click", () => {
  if (activeImage >= sliderItemsElem.length - 1) {
    activeImage = 0;
  } else {
    activeImage++;
  }
  slider();
});
arrowLeftElem.addEventListener("click", () => {
  if (activeImage <= 0) {
    activeImage = sliderItemsElem.length - 1;
  } else {
    activeImage--;
  }
  slider();
});

setInterval(() => {
  if (activeImage >= sliderItemsElem.length - 1) {
    activeImage = 0;
  } else {
    activeImage++;
  }
  slider();
}, 3000);

// второй вариант
// const initSlider = () => {
//   let div = document.createElement("div");
//   div = slider[activeImage];
//   document.querySelector(".index__slider_items").append(div);

//   nextImageGenerate();
//   prevImageGenerate();
// };

// const nextImageGenerate = () => {
//   let nextImg = activeImage + 1;
//   if (nextImg >= slider.length) {
//     nextImg = 0;
//   }

//   let div = document.createElement("div");
//   div = slider[nextImg];
//   document.querySelector(".index__slider_items").append(div);
// };

// const prevImageGenerate = () => {
//   let prevImg = activeImage - 1;
//   if (prevImg < 0) {
//     prevImg = slider.length - 1;
//   }

//   let div = document.createElement("div");
//   // if (w) div.style.width = 0;

//   div = slider[prevImg];

//   // div.classList.add("index__slider_item");
//   document.querySelector(".index__slider_items").prepend(div);
// };

// initSlider();
// console.log(document.querySelector(".index__slider_items"));
// console.log(document.querySelectorAll(".index__slider_item"));

// const nextSlide = () => {
//   // if (!flag) return;
//   // flag = !flag;

//   activeImage++;
//   if (activeImage >= slider.length) {
//     activeImage = 0;
//   }
//   console.log(activeImage);

//   // document.querySelector(".index__slider_item").remove();

//   nextImageGenerate();

//   let asd = document.querySelectorAll(".index__slider_item");
//   // console.log(asd);

//   animate({
//     duration: 1000,
//     draw: function (progress) {
//       asd[0].style.width = widthWindow * (1 - progress) + "px";
//     },
//     removeElement: asd[0],
//   });
//   // console.log(asd);

// };

// const prevSlide = () => {
//   // if (!flag) return;
//   // flag = !flag;

//   activeImage--;
//   if (activeImage < 0) activeImage = slider.length - 1;

//   prevImageGenerate(true);

//   document.querySelector(".index__slider_item:last-child").remove();
//   prevImageGenerate(true);

//   // animate({
//   //   duration: 1000,
//   //   draw: function (progress) {
//   //     document.querySelector(".index__slider_item").style.width =
//   //       widthWindow * progress + "px";
//   //   },
//   //   timing: function (step) {
//   //     return step;
//   //   },
//   //   removeElement: document.querySelector(".index__slider_items:last-child"),
//   // });
// };

// arrowRightElem.addEventListener("click", nextSlide);
// arrowLeftElem.addEventListener("click", prevSlide);

// function animate({ duration, draw, removeElement }) {

//   let start = performance.now();

//   requestAnimationFrame(function animate(time) {
//     let step = (time - start) / duration;

//     if (step > 1) step = 1;

//     draw(step);

//     if (step < 1) {
//       requestAnimationFrame(animate);
//     } else {
//       removeElement.remove();
//     }
//   });
// }

// третий вариант
// отвечает за смещение изображения
// let offset = 0;

// function drowImg() {
//   let div = document.createElement("div");
//   div = slider[step];
//   div.classList.add("index__slider_item");
//   let wid = window.innerWidth;
//   div.style.left = offset * wid + "px";
//   // console.log(div);
//   document.querySelector(".index__slider_items").appendChild(div);
//   if (step + 1 == sliderItemsElem.length) {
//     step = 0;
//   } else {
//     step++;
//   }
//   offset = 1;
// }

// function left() {
//   const slider2 = document.querySelectorAll(".index__slider_item");
//   let offset2 = 0;
//   for (let i = 0; i < slider2.length; i++) {
//     let wid = window.innerWidth;
//     console.log(wid);
//     slider2[i].style.left = offset2 * wid - wid + "px";
//     offset2++;
//   }
//   setTimeout(() => {
//     slider2[0].remove();
//     drowImg();
//   }, 1000);
// }

// drowImg();
// drowImg();

// document.onclick = left;

// setInterval(() => {
//   left();
// }, 1000);
