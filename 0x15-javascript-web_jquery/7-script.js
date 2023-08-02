// fetches the character name and displays in the HTML tag DIV#character
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, status) {
  if (status === 'success') {
    $('div#character').text(data.name);
  }
});
