# -*- coding: utf-8 -*-


def setup(app):
    from sphinxcontrib.getstart_sphinx import better_docref
    from sphinxcontrib.getstart_sphinx import column
    from sphinxcontrib.getstart_sphinx import footnote_relocator
    from sphinxcontrib.getstart_sphinx import glossary_decorator
    from sphinxcontrib.getstart_sphinx import oreilly_review_table

    better_docref.setup(app)
    column.setup(app)
    footnote_relocator.setup(app)
    glossary_decorator.setup(app)
    oreilly_review_table.setup(app)
