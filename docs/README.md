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
