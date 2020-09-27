//监控按钮点击事件，并且通过ajax 调用接口

$("#go-btn").click(function() {

    var in_url = $("#interface-url").val();
    var in_type = $("#interface-type").val();
    var in_desc = $("#interface-desc").val();
    var in_method = $("#interface-method").val();
    var in_request = $("#request-body").val();
    var in_reponse = $("#reponse-body").val();

    $.ajax({
        url: "/wiki/convert",
        type: "PUT",
        async: false,
        contentType: "application/json",
        accept: "application/json",
        // dateType: "json",
        data: {
            "url": in_url,
            "type": in_type,
            "desc": in_desc,
            "method": in_method,
            "request": in_request,
            "reponse": in_reponse
        },
        success: function(result) {
            var obj = JSON.parse(result);
            $("#id-s").val(obj.data);
        }
    });
});