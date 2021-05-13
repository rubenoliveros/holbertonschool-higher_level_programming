(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (payload, response) {
    if (response === 'success') {
      $('#character').text(payload.name);
    }
  });
})();
