#!/usr/bin/env python

"""
Pandoc filter for adding LaTeX environement on specific div.
"""

from panflute import Div, RawBlock, convert_text, run_filter


def latex(elem, environment, title, identifier):
    """
    Generate the LaTeX code.

    Arguments
    ---------
    elem
        The current element
    environment
        The environment to add
    title
        The environment title
    identifier
        The environment identifier

    Returns
    -------
        A list of pandoc elements.
    """
    if identifier:
        label = "\n\\label{" + identifier + "}"
    else:
        label = ""

    return [
        RawBlock(f"\\begin{{{environment}}}{title}{label}", "tex"),
        elem,
        RawBlock(f"\\end{{{environment}}}", "tex"),
    ]


def prepare(doc):
    """
    Prepare the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # Prepare the definitions
    doc.defined = {}

    # Get the meta data
    meta = doc.get_metadata("pandoc-latex-environment")

    if isinstance(meta, dict):
        # Loop on all definitions
        for key, definition in meta.items():
            # Verify the definition
            if isinstance(definition, list):
                doc.defined[key] = frozenset(definition)


def transform(elem, doc):
    """
    Transform div element.

    Arguments
    ---------
    elem
        current element
    doc
        pandoc document

    Returns
    -------
        A list of pandoc elements or None.
    """
    if doc.format in ("latex", "beamer") and isinstance(elem, Div):
        classes = frozenset(elem.classes)

        # Loop on all fontsize definition
        for key, definition in doc.defined.items():
            # Are the classes correct?
            if classes >= definition:
                if "title" in elem.attributes:
                    escaped = elem.attributes["title"].translate(
                        str.maketrans({"{": r"\{", "}": r"\}", "%": r"\%"})
                    )
                    title = f"{{{convert_text(escaped, output_format='latex')}}}"
                else:
                    title = ""

                identifier = elem.identifier
                elem.identifier = ""

                return latex(elem, key, title, identifier)
    return None


def main(doc=None):
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        pandoc document

    Returns
    -------
        The modified pandoc document.
    """
    return run_filter(transform, doc=doc, prepare=prepare)


if __name__ == "__main__":
    main()
