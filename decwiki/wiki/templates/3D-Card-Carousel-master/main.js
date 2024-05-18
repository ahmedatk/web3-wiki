
(function() {
    var rotate, timeline;

    rotate = function() {
        return $('.card:first-child').fadeOut(400, 'swing', function() {
            return $('.card:first-child').appendTo('.container').hide();
        }).fadeIn(400, 'swing');
    };

    $('.next').click(function() {
        return rotate();
    });
}).call(this);







$(document).on('change', '.file-input', function() {
        

  var filesCount = $(this)[0].files.length;
  
  var textbox = $(this).prev();

  if (filesCount === 1) {
    var fileName = $(this).val().split('\\').pop();
    textbox.text(fileName);
  } else {
    textbox.text(filesCount + ' files selected');
  }
});
