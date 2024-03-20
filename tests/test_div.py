# This Python file uses the following encoding: utf-8

from unittest import TestCase

from panflute import convert_text

import pandoc_latex_environment


class EnvironmentTest(TestCase):
    @classmethod
    def conversion(cls, markdown, fmt="markdown"):
        doc = convert_text(markdown, standalone=True)
        doc.format = fmt
        pandoc_latex_environment.main(doc)
        return doc

    def test_simple(self):
        doc = EnvironmentTest.conversion(
            """\
---                           
pandoc-latex-environment:
  test: [class1, class2]
---
::: {.class1 .class2}
content
:::
            """.strip(),
            "latex",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            """\
\\begin{test}

content

\\end{test}
            """.strip(),
        )

    def test_title(self):
        doc = EnvironmentTest.conversion(
            """\
---
pandoc-latex-environment:
  test: [class1, class2]
---
::: {.class1 .class2 title="My Title"}
content
:::
            """,
            "latex",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            """\
\\begin{test}{My Title}

content

\\end{test}
            """.strip(),
        )

    def test_title_complex(self):
        doc = EnvironmentTest.conversion(
            """
---
pandoc-latex-environment:
  test: ['class1', 'class2']
---
::: {.class1 .class2 title="**My Title**"}
content
:::
            """,
            "latex",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            """\
\\begin{test}{\\textbf{My Title}}

content

\\end{test}
            """.strip(),
        )

    def test_id(self):
        doc = EnvironmentTest.conversion(
            """\
---
pandoc-latex-environment:
  test: ['class1', 'class2']
---
::: {#id1 .class1 .class2}
content
:::
            """,
            "latex",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            """\
\\begin{test}
\\label{id1}

content

\\end{test}
            """.strip(),
        )
