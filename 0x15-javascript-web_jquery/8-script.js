$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function (i, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
