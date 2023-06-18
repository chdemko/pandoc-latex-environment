# Usage

To apply the filter, use the following option with pandoc:

~~~shell
$ pandoc --filter pandoc-latex-environment
~~~

## Explanation

In the metadata block, specific set of classes can be defined to surround HTML `div` tag by a LaTeX environment.

Thus,

~~~markdown
---                           
pandoc-latex-environment:
  test: [class1, class2]
---
::: {.class2 .class1}
content
:::
~~~

will be rendered in LaTeX format as

~~~
\begin{test}

content

\end{test}
~~~

