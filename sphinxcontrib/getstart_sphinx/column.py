# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst.directives.admonitions import Admonition
from sphinx.transforms import SphinxTransform


BLOCK_LEVEL_NODES = (
    nodes.literal_block,
    nodes.table,
)


class column(nodes.admonition):
    pass


class ColumnDirective(Admonition):
    """コラムを記述するディレクティブ、 ``column`` ディレクティブを提供する。

    ``column`` ディレクティブはコラムのタイトルを引数に指定し、コラムの本文を
    コンテンツパートに記述する。 ::

        .. column:: SphinxとPythonのバージョンの関係

           バージョン1.5以降、Sphinxを動作させるには2.7もしくは3.4以上の
           Pythonが必要です。
           そのため、古いPythonがインストールされるCentOS 6.x系などのディスト
           リビューションでは、最新のSphinxが利用できません。
    """
    node_class = column
    required_arguments = 1

    def run(self):
        self.options.setdefault('class', []).append(self.name)
        r = Admonition.run(self)
        r[0]['title'] = self.arguments[0]
        r[0]['name'] = self.name
        return r



def visit_column(self, node):
    if node['title']:
        node.insert(0, nodes.title(node['title'], node['title']))
    self.visit_admonition(node)


def depart_column(self, node):
    self.depart_admonition(node)


def review_visit_column(self, node):
    if any(node.traverse(lambda n: isinstance(n, BLOCK_LEVEL_NODES))):
        self.add_text('//raw[|html|<div class="column">]\n')
        header = '====='
    else:
        header = '=====[column]'

    if node['title']:
        self.add_text('%s %s\n' % (header, node['title']))
    else:
        self.add_text('%s\n' % header)


def review_depart_column(self, node):
    if any(node.traverse(lambda n: isinstance(n, BLOCK_LEVEL_NODES))):
        self.add_text('//raw[|html|</div>]\n\n')
    else:
        self.add_text('=====[/column]\n\n')


class ColumnTitleCollector(SphinxTransform):
    default_priority = 900  # after processing documents by Sphinx Domains

    def apply(self, **kwargs):
        std_domain = self.env.get_domain('std')
        for node in self.document.findall(column):
            for name in node['names']:
                if name not in std_domain.labels:
                    node_id = self.document.nameids[name]
                    std_domain.labels[name] = (self.env.docname, node_id, node['title'])


def setup(app):
    app.add_node(column,
                 html=(visit_column, depart_column),
                 latex=(visit_column, depart_column),
                 text=(review_visit_column, review_depart_column))
    app.add_directive('column', ColumnDirective)
    app.add_transform(ColumnTitleCollector)
