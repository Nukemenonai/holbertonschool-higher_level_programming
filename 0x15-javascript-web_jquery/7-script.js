$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: function (data) {
      console.log(data);
      $('DIV#character').text(data.name);
    }
  });
});
