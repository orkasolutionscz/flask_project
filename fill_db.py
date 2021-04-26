from mdblog.app import flask_app
from mdblog.models import db
from mdblog.models import Article

from loremipsum import get_sentences
import random

COUNT = 47


def create_article(num):
    title = "Article {:02d}".format(num)
    # nagenerovane vety jsou v LISTU, musime je spojit do stringu
    content = " ".join(get_sentences(random.randint(3, 9), True))
    article = Article(title=title, content=content)
    return article


# pro praci s DB potrebujeme aplikacni kontext
with flask_app.app_context():

    # jdeme v cyklu a vytvarime clanky
    for num in range(1, COUNT+1):
        article = create_article(num)
        db.session.add(article)
        db.session.commit()
        print("article #{:02d} created")
