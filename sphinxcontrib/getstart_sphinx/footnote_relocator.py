# -*- coding: utf-8 -*-

from docutils import nodes
from sphinx.transforms import SphinxTransform


class FootnoteVisitor(nodes.NodeVisitor):
    def __init__(self, document):
        self.footnotes = []
        nodes.NodeVisitor.__init__(self, document)

    def visit_section(self, node):
        for footnote in self.footnotes:
            footnote.parent.remove(footnote)
            index = node.parent.index(node)
            node.parent.insert(index, footnote)
        self.footnotes = []

    def depart_section(self, node):
        for footnote in self.footnotes:
            footnote.parent.remove(footnote)
            node += footnote
        self.footnotes = []

    def visit_footnote(self, node):
        self.footnotes.append(node)
        raise nodes.SkipNode

    def unknown_visit(self, node):
        pass

    def unknown_departure(self, node):
        pass


class FootnoteReloactor(SphinxTransform):
    """文中に登場する脚注を章末に移動する。"""
    default_priority = 100

    def apply(self):
        visitor = FootnoteVisitor(self.document)
        self.document.walkabout(visitor)


def setup(app):
    app.add_post_transform(FootnoteReloactor)
