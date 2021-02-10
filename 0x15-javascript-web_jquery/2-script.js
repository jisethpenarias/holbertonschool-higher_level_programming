/* updates the text color of the HTML tag HEADER to red
(#FF0000) when the user clicks on the tag DIV#red_header */
document.addEventListener('DOMContentLoaded', function () {
  $('header').click(function () {
    $('DIV#red_header').css('color', '#FF0000');
  });
});
