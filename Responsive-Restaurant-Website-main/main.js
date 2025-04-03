document.addEventListener("DOMContentLoaded", function () {
    generateQRCode(); // Automatically generate QR code on page load
});

function generateQRCode() {
    let qrCodeDiv = document.getElementById("qrcode");
    qrCodeDiv.innerHTML = ""; // Clear previous QR code

    let inputUrl = document.getElementById("urlInput").value || "https://example.com"; // Default URL
    new QRCode(qrCodeDiv, {
        text: inputUrl,
        width: 150,
        height: 150
    });
}
