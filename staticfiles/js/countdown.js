function countdown(endTime) {
    const timerElement = document.getElementById('timer');
    const interval = setInterval(() => {
        const remaining = Date.parse(endTime) - Date.now();
        if (remaining <= 0) {
            clearInterval(interval);
            timerElement.innerHTML = 'Time\'s up!';
            localStorage.removeItem('endTime');
        } else {
            const minutes = Math.floor(remaining / 1000 / 60);
            const seconds = Math.floor((remaining / 1000) % 60);
            timerElement.innerHTML = `${minutes}:${seconds.toString().padStart(2, '0')}`;
            localStorage.setItem('endTime', endTime.toISOString());
        }
    }, 1000);
}

window.onload = () => {
    let endTime = localStorage.getItem('endTime');
    if (endTime) {
        endTime = new Date(endTime);
    } else {
        endTime = new Date(Date.now() + 1000 * 60 * 1);
        localStorage.setItem('endTime', endTime.toISOString());
    }
    countdown(endTime);
};
