




// window.addEventListener('load', function() {
//     const videoLoader = document.getElementById('video-loader');
//     const loaderVideo = document.getElementById('loader-video');
//     const finalLogo = document.getElementById('final-logo');
//     const consumeWiseText = document.getElementById('consume-wise');
//     const productsTitle = document.getElementById('products-title');
//     const titleSeparator = document.querySelector('.title-separator');
//     const imageBoxes = document.getElementById('image-boxes');
//     const body = document.body;
//     const hamburgerIcon = document.getElementById('hamburger-icon');  // Added hamburger icon

//     // Initially hide the hamburger icon
//     hamburgerIcon.style.opacity = '0';

//     // When the video ends
//     loaderVideo.addEventListener('ended', function() {
//         // Hide video and show logo immediately
//         videoLoader.style.transition = 'opacity 1s ease';
//         videoLoader.style.opacity = '0';

//         setTimeout(() => {
//             videoLoader.style.display = 'none'; // Hide video loader
//             finalLogo.style.opacity = '1';      // Show logo

//             // Animate logo shrinking and moving
//             finalLogo.style.animation = 'shrinkAndMoveLogo 1.5s forwards';

//             // After the animation completes, change the logo image
//             setTimeout(() => {
//                 finalLogo.src = '/finall2/CWW.png';  // Replace with the new image path

//                 body.style.backgroundColor = 'black'; // Switch background to black

//                 // Make consume-wise text visible
//                 consumeWiseText.style.opacity = '1';

//                 // Add animation to each letter of CONSUMEWISE
//                 const letters = consumeWiseText.querySelectorAll('span');
//                 letters.forEach((letter, index) => {
//                     letter.style.animation = `letterFadeIn 0.5s forwards ${index * 0.2}s`; // Apply delay for each letter
//                 });

//                 // Animate the line growing below the CONSUMEWISE title
//                 setTimeout(() => {
//                     titleSeparator.style.width = '100%'; // Grow the line from left to right
//                     titleSeparator.style.opacity = '1'; // Fade in the line

//                     // Show the products title after the line animation completes
//                     productsTitle.style.opacity = '1'; // Fade in the Health Products title

//                     // Show the image boxes after the products title fades in
//                     setTimeout(() => {
//                         imageBoxes.style.opacity = '1'; // Fade in image boxes

//                         // Show the hamburger icon after everything else is displayed
//                         setTimeout(() => {
//                             hamburgerIcon.style.opacity = '1'; // Fade in the hamburger icon
//                         }, 500); // Delay for the hamburger icon to appear

//                     }, 500); // Shortened delay before image boxes appear

//                 }, letters.length * 0.2 * 1000); // Delay for the CONSUMEWISE letters animation to complete



//             }, 1500); // Match this with the logo transition timing (1.5 seconds)
//         }, 1000); // Wait for the video to fade out
//     });

//     // Fallback for video error
//     loaderVideo.addEventListener('error', function() {
//         videoLoader.style.display = 'none';
//         finalLogo.style.opacity = '1';
//         consumeWiseText.style.opacity = '1';
//         titleSeparator.style.width = '100%'; // Show line if video fails
//         titleSeparator.style.opacity = '1'; // Fade in line if video fails
//         productsTitle.style.opacity = '1';
//         imageBoxes.style.opacity = '1'; // Fade in image boxes if video fails
//         hamburgerIcon.style.opacity = '1';  // Show hamburger icon if video fails
//     });

// });


// const hamburgerIcon = document.getElementById('hamburger-icon');
// const sidebar = document.getElementById('sidebar');

// // Show sidebar and hide hamburger on hover
// hamburgerIcon.addEventListener('mouseenter', function() {
//     sidebar.style.right = '0'; // Slide sidebar into view
//     hamburgerIcon.style.opacity = '0'; // Hide hamburger icon
// });

// // When the mouse leaves the sidebar, hide it and show the hamburger again
// sidebar.addEventListener('mouseleave', function() {
//     sidebar.style.right = '-250px';  // Slide sidebar out of view
//     hamburgerIcon.style.opacity = '1'; // Show hamburger icon again
// });





window.addEventListener('load', function() {
    const videoLoader = document.getElementById('video-loader');
    const loaderVideo = document.getElementById('loader-video');
    const finalLogo = document.getElementById('final-logo');
    const consumeWiseText = document.getElementById('consume-wise');
    const productsTitle = document.getElementById('products-title');
    const titleSeparator = document.querySelector('.title-separator');
    const imageBoxes = document.getElementById('image-boxes');
    const body = document.body;
    const hamburgerIcon = document.getElementById('hamburger-icon');

    // Initially hide the hamburger icon
    hamburgerIcon.style.opacity = '0';

    // When the video ends
    loaderVideo.addEventListener('ended', function() {
        videoLoader.style.transition = 'opacity 1s ease';
        videoLoader.style.opacity = '0';

        setTimeout(() => {
            videoLoader.style.display = 'none'; // Hide video loader
            finalLogo.style.opacity = '1'; // Show logo

            // Animate logo shrinking and moving
            finalLogo.style.animation = 'shrinkAndMoveLogo 1.5s forwards';

            // After the animation completes, change the logo image
            setTimeout(() => {
                finalLogo.src = '/static/images/CWW.png'; // Replace with the new image path
                body.style.backgroundColor = 'black'; // Switch background to black

                // Make consume-wise text visible
                consumeWiseText.style.opacity = '1';

                // Animate each letter of CONSUMEWISE
                const letters = consumeWiseText.querySelectorAll('span');
                letters.forEach((letter, index) => {
                    letter.style.animation = `letterFadeIn 0.5s forwards ${index * 0.2}s`;
                });

                // Animate the line growing below the CONSUMEWISE title
                setTimeout(() => {
                    titleSeparator.style.width = '100%'; // Grow the line
                    titleSeparator.style.opacity = '1'; // Fade in the line

                    // Show the products title after the line animation completes
                    productsTitle.style.opacity = '1';

                    // Show the image boxes after the products title fades in
                    setTimeout(() => {
                        imageBoxes.style.opacity = '1'; // Fade in image boxes

                        // Show the hamburger icon after everything else is displayed
                        setTimeout(() => {
                            hamburgerIcon.style.opacity = '1';
                        }, 500); // Delay for the hamburger icon to appear

                    }, 1000); // Delay before image boxes appear (increased timing to match your requirements)

                }, letters.length * 0.2 * 1000); // Delay for the CONSUMEWISE letters animation to complete

            }, 1500); // Match this with the logo transition timing (1.5 seconds)
        }, 1000); // Wait for the video to fade out
    });

    // Fallback for video error
    loaderVideo.addEventListener('error', function() {
        videoLoader.style.display = 'none';
        finalLogo.style.opacity = '1';
        consumeWiseText.style.opacity = '1';
        titleSeparator.style.width = '100%'; // Show line if video fails
        titleSeparator.style.opacity = '1'; // Fade in line if video fails
        productsTitle.style.opacity = '1';
        imageBoxes.style.opacity = '1'; // Fade in image boxes if video fails
        hamburgerIcon.style.opacity = '1'; // Show hamburger icon if video fails
    });
});

// Sidebar hover events
const hamburgerIcon = document.getElementById('hamburger-icon');
const sidebar = document.getElementById('sidebar');

// Show sidebar and hide hamburger on hover
hamburgerIcon.addEventListener('mouseenter', function() {
    sidebar.style.right = '0'; // Slide sidebar into view
    hamburgerIcon.style.opacity = '0'; // Hide hamburger icon
});

// When the mouse leaves the sidebar, hide it and show the hamburger again
sidebar.addEventListener('mouseleave', function() {
    sidebar.style.right = '-250px'; // Slide sidebar out of view
    hamburgerIcon.style.opacity = '1'; // Show hamburger icon again
});

// Initialize Owl Carousel
$(document).ready(function(){
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        loop: true,         // Enable infinite loop
        nav: true,          // Show navigation arrows
        margin: 10,         // Margin between items
        autoplay: true,     // Enable autoplay
        autoplayTimeout: 2000, // Set delay between auto scrolls
        autoplayHoverPause: true, // Pause on hover
        responsive: {
            0: {
                items: 1    // 1 item visible on small screens
            },
            600: {
                items: 2    // 2 items visible on medium screens
            },
            960: {
                items: 3    // 3 items visible on larger screens
            },
            1200: {
                items: 3    // 3 items visible on desktop
            }
        }
    });

    // Mousewheel animation for Owl Carousel
    owl.on('mousewheel', '.owl-stage', function(e) {
        if (e.originalEvent.deltaY > 0) {
            owl.trigger('next.owl');
        } else {
            owl.trigger('prev.owl');
        }
        e.preventDefault();
    });
});
