(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (payload, response) {
    if (response === 'success') {
      $('#hello').text(payload.hello);
    }
  });
})();
