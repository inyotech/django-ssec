var dateFormat = 'ddd, MMM D, YYYY HH:mm:ss';

updateLocalTime();

var images = new Array(imageUrls.length);
var currentIndex = images.length-1;

imageUrls.forEach(function(url, index) {
    images[index] = new Image();
    images[index].onload = imageLoaded;
    images[index].src = url
});

var numLoaded = 0;

var animationDelay = 330;
var timerId = false;

function imageLoaded() {

    $('#progress').progressbar('value', ++numLoaded);

    if (numLoaded == images.length) {
        imageLoadComplete()
    }
}

function imageLoadComplete() {
    stop_animating();
    step(0);
    $('.loading').hide('slow');
    $('#weather #image-wrapper img').fadeIn('slow');
}

function stop_animating() {
    clearTimeout(timerId);
    timerId = false;
    $('#pause').button('disable');
    $('#step-backward, #play, #step-forward').button('enable');
}

function step(count) {

    function mod(n, m) {
        return ((n % m) + m) % m;
    }

    currentIndex += count;
    currentIndex = mod(currentIndex, images.length);

    var re = new RegExp(/image_(\d{4})_(\d{2})_(\d{2})_(\d{2})_(\d{2}).jpg/);
    var imageDate = re.exec(images[currentIndex].src);

    var date = moment.utc({y: imageDate[1], M: imageDate[2]-1, d: imageDate[3], h: imageDate[4], m: imageDate[5]});

    $('#image-time').html('Image Time: '+date.local().format(dateFormat));

    $('#progress').progressbar('value', currentIndex);

    $('#counter').text('Image: '+(currentIndex+1)+' of '+images.length);

    $('#weather #image-wrapper img').attr({
        'src': images[currentIndex].src,
        'width': '600px',
        'height': '450px'
    });

}

function isAnimating() {
    return timerId;
}

function animate() {
    $('#pause').button('enable');
    $('#step-backward, #play, #step-forward').button('disable');
    step(1);
    timerId = setTimeout(animate, animationDelay);
}

function updateLocalTime() {
    var date = moment();
    $('#local-time').html('Local Time: ' + date.format(dateFormat));
    setTimeout(updateLocalTime, 1000);
}

$('#step-backward').on('click', function() {
    step(-1);
});

$('#play').on('click', function() {
    animate();
});

$('#pause').on('click', function() {
    stop_animating();
});

$('#step-forward').on('click', function() {
    step(1);
});

$('#progress').progressbar({
   value: currentIndex,
   max: images.length-1
});

$('#step-backward').button();

$('#play').button();

$('#pause').button();

$('#step-forward').button();

$('#slider').slider({
    min: -1000,
    max: -25,
    value: -animationDelay,
    animate: true,
    change: function(event, ui) {
        animationDelay = -ui.value;
        if (isAnimating()) {
            stop_animating();
            animate();
        }
    }
});
$(document).tooltip({
    open: function(event, ui) {
        ui.tooltip.delay(1000).fadeTo(3000, 0);
    }
 });
