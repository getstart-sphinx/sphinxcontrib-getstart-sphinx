# -*- coding: utf-8 -*-
"""
oreilly_review_table
~~~~~~~~~~~~~~~~~~~~

オライリー内部ツールに合わせて、Re:VIEW原稿の空白セルには ``.`` の代わりに
全角スペースを入れる。
"""

from docutils import nodes
from sphinx.writers.text import Cell, TextTranslator


def visit_entry(self, node):
    if len(node) == 0:
        # Fill full-width space for empty table cells
        self.entry = Cell()
        self.new_state(0)
        self.new_state(0)
        self.add_text('　')
        self.end_state()
    else:
        TextTranslator.visit_entry(self, node)


def setup(app):
    app.setup_extension('sphinxcontrib.reviewbuilder')

    from sphinxcontrib.reviewbuilder.writer import ReVIEWTranslator
    ReVIEWTranslator.visit_entry = visit_entry
