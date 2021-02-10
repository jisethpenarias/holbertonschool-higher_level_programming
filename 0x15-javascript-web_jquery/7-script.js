/* fetches the name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
The name must be displayed in the HTML tag DIV#character */

document.addEventListener('DOMContentLoaded', function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    type: 'GET',
    success: function (people) {
      // console.log(data);
      $('DIV#character').text(people.name);
    }
  });
});
