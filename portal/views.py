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
    # Pega a lista de todas as tags únicas para exibir os botões de filtro
    all_tags = get_unique_tags()

    if tag:
        # Se uma tag foi passada na URL, busca as dicas por essa tag
        tips_list = get_tips_by_tag(tag)
        page_title = f'Dicas com a tag: {tag}'
    else:
        # Se nenhuma tag foi passada, busca todas as dicas
        tips_list = get_all_tips()
        page_title = 'Todas as Dicas'

    return render_template(
        'index.html.j2',  # Nome do seu arquivo de template
        tips=tips_list,
        all_tags=all_tags,
        title=page_title,
    )


# @bp.route("/tag")
# def detail(tag):
#     tips = get_tips_by_tag(tag)
#     if not post:
#         return abort(404, "Page not found")
#     return render_template("post.html.j2", tips=tips)


def configure(app):
    app.register_blueprint(bp)
