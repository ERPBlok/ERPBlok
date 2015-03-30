ERPBlok.ViewManager = ERPBlok.Model.extend({
    init: function(action) {
        this.action = action;
        this.$action = action.$el;
        this.$selector = $('<ul class="view-selector"></ul>');
        this.$selector.appendTo(action.$el);
        this.views = {};
        this.active_view = undefined;
        for (var i in action.value.views) {
            this.add(action.value.views[i]);
        }
        this.select_view(action.value.views[0].id);
    },
    add: function(view) {
        var self = this;
        var view = this.get_view_cls(view);
        var $navEl = view.getNavEl();
        $navEl.click(function (event) {
            self.select_view(event.currentTarget.id);
        });
        $navEl.appendTo(this.$selector);
        var $viewEl = view.getViewEl();
        $viewEl.addClass('hide');
        $viewEl.appendTo(this.$action);
        this.views[view.id] = {'$nav': $navEl, '$view': $viewEl, 'view': view};
    },
    get_view_cls: function(view) {
        if (ERPBlok.View[view.mode])
            return new ERPBlok.View[view.mode](this, view);
        return new ERPBlok.View(this, view);
    },
    select_view: function (view_id) {
        if (view_id == this.active_view) return;
        if (this.active_view) {
            this.views[this.active_view].$nav.removeClass('selected');
            this.views[this.active_view].$view.addClass('hide');
        }
        if (view_id) {
            this.active_view = view_id;
            this.views[view_id].$nav.addClass('selected');
            this.views[view_id].$view.removeClass('hide');
            this.views[view_id].view.render();
        }
    },
});
ERPBlok.View = ERPBlok.Model.extend({
    rpc_url: '/web/client/view',
    icon_url_selector: '/static/login-logo.png',  // TODO replace by other
    title_selector: 'undefined',
    class_name: 'view-undefined',
    init: function(viewManager, options) {
        this.viewManager = viewManager;
        this.id = options.id;
        this.$template = $(options.template);
        this.pks = options.primary_keys;
        this.fields = options.fields;
    },
    getNavEl: function(view_id) {
        var el = '<li id="' + this.id + '" title="' + this.title_selector + '">';
        el += '<img width="24" height="24" src="' + this.icon_url_selector + '">';
        el += '</img></li>';
        return $(el);
    },
    getViewEl: function() {
        var $el = $('<div id="' + this.id + '" class="view ' + this.class_name + '"></div>');
        this.$template.appendTo($el);
        this.$el = $el;
        return $el;
    },
    render: function() {
    },
});