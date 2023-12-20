document.addEventListener('DOMContentLoaded', function () {
    const video = document.getElementById('qr-video');
    const scanner = new Instascan.Scanner({ video: video });

    scanner.addListener('scan', function (content) {
        const confirmMessage = `넘어가시겠습니까?\nQR Code 내용: ${content}`;
        if (confirm(confirmMessage)) {
            window.open(content, '_blank');
        }
    });

    Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
            scanner.start(cameras[cameras.length - 1]);
        } else {
            console.error('No cameras found.');
        }
    }).catch(function (error) {
        console.error('Error accessing camera:', error);
    });
});
