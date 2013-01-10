function civx_new_tab(id, title, url, filter_resources) {
    id = id.replace(/[ \.\/:]/g, '_');
    if (id[0] != '#'){
        id = '#' + id;
    }

    if($(id).html() != null ) {
        $('#tabs').tabs('select', id);
    } else {
        $('#tabs').tabs('add', id, title);
        $.ajax({
            url: url,
            success: function(data) {
	        data = moksha.filter_resources(data);
                $(id, "#tabs").append(data);
             }
        });
    }
}

function civx_new_tab_iframe(id, title, url) {
    civx_new_tab(id, title, '/iframe?url=' + url);
}

function civx_new_widget_dialog(widget) {
    $('body').append($('<div/>').load('/widgets/' + widget + '?chrome=True'));
}

function civx_embed_widget_dialog(widget, args) {
    url = '/widgets/embed?chrome=True&iframe=True&url=/widgets/' + widget;
    if (args) url = url + args;
    $('body').append($('<div/>').load(url));
}

function resize_grid(grid, wrapper) {
    console.log("Resizing grid");
    $(grid).fluidGrid({example: wrapper});
}
