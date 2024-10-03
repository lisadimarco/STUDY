(function() {
    let numButtonClicks = 0;

    function buttonClicked() {
        numButtonClicks += 1;
        document.getElementById("mainDiv").textContent = "Button Clicked times: " + numButtonClicks;
    }

    document.querySelector('#myButton').addEventListener('click', function() {
        document.querySelector('#myDiv').classList.toggle('hidden'); // Toggle visibility of an element
    });

    // Limit the number of images uploaded
    document.addEventListener('DOMContentLoaded', function() {
        const pictureInput = document.getElementById('dog-picture');

        pictureInput.addEventListener('change', function(event) {
            const files = event.target.files;

            if (files.length > 10) {
                alert('You can upload a maximum of 10 pictures.');
                event.target.value = ''; // Reset the input field if more than 10 files are selected
            }
        });

        const form = document.getElementById('survey-form');
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            alert('Your submission has been received!'); // Confirmation message

            // Additional form processing logic could go here
        });
    });
})();
