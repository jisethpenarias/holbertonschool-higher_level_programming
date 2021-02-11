/*  script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and
displays the value of hello from that fetch in the HTML’s tag DIV#hello.
The translation of “hello” must be displayed in the HTML tag DIV#hello */

document.addEventListener('DOMContentLoaded', function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
