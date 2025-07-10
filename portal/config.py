"""Settings module"""
import os

from dynaconf import Dynaconf, FlaskDynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="pamps",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    load_dotenv=True,
)

def configure(app):
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=HERE)