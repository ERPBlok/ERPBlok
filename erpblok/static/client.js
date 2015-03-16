$(document).ready(function(){
    var userMenu = new ERPBlok.UserMenu();
    var quickMenu = new ERPBlok.QuickMenu();
    var menus = new ERPBlok.Menus();
    var actions = new ERPBlok.ActionManager();

    var hashTagManager = new ERPBlok.HashTagManager()
    window.addEventListener("hashchange", function(e) {
        hashTagManager.changed(
            hashTagManager.toObject(e.newURL),
            hashTagManager.toObject(e.oldURL));
    });

    $("#toolbar li a.usermenu").click(function(e) {
        var func = e.currentTarget.dataset.function;
        userMenu.call_function(func);
    });
    $("#toolbar div.quickmenu a").click(function (e) {
        var func = e.currentTarget.dataset.function;
        var action = e.currentTarget.dataset.action;
        var menu = e.currentTarget.dataset.menu;
        var hash = {};
        if (func != undefined) {
            quickMenu.call_function(func);
        }
        if (action != undefined) {
            hash['action'] = action;
        }
        if (menu != undefined) {
            hash['menu'] = menu;
        }
        if (hash) {
            hashTagManager.update(hash);
        }
    });
    $("#toolbar a.mainmenu").click(function (e) {
        var id = e.currentTarget.id;
        hashTagManager.update({menu: id});
    });
    $("#menus nav li.sheet a").click(function (e) {
        var func = e.currentTarget.dataset.function;
        var action = e.currentTarget.dataset.action;
        var menu = e.currentTarget.dataset.menu;
        var hash = {};
        if (func != undefined) {
            quickMenu.call_function(func);
        }
        if (action != undefined) {
            hash['action'] = action;
            // clear breadcrums
        }
        if (menu != undefined) {
            hash['menu'] = menu;
        }
        if (hash) {
            hashTagManager.update(hash);
        }
    });

    // Change Menu
    function display_menu(newMenu, oldMenu) {
        menus.rpc('menusTree', {menu: newMenu}, function (res) {
            var mainmenu = res.mainmenu;
            var nodemenu = res.nodemenu;
            var activemenu = res.activemenu;
            if (mainmenu != undefined) {
                $("nav#toolbar ul li a.mainmenu.selected").removeClass('selected');
                $("nav#toolbar ul li a#" + mainmenu).addClass('selected');
                $("aside#menus nav").addClass('invisible');
                $("aside#menus nav#menu-" + mainmenu).removeClass('invisible');
                if (nodemenu != undefined) {
                    for (var i in nodemenu) {
                        var node = "aside#menus";
                        node += " nav#menu-" + mainmenu;
                        node += " li#menu-" + nodemenu[i];
                        node += " input#input-" + nodemenu[i];
                        $(node)[0].checked = true;
                    }
                    if (activemenu != undefined) {
                        $("aside#menus nav li.selected").removeClass('selected');
                        var node = "aside#menus";
                        node += " nav#menu-" + mainmenu;
                        node += " li#menu-" + activemenu;
                        $(node).addClass('selected');
                    }
                }
            }
        });
    }
    hashTagManager.onAdd('menu', display_menu);
    hashTagManager.onChange('menu', display_menu);

    // Change Action
    hashTagManager.onAdd('action', function (newAction) {
        actions.load(newAction);
    });

    // Apply current hashTag
    hashTagManager.changed(hashTagManager.toObject(window.location.hash), {});
});
