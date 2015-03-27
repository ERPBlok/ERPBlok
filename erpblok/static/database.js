$(document).ready(function(){
    var $create = $('li#create');
    var $drop = $('li#drop');
    var $error = $('#error');
    var $error2 = $('#error2');
    function goto_create () {
        $("div#create").removeClass('hide');
        $("div#drop").addClass('hide');
        $drop.removeClass('active');
        $create.addClass('active');
        $error.addClass("hide");
        $error2.addClass("hide");
        $("div#create #database").val("");
        $("div#create #login").val("admin");
        $("div#create #password").val("");
        $("div#create #password2").val("");
    }
    $create.click(function (event) {
        goto_create();
    });
    $drop.click(function (event) {
        $("div#create").addClass('hide');
        $("div#drop").removeClass('hide');
        $drop.addClass('active');
        $create.removeClass('active');
        $error.addClass("hide");
        $error2.addClass("hide");
        $.ajax({
            type: "POST",
            url:"/database/manager/list",
            data: {}})
        .done(function (html) {
            var $select = $("div#drop #select");
            $select.children().remove();
            $select.append(html);
        });
    });
    $("#submit-create").click(function (){
        $error.addClass("hide");
        $error2.addClass('hide');
        var database = $("div#create #database").val();
        var login = $("div#create #login").val();
        var password = $("div#create #password").val();
        var password2 = $("div#create #password2").val();
        if (password != password2) {
            $error2.removeClass('hide');
        } else if (database && login && password) {
            $.ajax({
                type: "POST",
                url:"/database/manager/create",
                data: {database: database, login: login, password: password}})
            .fail(function (xhr, status) {
                if (xhr.status == 403) {
                    $error.removeClass("hide");
                }
            })
            .done(function (url) {
                window.location = url;
            });
        }
    });
    $("#submit-drop").click(function (){
        var database = $("div#drop #select select").val();
        goto_create();
        if (database) {
            $.ajax({
                type: "POST",
                url:"/database/manager/drop",
                data: {database: database}});
        }
    });
});
