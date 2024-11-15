document.addEventListener('DOMContentLoaded', () => {
    const videoFeed = document.getElementById('videoFeed');
    const toggleSwitch = document.getElementById('toggleCameraSwitch');

    let isCameraActive = false;
    let intervalId = null;

    toggleSwitch.addEventListener('change', () => {
        if (toggleSwitch.checked) {
            // Start the camera feed
            intervalId = setInterval(() => {
                videoFeed.src = '/video_feed';  // Refresh the video feed every second
            }, 1000);
            isCameraActive = true;
        } else {
            // Stop the camera feed
            clearInterval(intervalId);
            videoFeed.src = '';  // Stop the video feed by clearing the src
            isCameraActive = false;
        }
    });
});
