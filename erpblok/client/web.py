from anyblok import Declarations
from anyblok._argsparse import ArgsParseManager
from anyblok.registry import RegistryManager
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response
from .common import logout


Declarations.Pyramid.add_route('web-client', '/web/client')


@Declarations.Pyramid.add_view('web-client')
def load_client(request):
    database = request.session.get('database')
    login = request.session.get('login')
    password = request.session.get('password')
    state = request.session.get('state')

    # SHORTCUT
    database = 'erpblok'
    request.session['database'] = database
    request.session.save()
    login = password = 'admin'
    state = 'connected'
    # \SHORTCUT

    if not(database and login and password and state == "connected"):
        logout(request)
        return HTTPFound(location=request.route_url('homepage'))

    try:
        registry = RegistryManager.get(database)
        assert registry.Web.Login.check_authentification(login, password)
    except:
        logout(request)
        return HTTPFound(location=request.route_url('homepage'))

    css = registry.Web.get_css()
    js = registry.Web.get_js()
    usermenu = registry.Web.get_user_menu(login)
    quickmenu = registry.Web.get_quick_menu(login)
    mainmenu = registry.Web.get_main_menu(login)
    menus = registry.Web.get_sub_menu(login)
    title = ArgsParseManager.get('app_name', 'ERPBlok')
    return render_to_response('erpblok:templates/client.mak',
                              {'title': title,
                               'css': css,
                               'js': js,
                               'mainmenu': mainmenu,
                               'quickmenu': quickmenu,
                               'usermenu': usermenu,
                               'menus': menus,
                               }, request=request)
