<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
        <title>${title}</title>
        % for x in css:
            <link rel="stylesheet" type="text/css" href="${x}" ></link>
        % endfor
        % for x in js:
            <script type="text/javascript" src="${x}" ></script>
        % endfor
    </head>
    <body id="application" class="application">
        <header>
            <div class="navbar-fixed">
                <ul id="dropdown-quickmenu" class="dropdown-content">
                    % for function, action, menu, icon, titlelabel in quickmenu:
                        <li>
                            <a
                                % if function:
                                    data-function="${function}"
                                % endif
                                % if action:
                                    data-action="${action}"
                                % endif
                                % if menu:
                                    data-menu="${menu}"
                                % endif
                                % if title:
                                    title="${titlelabel}"
                                % endif
                            >
                                <img class="responsive-img" src="${icon}"></img>
                            </a>
                        </li>
                    % endfor
                </ul>
                <ul id="dropdown-usermenu" class="dropdown-content">
                    % for function, icon, name in usermenu:
                        <li>
                            % if icon:
                                <img src="${icon}" class="left responsive-img"></img>
                            % endif
                                <a class="usermenu"
                                   data-function="${function}">${name}</a>
                        </li>
                    % endfor
                </ul>
                <nav>
                    <div class="nav-wrapper">
                        <ul class="left">
                            <li>
                                <a href="#" data-activates="slide-out" class="button-collapse">
                                    <i class="mdi-navigation-menu"></i>
                                </a>
                            </li>
                        </ul>
                        <ul class="left"> <!-- FIXME class="right" wait fix from materializecss -->
                            <li>
                                <a class="dropdown-button" data-activates="dropdown-quickmenu">
                                    <i class="mdi-action-view-module"></i>
                                </a>
                            </li>
                            <li>
                                <a class="dropdown-button" data-activates="dropdown-usermenu">Dropdown
                                    <i class="mdi-navigation-arrow-drop-down right"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                    <ul id="slide-out" class="side-nav fixed">
                        <img class="responsive-img" src="/login/logo"/>
                        ${add_menus(appmenu)}
                    </ul>
                </nav>
            </div>
        </header>
        <main>
            Plop
            <div class="row">
                <div class="col s1 m1 l1">
                    1
                </div>
                <div class="col s1 m1 l1">
                    2
                </div>
                <div class="col s1 m1 l1">
                    3
                </div>
                <div class="col s1 m1 l1">
                    4
                </div>
                <div class="col s1 m1 l1">
                    5
                </div>
                <div class="col s1 m1 l1">
                    6
                </div>
                <div class="col s1 m1 l1">
                    7
                </div>
                <div class="col s1 m1 l1">
                    8
                </div>
                <div class="col s1 m1 l1">
                    9
                </div>
                <div class="col s1 m1 l1">
                    10
                </div>
                <div class="col s1 m1 l1">
                    11
                </div>
                <div class="col s1 m1 l1">
                    12
                </div>
            </div>
        </main>
        <footer></footer>
        <!--
        <div id="body">
            <section id="application">
                <nav id="breadcrums">
                    <ul>
                    </ul>
                </nav>
                <div id="views">
                </div>
            </section>
        </div>
        -->
    </body>
</html>
<%def name="add_menus(menus)">
    % for function, action, menu, name , submenus, in menus:
        % if submenus:
            <li>
                <label for="input-${menu}">${name}</label>
                <input type="checkbox" id="input-${menu}" />
                    <ul>
                        ${add_menus(submenus)}
                    </ul>
            </li>
        % else:
            <li id="menu-${menu}" class="sheet">
                <a
                    % if function:
                        data-function="${function}"
                    % endif
                    % if action:
                        data-action="${action}"
                    % endif
                    % if menu:
                        data-menu="${menu}"
                    % endif
                    ><label>${name}<label></a>
            </li>
        % endif
    % endfor
</%def>
