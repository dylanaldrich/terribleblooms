// Handle responsive image loading
$(document).ready(function() {
    function loadResponsiveImage() {
        if ($(window).width() <= 450) {
            $('.page-header').css(
                'background-image',
                'url(' + mobileImageUrl + ')'
            );
        } else {
            $('.page-header').css(
                'background-image',
                'url(' + desktopImageUrl + ')'
            );
        }
    }

    // Load initial image
    loadResponsiveImage();

    // Update on window resize
    $(window).resize(loadResponsiveImage);
});