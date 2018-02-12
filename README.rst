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

Settings
--------

You can configure the behavior of the extension.
