// Initialize mobile menu
$(document).ready(function() {
    $('.button-collapse').sideNav();
    $('.dropdown-trigger').dropdown();

    // Update copyright year
    $('#year').text(new Date().getFullYear());

    // Handle navbar active state
    const currentPage = $(location).attr('pathname').replace(/^\/|\/$/g, '');
    $('.navlink').each(function() {
        const linkText = $(this).text().toLowerCase().replace(/\s+/g, '');

        if (currentPage === '') {
            $('li').removeClass('active');
            return $('li.default').addClass('active');
        }

        if (linkText.includes(currentPage)) {
            return $(this).addClass('active');
        }
    });

    // Initialize social share links
    const currentURL = window.location.href;
    $('.share').append(
        `<a href="https://www.facebook.com/sharer/sharer.php?u=${currentURL}" rel="noopener" target="_blank"><i class="fab fa-facebook-square" style="color: rgb(66,103,178);"></i></a>`,
        `<a href="https://x.com/intent/tweet?url=${currentURL}&text=" rel="noopener" target="_blank"><i class="fa-brands fa-x-twitter" style="color: #000000;"></i></a>`,
        `<a href="https://www.linkedin.com/shareArticle?mini=true&url=${currentURL}" rel="noopener" target="_blank"><i class="fab fa-linkedin" style="color: rgb(0,119,181);"></i></a>`
    );
});
