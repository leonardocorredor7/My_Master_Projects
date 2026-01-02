# LEARNING


- [YAML](#yaml)
- [HTML pages](#html-pages)
- [Code Chunks](#code-chunks)
- [Markdown Linebreaks](#markdown-linebreaks)
- [Pipe](#pipe)
- [Grouping](#grouping)

Use the opportunity in this Homework Project to learn a bit more about
some concepts and tools used here.

## YAML

*What is the YAML?* The **YAML** is all text between `---` at the very
beginning of the file and the next `---` some lines below.

[YAML](https://en.wikipedia.org/wiki/YAML) is a specification language
used for configuration information. Quarto uses it to store and read
meta-data of files. In `Project_NYCFlights.qmd` it specifies `title:`
and `author:` and specification for rendering HTML files. In this case,
it specifies that a standalone HTML should be produced with all figures
and style files embedded, and the code should be folded in the output
HTML.

We do not learn details about YAML now, but two things are good to know:
(i) YAML uses whitespace indentation to structure information (similar
to python and different from R). Test it: Make one space before
`author:` and try to render, it will fail! Remove it and it is fine
again. (ii) `#` marks the beginning of a comment after it. This text
will be ignored while rendering (just like comments in R and python).

You can do a lot of design changes by specifying different things in the
YAML. Quarto will then give your output a different look. You find a lot
of this in the [quarto](http://quarto.org)-documentation. Read the [Get
started Tutorial:
Authoring](https://quarto.org/docs/get-started/authoring/rstudio.html).

Make a test: Add a line after the `code-fold:` line. Write
`number-sections: true` and make sure that you have whitespaces before
such that it matches the line above. Render, and see that headlines are
numbered now! (Want to play more: Try `toc: true` and guess what *toc*
means.)

## HTML pages

*Why standalone and embedded?* Typically, a HTML file has only the text
and semantic structure. Design specifications are in .css-files and
figures are independent files in a subdirectory.

Test it: change `embed-resources: true: true` to
`embed-resources: false` and render. You see: Now a subdirectory
`Project_NYCFlights_files` is created, but the output file in your
browser looks the same. Put it back to `true` and render again, the
folder will be removed. There are pro’s and con’s for both. An embedded
HTML is nice because it is one file, you can email it and the recipient
can view it. If you send the HTML file without embedded figures, the
recipient will not see figures. However, if you create a collection of
HTML files then many will use the same specification and embedding it in
each HTML-file will be a waste of space! (Compare the HTML-file size
with and without embedding.) If you commit your HTML file, such that
instructors can see your progress in the output resource (next task)
then all files need to be added and committed! With embedded resources
this is easier – just one file. So, it is a good solution for a one-file
HTML report. [Read
more.](https://quarto.org/docs/output-formats/html-basics.html#self-contained)

## Code Chunks

A code chunk starts with ```` ```{r} ```` and ends with ```` ``` ````.
Everythings inbetween is treated as `R` code when you render the Quarto
Markdown file it with `quarto render`. Whenever the code produces some
output, either output in the Console or graphics in the Plots tab, this
will appear in the rendered document. (Later we will also use Quarto
with `python` code, so chunks will appear as ```` ```{python} ````.)

The lines starting with `#|` are naturally treated as comments in `R`
and `python` and ignored. However, because of the `|`, `quarto` will
read them as *chunk options* or *cell attributes*. You see the chunk
options for `label` and `message` in the chunk. Play with it! Try how
the output looks when `message: true`. Read more about what other
options are available in the [Quarto References: Code Cells:
Knitr](https://quarto.org/docs/reference/cells/cells-knitr.html). (Knitr
is the R package used by quarto for dynamic document generation. [Code
Cells:
jupyter](https://quarto.org/docs/reference/cells/cells-jupyter.html)
similar but not that many options are available.) Try what `echo: false`
would do!

⚠️ **quarto runs code in a different environment!**  
That means, all dataframes, variables, and packages you have loaded to
work with in the Console are not available to `quarto` when it executes
the code while rendering the document! That is why we typically start
with a chunk loading packages and data. You can think of rendering as
quarto opening a new R session without anything loaded than base R. We
need to specify everything in the document. This is how it should be for
*reproducible research*! If `quarto` could access what is in your
Console environment, we could not re-render the code when we (or someone
else who clones our repository) opens it in a new R session.

Note: Reproducibility can be further imporved by specifying which
version of R and which packages are used. This is beyond our scope. In
the end, reproducibility is an important technical but also *social*
concept in a (research) community of practice.

## Markdown Linebreaks

Linebreaks in your Markdown file do not appear as such in your output
document! It works in the following way:

    A sentence like this 
    is two lines of code but will be one paragraph in the output. 

Line breaks in the output are dynamic, depending on the window size.

    Only when you put an extra line between two lines ... 

    There will be two paragraphs.  

Try it with an example sentence in your Markdown document!

But  
how  
can I  
write  
a paragraph  
with  
linebreak?

The secret is: Make two spaces at the end of the line you want to break!
Try it.

## Pipe

Since R version 4.1 There is a pipe operator in base-R `|>`. In earlier
versions there is none, but there was already the pipe operator `%>%`
from the package `magrittr` which is part of the `tidyverse` though not
in the tidyverse core. Code you find on the internet may often use `%>%`
instead of `|>`. There are only minor differences between the two, so
your default should be to replace `%>%` with `|>`, however using `%>%`
is not wrong.

To understand the usage of the pipe remember: `x |> f(a,b)` is *the
same* as `f(x, a, b)`. Test it once in a while to understand it! There
is no right or wrong in using the pipe or not.

## Grouping

Grouping for a categorical variable before summarizing or mutating other
variables is a very important tool and a very common operation. We did
it by adding `.by = VARNAME` as an argument in our `summarize` call.
Another version of doing this is to add a line with
`group_by(VARNAME) |>` before `summarize`. `group_by` adds some grouping
information to the data frame which will then be taken into account by
later operations. Older tidyverse code examples will use this operation.
The results is the same. Having grouping information (unconsciously) in
a dataframe objects can be a source of confusion. Therefore, the
`.by = VARNAME` is now the default in tidyverse.
