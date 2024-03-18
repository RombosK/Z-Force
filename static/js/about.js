const headerElem1 = document.querySelector('.header');
const headerHeight1 = headerElem1.offsetHeight;
// let headerHeight1 = localStorage.getItem("headerHeight");
console.log(headerHeight1);

// document.querySelector('.about').style['padding-top'] = `${headerHeight1}px`;

console.log(headerHeight1);


// this.sliderLine.style.transform = `translateX(${ -this.sliderWidth * this.slidIdx
//   }px)`;

function aboutOnHover() {
  document
    .querySelector(".about__buttonHistory")
    .classList.add("about__buttonHistoryActiv");

  document
    .querySelector(".about__buttonTarget")
    .classList.add("about__buttonTargetNotActiv");
}

function aboutOutHover() {
  document
    .querySelector(".about__buttonHistory")
    .classList.remove("about__buttonHistoryActiv");

  document
    .querySelector(".about__buttonTarget")
    .classList.remove("about__buttonTargetNotActiv");
}

// слайдер

class AboutSlider {
  // selector1 - выбор слайдера
  // selector2 - выбор текста к слайдеру

  constructor(selector1, selector2) {
    this.sliderEl = document.querySelector(selector1);
    this.sliderElText = document.querySelector(selector2);

    if (!this.sliderEl) {
      throw new Error("wrong selector");
    }
    if (!this.sliderElText) {
      throw new Error("wrong selector");
    }

    // коробка для слайдера
    this.sliderВох = this.sliderEl.querySelector(".about__item_imgBox");

    //  объект дял  сдвига ленты фотограйий
    this.sliderLine = this.sliderEl.querySelector(".about__item_imgLine");

    // создаем массив изображений в выбранном selector1
    this.slides = this.sliderLine.querySelectorAll(".about__item_img");

    // создаем массив навигационных точек в выбранном selector1
    this.dots = this.sliderEl.querySelectorAll(".about__dot");

    // создаем массив текста в выбранном selector2
    this.texts = this.sliderElText.querySelectorAll(".about__item_text");

    // индекс слайда
    this.slidIdx = 0;

    // ширина слайдера (нужно для перелистывания)
    this.sliderWidth = document.querySelector(
      ".about__item_imgBox"
    ).offsetWidth;
  }

  // нажатие на точку

  changImg() {
    this.sliderLine.style.transform = `translateX(${
      -this.sliderWidth * this.slidIdx
    }px)`;

    // смена активновного класа у точки
    this.dots.forEach((item) => {
      item.classList.remove("about__dot_activ");
    });
    this.dots[this.slidIdx].classList.add("about__dot_activ");

    // смена активновного класа у текста
    this.texts.forEach((text) => {
      text.classList.remove("about__item_text_active");
    });
    this.texts[this.slidIdx].classList.add("about__item_text_active");
  }

  abouInit() {
    this.dots.forEach((dot, index) => {
      dot.addEventListener("click", () => {
        this.slidIdx = index;

        this.changImg();
      });
    });

    setInterval(() => {
      if (this.slidIdx >= this.slides.length - 1) {
        this.sliderLine.classList.remove("about__item_imgLineTransition");
        this.slidIdx = 0;
      } else {
        this.sliderLine.classList.add("about__item_imgLineTransition");
        this.slidIdx++;
      }
      this.changImg();
    }, 4000);
  }

  //   шаг перелистывания
  // function rollSlider(slides, slidIdx, sliderWidth) {
  //   slides.style.transform = `translateX(${-slidIdx * sliderWidth}px)`;
  // }

  //   abouInit() {
  //     this.dots.forEach((dot, index) => {
  //       dot.addEventListener("click", () => {
  //         this.slidIdx = index;

  //         // смена активновного класа у фотографии
  //         this.slides.forEach((img) => {
  //           img.classList.add("about__item_img_hidden");
  //         });
  //         this.slides[this.slidIdx].classList.remove("about__item_img_hidden");

  //         // смена активновного класа у точки
  //         this.dots.forEach((item) => {
  //           item.classList.remove("about__dot_activ");
  //         });
  //         this.dots[this.slidIdx].classList.add("about__dot_activ");

  //         // смена активновного класа у текста
  //         this.texts.forEach((text) => {
  //           text.classList.remove("about__item_text_active");
  //         });
  //         this.texts[this.slidIdx].classList.add("about__item_text_active");

  //         console.log(this.slidIdx);

  //         console.log(this.dots);
  //         console.log(this.slides);
  //       });
  //     });
  //   }
}

const slider1 = new AboutSlider(".about__slider1", ".about__slider1_text");
const slider2 = new AboutSlider(".about__slider2", ".about__slider2_text");
const slider3 = new AboutSlider(".about__slider3", ".about__slider3_text");


slider1.abouInit();
slider2.abouInit();
slider3.abouInit();

