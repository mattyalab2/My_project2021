var url = 'http://127.0.0.1:8000/LenOfImage';
/*
function load(url){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'text';
    var len = 0;
    xhr.onload = function () {
        if (xhr.readyState === xhr.DONE){
            if (xhr.status === 200) {
                console.log(xhr.response);
                console.log(xhr.responseText);
                len = Number(xhr.response.len);
            }
        }
    };
    xhr.send();
    return len;
}

var len = load(url);
*/
var len = 6;
var pics_src = [];
var num = -1;

function load_pics () {
    for (let i = 0; i < len; i++)
        pics_src.push("static/image/instagram/mattya_lab/" + i +　".jpg");
}

function slideshow_timer () {
    num = (num + 1) % len;
    document.getElementById("instapic").src=pics_src[num];
    setTimeout("slideshow_timer()", 10000);
}

load_pics();
slideshow_timer();
