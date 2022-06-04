variavel = document.getElementById("form_input_button");

variavel.onclick = function efeito() {
   var e = document.getElementById("form_imput_button");
   e.style.animation = "rotate";
   setTimeout(function() {
      e.style.animation = "";
   }, 100);
}