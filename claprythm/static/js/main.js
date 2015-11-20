function goYoutubeURL(url) {
    if (url.indexOf("://") == -1) {
        url = "http://" + url;
    }

    var parser = document.createElement('a');
    parser.href = url;

    var video_id = "";

    if (parser.hostname == "youtube.com" || parser.hostname == "www.youtube.com") {
        var query = parser.search.substring(1);
        var vars = query.split('&');
        for (var i = 0; i < vars.length; i++) {
            var pair = vars[i].split('=');
            if (decodeURIComponent(pair[0]) == "v") {
                video_id = pair[1];
            }
        }
    }
    else if (parse.hostname == "youtu.be") {
        var path = parser.pathname;
        var vars = path.split('/');
        video_id = vars[0];
    }

    if (video_id  != "") {
        location.href = "/yt/" + video_id;
        return true;
    }

    return false;
}