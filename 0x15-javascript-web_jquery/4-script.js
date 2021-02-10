/* toggles the class of the HTML tag HEADER when the user clicks on the tag DIV#toggle_header:
The HEADER tag must always have one class: red or green, never both in the same time, never empty.
If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
*/
document.addEventListener('DOMContentLoaded', function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
