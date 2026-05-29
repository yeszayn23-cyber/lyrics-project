const audio = document.getElementById('myAudio');
const display = document.getElementById('lyricsDisplay');

// التوقيت بالثواني والكلمات اللي بغيتي تبان
const lyrics = [
    { time: 0, text: "أجي نتسامحو" },
    { time: 5, text: "منك مجاني نوم" },
    { time: 10, text: "أجي عندي نتسامحو" },
    { time: 15, text: "ويا كحلة العيون" }
];

audio.addEventListener('timeupdate', () => {
    let currentTime = audio.currentTime;
    
    // كنشوفو شكون هي الجملة اللي خاصها تبان دابا
    lyrics.forEach(item => {
        if (currentTime >= item.time && currentTime < item.time + 5) {
            display.innerText = item.text;
        }
    });
});
