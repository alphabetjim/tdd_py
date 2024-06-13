from flask import Flask, jsonify, request, render_template, url_for, redirect

from blog.commands import CreateArticleCommand
from blog.queries import GetArticleByIDQuery, ListArticlesQuery
from blog.models import Article

from pydantic import ValidationError

app = Flask(__name__)


@app.errorhandler(ValidationError)
def handle_validation_exception(error):
    response = jsonify(error.errors())
    response.status_code = 400
    return response


@app.route("/create-article/", methods=["POST"])
def create_article():
    cmd = CreateArticleCommand(
        **request.json
    )
    return jsonify(cmd.execute().dict())

@app.route("/create-article-form/", methods=["POST", "GET"])
def create_article_form():
    if request.method == "POST":
        # As input validation is handled on client side for this simple example,
        # we can assume that the form is always valid
        form_info = request.form.to_dict()
        print(form_info)
        article = Article(author=form_info["author"], title=form_info["title"], content=form_info["content"]).save()
        return redirect(url_for("get_article", article_id=article.id))
    else:
        return render_template("create_article.html")


@app.route("/article/<article_id>/", methods=["GET"])
def get_article(article_id):
    query = GetArticleByIDQuery(
        id=article_id
    )
    article_detail = query.execute().dict()
    return render_template("article_detail.html", article=article_detail)


@app.route("/article-list/", methods=["GET"])
def list_articles():
    query = ListArticlesQuery()
    records = [record.dict() for record in query.execute()]
    return render_template("article_list.html", articles=records)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()