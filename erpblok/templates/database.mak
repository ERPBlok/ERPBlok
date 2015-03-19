<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
        <link rel="stylesheet" type="text/css" href="/static/materialize-src/css/materialize.css">
        <link rel="stylesheet" type="text/css" href="/static/database.css">
        <script type="text/javascript" src="/static/jquery-2.1.3.min.js" ></script>
        <script type="text/javascript" src="/static/materialize-src/js/bin/materialize.min.js"></script>
        <script type="text/javascript" src="/static/database.js" ></script>
        <title>${title}</title>
    </head>
    <body data-twttr-rendered="true">
        <header>
            <nav>
                <div class="nav-wrapper">
                    <a href="#" data-activates="slide-out" class="button-collapse">
                        <i class="mdi-navigation-menu"></i>
                    </a>
                    <a href="#" class="brand-logo center">Database manager</a>
                </div>
                <ul id="slide-out" class="side-nav fixed">
                    <img class="responsive-img" src="/login/logo"/>
                    <li class="active" id="create">
                        <a class="waves-effect waves-teal">Create a new database</a>
                    </li>
                    <li id="drop">
                        <a class="waves-effect waves-teal">Drop an existing database</a>
                    </li>
                    <li>
                        <a class="waves-effect waves-teal" href="/">Close</a>
                    </li>
                </ul>
            </nav>
        </header>
        <main>
            <div class="row">
                <div class="col s12 m12 l9 offset-l3">
                    <div id="error" class="container hide error center-align">
                        The database already exist
                    </div>
                    <div id="create" class="container">
                        <div class="section">
                            <label for="database">Name of the database</label>
                            <input id="database" type="text" required/>
                        </div>
                        <div class="section">
                            <label for="login">Login of the administrator</label>
                            <input id="login" type="text" required/>
                        </div>
                        <div class="section">
                            <label for="password">Password of the administrator</label>
                            <input id="password" type="text" required/>
                        </div>
                        <a id="submit-create"
                           class="waves-effect waves-light btn right">Create</a>
                    </div>
                    <div id="drop" class="container hide">
                        <div id="section">
                            <div id="select">
                            </div>
                        </div>
                        <a id="submit-drop"
                           class="waves-effect waves-light btn right">Drop</a>
                    </div>
                </div>
            </div>
        </main>
        <footer></footer>
    </body>
</html>
