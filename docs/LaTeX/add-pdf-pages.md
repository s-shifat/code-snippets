---
id: add-pdf-pages
aliases: []
tags: []
---

# Add Pdf Pages to a document
To include pages from a pdf to a document you can do:

```latex

\usepackage{pdfpages} % To include PDF pages

\begin{document}

...

\includepdf[pages=-]{yourfile.pdf} % The `pages=-` option includes all pages from the PDF


\end{document}


```
