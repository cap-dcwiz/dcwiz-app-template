from dcwiz_app_utils.cli import create_cli_main
from fastapi import FastAPI


def make_app():
    from .api import router_map
    from dcwiz_app_utils.app import config

    app = FastAPI()
    for prefix, router in router_map.items():
        app.include_router(router, prefix=prefix)

    return app


main = create_cli_main(make_app,
                       envvar_prefix="{{ cookiecutter.__project_slug.upper() }}",
                       default_config="config/config.toml",
                       )
