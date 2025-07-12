from flask import (
    Blueprint,
    render_template,
)

from portal.tips import get_all_tips, get_tips_by_tag, get_unique_tags

bp = Blueprint('tips', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/tag/<tag>')
def index(tag=None):
    """
    Renderiza a página de dicas.
    Se uma tag for fornecida, filtra as dicas por essa tag.
    Caso contrário, mostra todas as dicas.
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
    app.register_blueprint(bp)
