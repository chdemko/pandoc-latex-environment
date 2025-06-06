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

    def test_empty(self):
        doc = EnvironmentTest.conversion(
            """\
---                           
pandoc-latex-environment:
  test: [class1, class2]
---
::: {.class1 .class2}
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
            """.strip(),
        )

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

    def test_div(self):
        doc = EnvironmentTest.conversion(
            """\
---                           
pandoc-latex-environment:
  test: [class1, class2]
---
::: {.class1 .class2}
::: {.class}
content
:::
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

    def test_itemize0(self):
        doc = EnvironmentTest.conversion(
            """\
---                           
pandoc-latex-environment:
  test: [class1, class2]
---
::: {.class1 .class2}
* a
* b
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

\\begin{itemize}
\\tightlist
\\item
  a
\\item
  b
\\end{itemize}

\\end{test}
            """.strip(),
        )

    def test_itemize1(self):
        doc = EnvironmentTest.conversion(
            """\
---                           
pandoc-latex-environment:
  test: [class1, class2]
---
::: {.class1 .class2}
* a
* b

Test
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

\\begin{itemize}
\\tightlist
\\item
  a
\\item
  b
\\end{itemize}

Test
\\end{test}
            """.strip(),
        )

    def test_itemize2(self):
        doc = EnvironmentTest.conversion(
            """\
---                           
pandoc-latex-environment:
  test: [class1, class2]
---
::: {.class1 .class2}
Test

* a
* b
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
Test

\\begin{itemize}
\\tightlist
\\item
  a
\\item
  b
\\end{itemize}

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
