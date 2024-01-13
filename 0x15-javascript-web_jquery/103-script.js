function translateHello () {
  // languageCode = $('INPUT#language_code').val();
  $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('INPUT#language_code').val()}`, function (data) {
    $('DIV#hello').text(data.hello);
  });
}

$(function () {
  $('INPUT#btn_translate').click(function () {
    translateHello();
  });

  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translateHello();
    }
  });
});
