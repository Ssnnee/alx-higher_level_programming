$(function () {
  $('INPUT#btn_translate').click(function () {
    // languageCode = $('INPUT#language_code').val()
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('INPUT#language_code').val()}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
