// убираем общую обертки для всех страниц
const containerMDElem = document.querySelector(".container-md");
containerMDElem.classList.remove("container-md");

// слейдер
const sliderItemsElem = document.querySelectorAll(".index__slider_item");
const arrowLeftElem = document.querySelector(".index__slider_arrowLeft");
const arrowRightElem = document.querySelector(".index__slider_arrowRight");

let slider = [];

for (let i = 0; i < sliderItemsElem.length; i++) {
  slider[i] = sliderItemsElem[i];
  sliderItemsElem[i].remove();
}

console.log(slider);

let step = 0;
// отвечает за смещение изображения
let offset = 0;

function drowImg() {
  let div = document.createElement("div");
  div = slider[step];
  div.classList.add("index__slider_item");
  let wid = window.innerWidth;
  div.style.left = offset * wid + "px";
  // console.log(div);
  document.querySelector(".index__slider_items").appendChild(div);
  if (step + 1 == sliderItemsElem.length) {
    step = 0;
  } else {
    step++;
  }
  offset = 1;
}

// drowImg();
// drowImg();

function left() {
  const slider2 = document.querySelectorAll(".index__slider_item");
  let offset2 = 0;
  for (let i = 0; i < slider2.length; i++) {
    let wid = window.innerWidth;
    console.log(wid);
    slider2[i].style.left = offset2 * wid - wid + "px";
    offset2++;
  }
  setTimeout(() => {
    slider2[0].remove();
    drowImg();
  }, 1000);
}

drowImg();
drowImg();
// drowImg();

document.onclick = left;

// setInterval(() => {
//   left();
// }, 1000);
