// fetches and lists the title for all movies in the list in the HTML tag UL#list_movies
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  if (status === 'success') {
    for (let movie in data.results) {
      $('ul#list_movies').append('<li>' + data.results[movie].title + '</li>');
    }
  }
});
