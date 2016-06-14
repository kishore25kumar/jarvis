/*global $, document */
/*jslint var:true */

(function () {
    "use strict";

    $(document).ready(function () {
        $("#textToSpeech").click(function () {
            var text = $("#textData").val();
            var data = { text: text };
            var success = function (response) {
                $("#responseAudio").attr("src", response);
                $("#responseAudio")[0].play();
            };

            $.ajax({
                type: "POST",
                url: "/text-to-speech",
                data: data,
                success: success
            });
        });
    });
})();