// Smooth scrolling effect
// Get the input element by its ID
function getPosition(e) {
            var square = document.getElementById('square');
            var point = document.getElementById('point');
            var verticalLine = document.querySelector('.verticalLine');
            var horizontalLine = document.querySelector('.horizontalLine');
            var rect = square.getBoundingClientRect();

            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;

            point.style.left = x + 'px';
            point.style.top = y + 'px';

            var relX = x / square.clientWidth;
            var relY = y / square.clientHeight;
             relX= 1-relX
             relY=1-relY

            // Log x and y coordinates to the console
            console.log('x:', x, 'y:', y);
            console.log('cx:', square.clientWidth, 'cy:', square.clientHeight);
            console.log('rx:', relX, 'ry:', relY);

            // Show the selected lines at the chosen point
            verticalLine.style.left = x + 'px';
            verticalLine.style.bottom = 0;
            verticalLine.style.height = square.clientHeight- y + 'px';
            verticalLine.style.display = 'block';


            horizontalLine.style.top = y + 'px';
            horizontalLine.style.right = 0;
            horizontalLine.style.width = square.clientWidth - x +'px';
            horizontalLine.style.display = 'block';

            // Adjust coordinates based on the position within the square
            if (relY === 0) {
                relY = 0;
            } else if (relY === 1) {
                relY = 1;
            }

            // Sending relative coordinates to Flask using AJAX (you can use fetch API or other methods)
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/coordinate');
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({ x: relX, y: relY }));
        }





document.addEventListener('DOMContentLoaded', function() {
    const minutesInput = document.getElementById('minutesInput');
    if (minutesInput) {
        minutesInput.placeholder = 'Type how much \ud83d\udd52 in minutes?';
    } else {
        console.error("Element with ID 'minutesInput' not found.");
    }
     minutesInput_1 = document.getElementById('minutesInput_1');

// Set the placeholder text including the clock emoji
minutesInput_1.placeholder = 'Type how much \ud83d\udd52 in minutes?';
});
 // This represents the clock emoji (🕒)



document.addEventListener('DOMContentLoaded', function() {
  const withCameraImage = document.getElementById('withCamera');
  const minutesInput = document.getElementById('minutesInput');
  const withoutCameraImage = document.getElementById('withoutCamera');
  const minutesInput_1 = document.getElementById('minutesInput_1');

  withCameraImage.addEventListener('click', function() {

    minutesInput.focus();
  });
    withoutCameraImage.addEventListener('click', function() {

    minutesInput_1.focus();
  });
});

document.addEventListener("DOMContentLoaded", function() {
    var video = document.getElementById("myVideo");


     // Listen for the 'ended' event and replay the video

     video.addEventListener("ended", function() {
      video.currentTime = 0; // Reset video to the beginning
      video.play(); // Play the video again
    });
    var video_1 = document.getElementById("myVideo_1");


     // Listen for the 'ended' event and replay the video

     video_1.addEventListener("ended", function() {
      video_1.currentTime = 0; // Reset video to the beginning
      video_1.play(); // Play the video again
    });

    var video_2 = document.getElementById("myVideo_2");


     // Listen for the 'ended' event and replay the video

     video_2.addEventListener("ended", function() {
      video_2.currentTime = 0; // Reset video to the beginning
      video_2.play(); // Play the video again
    });


     // Listen for the 'ended' event and replay the video

     video_2.addEventListener("ended", function() {
      video_2.currentTime = 0; // Reset video to the beginning
      video_2.play(); // Play the video again
    });

});


    document.querySelectorAll('.scroll-link').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            window.scrollTo({
                top: targetSection.offsetTop,
                behavior: 'smooth'
            });
        });
    });

function handleClick(img, imageId) {
  if (!img.classList.contains('clicked')) {
    // If the image is not already clicked, toggle the 'clicked' class and send the info
    toggleClicked(img); // Toggle the 'clicked' class for the clicked image
    sendInfo(imageId); // Call the sendInfo function with the specified imageId
  }
}
function toggleClicked(img) {
  // Remove 'clicked' class from all images before adding it to the clicked image
  const images = document.querySelectorAll('.image-container-convert img');
  images.forEach((image) => {
    image.classList.remove('clicked');
  });

  img.classList.add('clicked'); // Add 'clicked' class to the clicked image
}
function sendInfo(imageId) {
    // Send an HTTP request to Flask when the image is clicked
    fetch('/handle_image_info' , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ imageId: imageId })
    })
    .then(response => {
        // Handle the response if needed
        console.log('Information sent for Image ' + imageId);
    })
    .catch(error => console.error('Error:', error));
}


function openMultipleLinks() {
  var links = [
    'https://github.com/menithecoder?tab=repositories',
    'https://menachemle.wixsite.com/my-site-2',
    'https://meni-the-coder.itch.io/destroy-hamas-hard'
    // Add more URLs to this array as needed
  ];
 function openLink(index) {
    if (index < links.length) {
      var newWindow = window.open(links[index]);
      if (newWindow) {
        newWindow.focus();
        setTimeout(function () {
          openLink(index + 1);
        }, 1000); // Change the delay time (in milliseconds) if needed
      } else {
        alert('Popup blocked! Please enable popups for this site to open the links.');
      }
    }
  }

  openLink(0);
}

function toggleClicked(img) {
  img.classList.toggle('clicked'); // Toggle the 'clicked' class on the clicked image
}

