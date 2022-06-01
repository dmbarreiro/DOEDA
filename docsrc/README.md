# How to use sphinx

Documentation is written using [reStructuredText](https://docutils.sourceforge.io/rst.html)
and built using [sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)

There are two folders used for the documentation:

- `docsrc/`: contains all the source files for the documentation
- `docs/`: contains the documentation, built in html. DO NOT MODIFY THESE FILES.

To build the documentation using sphinx follow these steps:

1. Move to the `docsrc/` folder

    ```bash
    cd docsrc
    ```

2. Use the makefile to build to html and move the built html files to the `docs/` folder.

    ```bash
    make github
    ```

Then, the built documentation is located in the `docsrc/_build/html/`.
Documentation can also be built to pdf.

The raw documentation files (`.rst`) are located in the `docsrc/` folder.
Any file not located in that folder will not be complied in the documentation.
This file is a meta-guide that is not meant to be included in the main documentation.

## reStructuredText convetion

To contribute to the doucumentation, follow the convention for header levels:

- `#` with overline, for parts
- `*` with overline, for chapters
- `=` for sections
- `-` for subsections
- `^` for subsubsections
- `"` for paragraphs