$('.smooth').on('click', function (e) {
    e.preventDefault();

    // Store hash value.
    const hash = this.hash;

    // Fetch offset top
    const offset = $(hash).offset().top;

    $('html, body').animate({
        scrollTop: offset
    }, 1000, function () {
    });
});

$(function () {
    $("#id_date").datepicker({
        minDate: new Date()
    });
});