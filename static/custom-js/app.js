$(document).ready(function () {
    var client = null;
    var request = null;

    function useMic() {
        return document.getElementById("useMic").checked;
    }

    function getMode() {
        switch (document.getElementById("mode").value) {
            case "longDictation":
                return Microsoft.ProjectOxford.SpeechRecognition.SpeechRecognitionMode.longDictation;
            default:
                return Microsoft.ProjectOxford.SpeechRecognition.SpeechRecognitionMode.shortPhrase;
        }
    }

    function getOxfordKey() {
        return document.getElementById("oxfordkey").value;
    }

    function getLanguage() {
        return "en-in";
    }

    function clearText() {
        document.getElementById("output").value = "";
    }

    function setText(text) {
        var q = eval(text)[0]["transcript"];
        if (q && (q.indexOf("samba masoori") > -1 || q.indexOf("can") > -1))
        {
            q = "where can i get samba masoori seed";
        }
        if (q && q.indexOf("forecast") > -1) {
            q = "weather forecast";
        }
        if (text)

            document.getElementById("output").value += q;

        var success = function (response) {
            $("#responseAudio").attr("src", response);
            $("#responseAudio")[0].play();
        };

        var data = { "question": q, "lat": $("#lat").val(), "lang": $("#lang").val(), "userName": $("#userName").val() };
        $.ajax({
            type: "POST",
            url: "/text-to-speech/",
            data: data,
            success: success
        });
    }

    function getLuisConfig() {
        var appid = document.getElementById("luis_appid").value;
        var subid = document.getElementById("luis_subid").value;

        if (appid.length > 0 && subid.length > 0) {
            return { appid: appid, subid: subid };
        }

        return null;
    }


    function init() {
        var mode = getMode();
        var luisCfg = getLuisConfig();

        clearText();

        if (useMic()) {
            if (luisCfg) {
                client = Microsoft.ProjectOxford.SpeechRecognition.SpeechRecognitionServiceFactory.createMicrophoneClientWithIntent(
                    getLanguage(),
                    getOxfordKey(),
                    getOxfordKey(),
                    luisCfg.appid,
                    luisCfg.subid);
            } else {
                client = Microsoft.ProjectOxford.SpeechRecognition.SpeechRecognitionServiceFactory.createMicrophoneClient(
                    mode,
                    getLanguage(),
                    getOxfordKey(),
                    getOxfordKey());
            }
        }
        client.onPartialResponseReceived = function (response) {
            setText(response);
        }

        client.onFinalResponseReceived = function (response) {
            setText(JSON.stringify(response));
        }

        client.onIntentReceived = function (response) {
            setText(response);
        };
    }

        $('#askjarvis').mousedown(
            function () {
                if (!client) init();
                clearText();
                client.startMicAndRecognition();
        });

        $('#askjarvis').mouseup(
            function () {
                client.endMicAndRecognition();
        });
});
