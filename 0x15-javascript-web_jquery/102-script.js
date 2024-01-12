$(function () {
  $('INPUT#btn_translate').click(function () {
    languageCode = $('INPUT#languageCode').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
