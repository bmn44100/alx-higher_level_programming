// script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello
let url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url, function (data, status) {
  if (status === 'success') {
    $('div#sf_wind_speed').text(data.hello);
  }
});
