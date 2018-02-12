# -*- coding: utf-8 -*-
"""
oreilly_review_table
~~~~~~~~~~~~~~~~~~~~

オライリー内部ツールに合わせて、Re:VIEW原稿の空白セルには ``.`` の代わりに
全角スペースを入れる。
"""

from docutils import nodes
from sphinx.writers.text import TextTranslator


def visit_entry(self, node):
    if len(node) == 0:
        # Fill single-dot ``.`` for empty table cells
        self.table[-1].append(u'　')
        raise nodes.SkipNode
    else:
        TextTranslator.visit_entry(self, node)


def setup(app):
    app.setup_extension('sphinxcontrib.reviewbuilder')

    from sphinxcontrib.reviewbuilder.writer import ReVIEWTranslator
    ReVIEWTranslator.visit_entry = visit_entry
