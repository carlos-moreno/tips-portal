from flask import (
    Blueprint,
    render_template,
)

from portal.tips import get_all_tips, get_tips_by_tag, get_unique_tags

bp = Blueprint('tips', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/tag/<tag>')
def index(tag=None):
    """Render the main page displaying a list of programming tips.

    This view serves as the primary endpoint for displaying tips. It handles
    two URL routes: the root URL ('/'), which shows all tips, and a
    tagged URL ('/tag/<tag>'), which filters tips by a specific tag.
    It fetches the necessary data from the database and passes it to the
    'index.html.j2' template for rendering.

    Args:
        tag: (str, optional)
            The tag used to filter the tips. Defaults to None. If provided,
            the page will display only tips associated with this tag.

    Returns:
        Response
    """

    all_tags = get_unique_tags()

    if tag:
        tips_list = get_tips_by_tag(tag)
        page_title = f'Dicas com a tag: {tag}'
    else:
        tips_list = get_all_tips()
        page_title = 'Todas as Dicas'

    return render_template(
        'index.html.j2',
        tips=tips_list,
        all_tags=sorted(all_tags),
        title=page_title,
        active_tag=tag,
    )


def configure(app):
    """Registers the 'tips' blueprint with the main Flask application.

    This function serves as the entry point for integrating the 'tips' feature
    module into the application. It takes the main Flask app instance and
    attaches the 'tips' blueprint to it. Registering a blueprint makes all
    its associated routes (e.g., @bp.route('/')), error handlers, and other
    components active and accessible within the main application.

    This setup function is typically called from the application factory
    (`create_app`) to assemble the application from its modular parts.

    Args:
        app: Flask
            The instance of the main Flask application to which the blueprint
            will be registered.

    Returns:
        None
    """

    app.register_blueprint(bp)
