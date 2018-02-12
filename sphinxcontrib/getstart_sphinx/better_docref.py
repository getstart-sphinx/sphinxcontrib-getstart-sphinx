# -*- coding: utf-8 -*-

import os

from docutils import nodes
from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.transforms import SphinxTransform
from sphinx.util import docname_join
from sphinx.util.nodes import clean_astext


class doctitle(nodes.Inline, nodes.TextElement):
    """A node to represent ``@<title>{...}`` in Re:VIEW."""
    pass


doctitle_role = XRefRole(innernodeclass=nodes.inline)


class BetterDocRefTransform(SphinxTransform):
    """``:doc:`` によるドキュメント参照に章番号を付け加える。

    通常、Sphinx ではドキュメント参照は該当ドキュメントのタイトルに置き換わる。しかし、
    書籍では『第1章「Sphinxとは」では…』のように章番号をつけて参照することが多い。
    この Transform では、Re:VIEW 出力時にドキュメント参照をこのような章への参照リンク
    に置き換える。

    章への参照リンクの組み立ての際には、設定項目 ``section_numbers`` を参照してリンク
    文字列を組み立てる。 ``section_numbers`` はドキュメント名をキー、各ドキュメントの
    章番号を値とした、辞書データである。 ::

        section_numbers = {
            'ch01': '第1章',
            'ch02': '第2章',
            'ch03': '第3章',
            'ch04': '第4章',
            'ch05': '第5章',
            'ch06': '第6章',
            'appendix/references': '付録A',
            'appendix/builders': '付録B',
            'appendix/quickstart': '付録C',
            'appendix/texlive': '付録D',
            'appendix/make_sh': '付録E',
            'appendix/markdown': '付録F',
            'appendix/community': '付録G',
        }

    .. note::

       ``reviewbuilder`` では、ドキュメント参照を ``@<chap>{...}`` に置き換えるため、
       この Transform と似たような動作となる。しかし、Re:VIEW の ``@<chap>{...}`` は
       EPUB 形式に変換した場合は単なるテキストとなるため、Re:VIEW に変換する場合でも、
       この Transform は有効に働く。
    """
    default_priority = 1

    def apply(self):
        if self.app.builder.name != 'review':
            return

        for node in self.document.traverse(addnodes.pending_xref):
            if node['refdomain'] == 'std' and node['reftype'] == 'doc':
                title = self.get_title_for(node)
                self.replace_doc_by_refs(node, title)
            elif node['refdomain'] == '' and node['reftype'] == 'doctitle':
                title = self.get_doctitle_for(node)
                self.replace_doc_by_refs(node, title)

    def replace_doc_by_refs(self, node, title):
        if title:
            refuri = os.path.basename(node['reftarget'])
            refnode = nodes.reference('', '', name=title,
                                      refuri='%s.xhtml' % refuri)
            node.replace_self(refnode)

    def get_title_for(self, node):
        refdoc = node.get('refdoc', 'index')
        docname = docname_join(refdoc, node['reftarget'])
        if docname not in self.env.all_docs:
            return None
        else:
            title = clean_astext(self.env.titles[docname])
            sectnum = self.config.section_numbers.get(docname)
            if sectnum:
                return u"%s「%s」" % (sectnum, title)
            else:
                return title

    def get_doctitle_for(self, node):
        refdoc = node.get('refdoc', 'index')
        docname = docname_join(refdoc, node['reftarget'])
        if docname not in self.env.all_docs:
            return None
        else:
            return clean_astext(self.env.titles[docname])


def setup(app):
    app.add_config_value('section_numbers', {}, 'env')
    app.add_post_transform(BetterDocRefTransform)
    app.add_role('doctitle', doctitle_role)
