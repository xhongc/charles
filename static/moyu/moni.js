$(document).ready(function () {

})
//moni
function onMouseMove(event, end) {
    const eyes = document.getElementsByClassName("eye");
    for (let i in eyes) {
        const eye = eyes[i];
        if (eye.style) {
            if (end) {
                eye.style.transform = "rotate(190deg)";
            } else {
                const {
                    x, y, width, height
                } = eye.getBoundingClientRect();
                const left = x + width / 2;
                const top = y + height / 2;
                const rad = Math.atan2(event.pageX - left, event.pageY - top);
                const degree = rad * (180 / Math.PI) * -1 + 180;
                eye.style.transform = "rotate(" + degree + "deg)";
            }
        }
    }
}

function moniTalk(content, times = 2) {
    xtip.tips(content, '#moni_msg', {
        bgcolor: '#FFFFFF',
        times: times,
        pos: 'r',
        color: 'black'
    })
}