from views import monitor


def routes(app):
    app.router.add_get("/", monitor)