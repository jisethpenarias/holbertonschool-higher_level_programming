/* fetches and lists the title for all movies by using
this URL: https://swapi-api.hbtn.io/api/films/?format=json */

document.addEventListener('DOMContentLoaded', function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    dataType: 'json',
    success: function (films) {
      // console.log(data);
      $.each(films.results, function (index, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
