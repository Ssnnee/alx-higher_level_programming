function translateHollo () {
  languageCode = $('INPUT#languageCode').val();
  $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
    $('DIV#hello').text(data.hello);
  });
}

$(function () {
  $('INPUT#btn_translate').click(function () {
    translateHollo();
  });
  $('INPUT#languageCode').keypress(function (e) {
    if (e.which === 13) {
      translateHollo();
    }
  });
});
