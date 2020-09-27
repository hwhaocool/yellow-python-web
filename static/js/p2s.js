//监控按钮点击事件，并且通过ajax 调用接口

$("#go-btn").click(function() {
    console.info("123");

    var protobuf_content = $("#id-p").val();

    var url = $("#interfaceUrl").text();

    $.ajax({
        url: url,
        type: "PUT",
        async: false,
        contentType: "application/json",
        dateType: "json",
        data: {
            "data": protobuf_content
        },
        success: function(data) {
            $("#id-s").val(data);
        }
    })
});