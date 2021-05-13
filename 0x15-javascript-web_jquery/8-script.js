(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (payload, response) {
    if (response === 'success') {
      const films = payload.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
})();
