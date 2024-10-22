#!/usr/bin/env python

"""
Pandoc filter for adding LaTeX environement on specific div.
"""
from __future__ import annotations

from panflute import (
    Div,
    Doc,
    Element,
    Para,
    Plain,
    RawBlock,
    RawInline,
    convert_text,
    run_filter,
)


def latex(
    elem: Element,
    environment: str,
    title: str,
    identifier: str,
) -> list[Element] | None:
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
    list[Element] | None
        A list of pandoc elements.
    """
    if identifier:
        label = f"\n\\label{{{identifier}}}"
    else:
        label = ""

    first = elem.content[0]
    while isinstance(first, Div):
        first = first.content[0]

    last = elem.content[-1]
    while isinstance(last, Div):
        last = last.content[-1]

    if isinstance(first, (Para, Plain)):
        first.content.insert(
            0,
            RawInline(f"\\begin{{{environment}}}{title}{label}\n", "tex"),
        )
        if isinstance(last, (Para, Plain)):
            last.content.append(RawInline(f"\n\\end{{{environment}}}", "tex"))
            return None
        return [elem, RawBlock(f"\\end{{{environment}}}", "tex")]
    if isinstance(last, (Para, Plain)):
        last.content.append(RawInline(f"\n\\end{{{environment}}}", "tex"))
        return [RawBlock(f"\\begin{{{environment}}}{title}{label}", "tex"), elem]

    return [
        RawBlock(f"\\begin{{{environment}}}{title}{label}", "tex"),
        elem,
        RawBlock(f"\\end{{{environment}}}", "tex"),
    ]


def prepare(doc: Doc) -> None:
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


def transform(elem: Element, doc: Doc) -> list[Element] | None:
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
    list[Element] | None
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


def main(doc: Doc | None = None) -> Doc:
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        pandoc document

    Returns
    -------
    Doc
        The modified pandoc document.
    """
    return run_filter(transform, doc=doc, prepare=prepare)


if __name__ == "__main__":
    main()
