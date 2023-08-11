$(document).ready(function() {
  const spans = document.querySelectorAll('.loader .m span');

  const colors = ['#ff9933', '#ffffff', '#008000']; // Orange, White, Green
  const duration = 2000; // Animation duration for each color

  let currentIndex = 0;

  anime({
    targets: spans,
    color: function() {
      return colors[currentIndex];
    },
    duration: duration,
    delay: function(el, i) {
      return i * duration;
    },
    loop: true,
    update: function(anim) {
      currentIndex = anim.currentTime % colors.length;
    }
  });
});



// #### Section ####

const parallax = document.getElementById("parallax");

// Parallax Effect for DIV 1
window.addEventListener("scroll", function () {
  let offset = window.pageYOffset;
  parallax.style.backgroundPositionY = offset * 0.7 + "px";
  // DIV 1 background will move slower than other elements on scroll.
});
