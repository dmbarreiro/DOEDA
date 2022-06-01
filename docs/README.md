# How to use sphinx

Documentation is written using [reStructuredText](https://docutils.sourceforge.io/rst.html)
and built using [sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)

To build the documentation using sphinx follow these steps:

1. Move to the `docs/` folder

    ```bash
    cd docs
    ```

2. Use the makefile to build to html

    ```bash
    make html
    ```

Then, the built documentation is located in the `docs/build/html/`.
Documentation can also be built to pdf.

The raw documentation files (`.rst`) are located in the `docs/source/` folder.
Any file not located in that folder will note be complied in the documentation.
This file is a meta-guide that is not meant to be included in the main documentation.

## reStructuredText convetion

To contribute to the doucumentation, follow the convention for header levels:

- `#` with overline, for parts
- `*` with overline, for chapters
- `=` for sections
- `-` for subsections
- `^` for subsubsections
- `"` for paragraphs
