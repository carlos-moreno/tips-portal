from flask import Flask

from portal.config import configure


def create_app():
    """Create and configure an instance of the Flask application.

    This function implements the Application Factory pattern, a best practice
    for structuring Flask applications. Using a factory helps avoid circular
    imports and makes the application more modular and testable, as different
    configurations can be passed in to create different app instances (e.g.,
    for production, development, or testing).

    The factory initializes the core Flask app and then calls the `configure()`
    function, which is responsible for registering all necessary blueprints
    and components. In this case, it registers the 'tips' blueprint, making
    its routes and functionalities available.

    Returns:
        Flask
    """

    app = Flask(__name__)
    configure(app)
    return app


app = create_app()
