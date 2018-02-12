sphinxcontrib-getstart-sphinx
=============================

``sphinxcontrib-getstart-sphinx`` is a collection of Sphinx extensions to
build `Sphinxをはじめよう 第2版 (Getting Started with Sphinx 2nd Edition)`__.

__ https://www.oreilly.co.jp/books/9784873118192/


This package provides following extensions:

``sphinxcontrib.getstart_sphinx.better_docref``
    Append section numbers to each ``:doc:`` references.

``sphinxcontrib.getstart_sphinx.column``
    Add ``column`` directive to note columns.

``sphinxcontrib.getstart_sphinx.footnote_relocator``
    Move footnote definitions to the bottom of each sections.

``sphinxcontrib.getstart_sphinx.glossary_decorator``
    Make terms of glossaries bold.

``sphinxcontrib.getstart_sphinx.oreilly_review_table``
    Convert tables in Re:VIEW output to original notation for
    O'Reilly Japan internal tools.


Usage
-----

To enable all extensions in this package, please add
``sphinxcontrib.getstart_sphinx`` to your ``extensions`` list in conf.py::

    extensions = ['sphinxcontrib.getstart_sphinx']

If you want to enable specific extensions individually, please add its
name to the list like bollow::

    extensions = ['sphinxcontrib.getstart_sphinx.better_docref',
                  'sphinxcontrib.getstart_sphinx.footnote_relocator']

Directives
----------

You can use following directives:

``column``
    A directive to note a column.  It takes a title of column as an argument,
    and also takes body of column as content block.

    Example::

        .. column:: SphinxとPythonのバージョンの関係

           バージョン1.5以降、Sphinxを動作させるには2.7もしくは3.4以上の
           Pythonが必要です。
           そのため、古いPythonがインストールされるCentOS 6.x系などのディスト
           リビューションでは、最新のSphinxが利用できません。


Settings
--------

You can configure following settings to arrange the behavior of the extension.

``section_numbers``:
    A dict for mapping docname to section number text.
    This is used by ``better_docref`` extension to build a link title
    for document reference.

    Example::

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
