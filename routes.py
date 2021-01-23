from views import get, monitor


def routes(app):
    app.router.add_get("/", get)
    app.router.add_post("/monitor", monitor)