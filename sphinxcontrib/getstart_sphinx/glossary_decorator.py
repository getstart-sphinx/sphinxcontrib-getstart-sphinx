# -*- coding: utf-8 -*-


from docutils import nodes
from sphinx import addnodes
from sphinx.transforms import SphinxTransform


class GlossaryDecorator(SphinxTransform):
    """``glossary`` ディレクティブの用語部分を太字にする。"""
    default_priority = 100

    def apply(self):
        for node in self.document.traverse(addnodes.glossary):
            for item in node.traverse(nodes.definition_list_item):
                if len(item) == 2 and isinstance(item[0], nodes.term):
                    term = item[0].pop(0)
                    bold = nodes.strong()
                    bold += term
                    item[0].insert(0, bold)


def setup(app):
    app.add_transform(GlossaryDecorator)
