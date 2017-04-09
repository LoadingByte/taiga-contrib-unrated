(function(){
  setTimeout(function () {
    setInterval(addJoinButton, 1000);

    $(document).on("click", "#unrated_joinProject", function() {
        var projectTitle = window.location.pathname;
        projectTitle = projectTitle.replace('/project/','');
        projectTitle = projectTitle.replace('/','');

        var $button = $(this);

        $button.prop('disabled', true);

        if(projectTitle !== undefined && projectTitle !== null) {
            $.ajax({
                "method": "GET",
                "url": "/api/v1/unrated/join_project",
                "data": { "project": projectTitle },
                beforeSend: function (xhr) {
                    var token = localStorage.getItem("token").slice(1, -1);
                    xhr.setRequestHeader ("Authorization", "Bearer " + token);
                }
            }).fail(function() {
              alert("ALAMR! Es ist ein Fehler aufgetreten!");
              $button.prop('disabled', false);
            }).done(function( result ) {
              alert("Du bist erfolgreich beigetreten.");
              $button.remove();
            });
        }
    });
  }, 3000);
})();

function addJoinButton() {
  if($("#unrated_joinProject").length <= 0) {
    $(".track-buttons-container").append('<button class="track-button" style="margin-left: .75em;" id="unrated_joinProject"><span class="track-inner"><span>Projekt beitreten</span></span></button>');
  }
}
