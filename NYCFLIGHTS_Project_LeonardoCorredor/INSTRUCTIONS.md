# Project NYC Flights


- [1. Warmup: Cloning, Rendering, and finish a round of the
  git-GitHub-dance](#1-warmup-cloning-rendering-and-finish-a-round-of-the-git-github-dance)
- [2. Data overview](#2-data-overview)
- [3. Basic data visualization](#3-basic-data-visualization)
- [4. Data wrangling, pipes, and
  visualization](#4-data-wrangling-pipes-and-visualization)
- [5. Data Audit](#5-data-audit)
- [6. More Data Visualization](#6-more-data-visualization)
- [7. Your own data science question](#7-your-own-data-science-question)

This is·a good first Homework Project.

## 1. Warmup: Cloning, Rendering, and finish a round of the git-GitHub-dance

**Learning goals:** Rendering quarto markdown to HTML output, the
git-GitHub-dance (add, commit, push), orientation of relevant files and
workflow. (Consult the generic [HOW-TO.md](HOW-TO.md).)

⚠️ It is possible that you get stuck at some point.  
**Heads up!** Getting into the git-GitHub-dance is a challenge for
newbies. Make it a priority and reach out for help with clear
descriptions, when you spent enough time trying yourself.

**Tasks:**

- Clone this repository to your local computer.

  - Follow the instructions in the [HOW-TO.md](HOW-TO.md).  

- Start working: Open the starter document `Project_NYCFlights.qmd`.
  This document will become the quarto-markdown file which is the basis
  of your Project Report in this Homework.

- In the R Console, `install.packages("nycflights13")` to install the
  data package. Do the same with the packages `tidyverse` and
  `patchwork` if you have not installed them already.

- *Preveiw* the document and check if the HTML output
  `Project_NYCFlights.html` is produced correctly. Click on the
  HTML-file and view it in your browser. Does it look good?

- **Make the first change in the document**

  - In `Project_NYCFlights.qmd` change the phrase `YOUR NAME HERE` in
    the YAML at the beginning of the document and write your *full name*
    instead.
  - *Preview* the file again and check that your name now appears in the
    HTML output.

  This is a good opportunity to learn and test some basics about YAML
  and HTML pages. Check:

  - [Learning: YAML](LEARNING.md#yaml)
  - [Learning: HTML pages](LEARNING.md#html-pages)

- **Bring your output file and your changed markdown file back to
  GitHub**  
  Follow the instructions in the [HOW-TO.md](HOW-TO.md) workflow to
  `git add`, `git commit`, and `git push` by using the *Source Control*
  section in positron.

**Note:** For the instructors it may be important to find both the input
Quarto Markdown File (.qmd) and the output HTML file of your report in
the repository. Check that both are there by visiting your repository on
<http://github.com> in your browser. One thing may be confusing: You
cannot view the HTML file properly from the GitHub website. If you click
on it you may see the source code but not the page. That is because
GitHub is natively for code. As instructors we clone your repo and look
at the HTML file locally.

**Milestone achieved ✅**

## 2. Data overview

Now, you will extend the section **Data overview** in your Quarto
Markdown file such that the rendered HTML file delivers a human readable
text with an overview about what data is treated in the report.

**Learning Goals:** Working with code chunks, understand *Environment*
and why what works in the console may not work in your rendered report,
loading packages and data, inline code output

1.  Run the first chunk `packages-data` such that the lines are executed
    in the console to load the tidyverse functions and the nycflight13
    data.  
    Typical ways to run a chunk in RStudio are: (i) Click the small
    green triangle on the top right of the chunk. This sends all lines
    to the Console and they are executed one by one. (ii) Put you cursor
    into the first code line and press Ctrl+Enter to execute the line
    and put the cursor to the next line. That is a common action when
    you develop your code line.  
    See which dataframes are available in the Environment tab. The
    environment should be empty, but you can select
    “package:nycflights13” instead of “Global Environment” and you see
    values marked as `<Promise>`. Once you click on one or call it in
    the Console you see basic information there. Learn more about [Code
    Chunks](LEARNING.md#code-chunks). We can leave the chunk as it is.
    Have you understood why it is important that this chunk is at the
    beginning?

2.  Now, finish the text about the number of rows in each of the five
    dataframes. You see the solution for **airport** already in the
    output. It is created by using [Inline
    Code](https://quarto.org/docs/get-started/computations/rstudio.html#inline-code)
    in the Quarto Markdown file. See how the part starting with
    `` `r ``. Everything up to the next backtick `` ` `` is executed and
    the output is formatted as normal text. *What to do?* Replace the
    “*Put your in-line code-output here*” in the text with the actual
    numbers using inline code. Think about: *Why is inline code
    beneficial*, instead of executing `nrow(airports)` in the Console
    and just write the number? (The answer goes beyond the case here,
    think about work in progress.)

3.  Finish the text paragraph about the variables in `flights`. The
    variables `year` to `carrier` are already described. Look up the
    data description with `?flights`. The Help page provides short
    descriptions about each variable.  
    Look at the Output and the Markdown file and try to understand how
    Markdown is transferred to output looking. Now, copy the description
    about the missing varaibles in `flights` into the Markdown file and
    format it such that it renders nicely as the other text. Learn some
    [Markdown
    Basics](https://quarto.org/docs/authoring/markdown-basics.html) for
    Quarto.  
    In particular, check how **bold** and `verbatim code` text is
    formatted. Learn about [Markdown
    Linebreaks](LEARNING.md#markdown-linebreaks).

4.  Render the document and check that the text in Section **Data
    overview** looks good, commit the changes with message “Data
    overview finished” and push it to GitHub such the instructor can
    enjoy your progress!

**Milestone achieved ✅ ✅**

## 3. Basic data visualization

Now, we progress to the section **Data Visualization**.

1.  We first want to know the distribution of values of the categorical
    variable `origin` in `flights`. To that end, make a bar chart. Read
    the Help `?geom_bar` and decide if you need to use `geom_bar` or
    `geom_col`. You can use the template below. Write your solution in
    the chunk `flightsorigin`. Test your line by sending it to the
    Console (with Ctrl + Enter). This is the template.

    ``` r
    ggplot(data = __________, mapping = aes(x = ________)) + 
      geom_TOSELECT()
    ```

    Below the graphic, write a sentence about the number of airports in
    New York City and which had the most and the least departing
    flights.

2.  Now, we want to know the distribution of values of the numerical
    variable `distance` in `flights`. A common visualization is a
    histogram. Use `geom_histogram` with the same template, write the
    solution in the chunk `flightsdistance`, and test it. When you
    render you find the following additional sentence in the output
    `` `stat_bin()` using `bins = 30`. Pick better value with `binwidth` ``.
    It advises to specify a binwidth. Test `binwidth = 5`,
    `binwidth = 50`, and `binwidth = 500` in `geom_histogram`, notice
    the difference (consult `?geom_histogram`) for details, and decide
    which shows the distribution best.

    Below the graphic, write a sentence roughly describing the range and
    frequency of flights of different distances. (Check what the unit of
    distance is, miles or kilometers, and use it in the sentence.)

3.  In chunk `distributions` you see two ways to visualize the
    distribution of the number of `seats` in `airplanes` - points for
    each observation and a boxplot. (Read `?geom_boxplot` for more
    information). Note, that there are three ggplot objects (`g1`, `g2`,
    `g3`) which are shown combined with `g1 + g2 + g3` (using the
    `patchwork` package). Make the empty `g3` into a vertical histogram
    for the same data following the exercise before. Hint: For the
    vertical histogram assign `seats` to the `y` aesthetic and leave out
    the `x` aesthetic.

    Write a short text about the advantages and disadvantages of each
    visualization for showing the distribution of seats.

4.  Now, we make the first plot which visualizes two variables, the
    categorical variable `engine`, and the numerical variable `seats` in
    `planes`. Use the template with aesthetics `x` and `y` and
    `geom_boxplot`. Put the solution into the chunk `engine-seats`.

    Describe the relation between engines and seats of planes in a short
    paragraph below the graphic.

5.  Two numerical variables can be visualized with a scatter plot using
    `geom_point` and the aesthetics `x` and `y`. Let us look at
    `dep_delay` and `arr_delay` of `flights`. Warning: `flights` is very
    large! So, do not use `flights` in `data = _____` but a random
    sample of 5,000 flights `sample_n(flights, 5000)`. Now, let us add
    information about the categorical variable `origin` and assign it to
    the `color` aesthetic. Put your solution into the chunk `delays`.
    Test your solution several times and observe the changes in the
    visualization because of the random sampling.

    Analyze the following and describe it. Are there planes departing
    and/or deriving earlier than planned? How much maximally? What is
    the main source of arrival delay, departure delay or something else?
    How can we see it?

    Bonus: Can you think of helful annotation lines in the graphic? Try
    to plot them additionally.

6.  Visualize the location of `airports` as points at their *longitude*
    and *latitude* (look up the variable names) and color them with the
    timezone `tzone`. Put the solution into the chunk
    `airportlocations`.

    Describe how many time zone we see.

7.  Render the document and check that the text in Section **Basic data
    visualization** looks good, commit the changes with message “Basic
    data visualization finished” and push it to GitHub such the
    instructor can enjoy your progress!

**Milestone achieved ✅ ✅ ✅**

## 4. Data wrangling, pipes, and visualization

In the following, you have to solve some data wrangling tasks to answer
questions. For data wrangling, the usage of the
[Pipe](LEARNING.md#pipe), or a chain of pipes, is convenient. You can
also use the pipe to finish with a visualization.

1.  Put the code snippet below into the chunk `flightsaveragespeed` and
    test it.

    ``` r
    flights |> 
    mutate(speed = distance / air_time ) |> 
    select(air_time, distance, speed)
    ```

    The `mutate` line makes a new variable called `speed` which is the
    distance of the flight divided by the time in the air. The `select`
    line selects variables from the dataset. In this case, it selects
    `air_time` as the first, `distance` as the second, and the new
    `speed` as the third variable. All other variables are dropped.

    The values in the new speed variable do not look like speeds of
    airplanes in km/h. Why? Because they are in miles/minute which we
    know from the variable descriptions. Modify the equation in the
    mutate command such that the values are in km/h. To that end, you
    have to divide air time by 60 and multiply distance by a certain
    factor. Look up the factor. Be careful with the order of
    mathematical operations and maybe use brackets `()`. Test your
    computation. Are the speed values reasonable?

    Now, make a histogram of speed. Add another pipe after the `select`
    statement and write `ggplot(mapping = aes())` in the next line.
    Note, that you should not put `data = flights` into the argument of
    `ggplot()` this time! It is the mission of the pipe to do this. Fill
    out the `aes()` command accordingly, and add the geom for a
    histogram.

2.  Practice `filter` operations, which subsets certain observations of
    a dataframe. Write a line which filters the flights which

    1.  had an arrival delay of two or more hours
    2.  flew to Houston (IAH or HOU)
    3.  arrived more than two hours late, but didn’t leave late
    4.  started with a delay of at least an hour, but made up over 30
        minutes in flight.

    For each question write a sentence of the type “X flights had an
    arrival delay of two or more hours.” and replace the “X” with an
    inline code `` `r YOUR PIPE` ``. You can end your pipe with
    `|> nrow()` to output the number of rows in the filtered dataframe.

3.  Another common operation is summarizing data. Put the code below
    into the chunk `summarizing` and test it. You see the average delay
    at departure. (See `?mean` to learn what `na.rm = TRUE` is doing).
    Now, we want to know the average delay at departure for each of the
    three airports of `origin`. This can be done by adding the variable
    in a `.by = VARNAME` argument to the `summarize` command.

    ``` r
    flights |> 
      summarize(mean_dep_deplay = mean(dep_delay, na.rm = TRUE))
    ```

    Learn about another common way of [Grouping](LEARNING.md#grouping).

    Now, we want to make a nicer looking table output. To that end, add
    `library(knitr)` at the begining of the chunk. The library has the
    function `kable` which produces markdown output for a dataframe. So,
    add `|> kable()` at the end of your summarize pipe.

    Write a sentence answering the question from which airport the
    flights are on average most delayed.

4.  Render the document and check that the text in Section **Data
    wrangling** looks good, commit the changes with message “Basic data
    visualization finished” and push it to GitHub such the instructor
    can enjoy your progress!

**Milestone achieved ✅ ✅ ✅ ✅**

## 5. Data Audit

In the section **Data Audit** you do a typical data audit task starting
with the plot of `airportlocations`. The airport locations show the
shape of the United States of America. (Do you recognize the shape,
maybe distorted? You see Alaska?) There are four airports on the right
hand side which do not fit that pattern. Filter `airports` such that you
only see these four airport. Write your solution into the chunk
`strangeairportlocations`. Check with internet research where these
airports are located. Why are the locations from the data as they are?
Write your hypotheses for each airport under the chunk in plain text.

Render, commit and push!

**Milestone achieved ✅ ✅ ✅ ✅ ✅**

## 6. More Data Visualization

1.  The Section **More data visualization** does not exist in the
    document. So, you have to write it your self. Check [Markdown
    Basics](https://quarto.org/docs/authoring/markdown-basics.html) for
    Quarto.

    As starting text for the new section write “In the following we
    provide some more information about the flights of different
    airlines, about the age or planes departing for the three New York
    airports and the weekly percipation on the three airports.”

    \*For all following graphs use tune your axis labels more human
    readable and give them an informative title. (Hint: use `+ labs()`).

2.  **Graphs about airlines**

    1.  Create a chunk in which you visualize the following: On the
        y-axis you provide the names of all airlines. On the x-axis you
        provide bars which show the number of flights this airline
        operated. Order the airlines by the number of flights. Use the
        names of the airport in the graphic, not the carrier ID! Write a
        descriptive label for the x-axis and remove the label “Airline”
        on the y-axis. (Hints: You need to join data here! Avoid that
        text like “Joining with `by = join_by(carrier)`” appears in the
        html output. To that end, copy the join specification into the
        join command. There are different ways to construct the graphic
        either using `geom_bar` or first summarizing the dataframe and
        then using `geom_col`. Use the second way. An easy way to
        summarize for this case is to use `count`. Use `fct_reorder` to
        order the airport names by the number of fights. Use
        `+ labs(...)` for customization of the axis labels.)
    2.  Create another chunk and visualize the mean departure delay by
        airline similarly. (Hints: Create the new variable for the mean
        departure delay with `summarize`.)  
    3.  (BONUS) Visualize the mean departure delay and the mean arrival
        delay with two bars (departure and arrival delay) for each
        airline side by side. (Hints: Use `pivot_longer` to create a
        column `delay_type` and `mean_delay`. Then assign `delay_type`
        to the `fill` aesthetic in the plot. Use `position = "dodge"` to
        make the bars side-by-side. Optional: Use `fct_reorder2` to
        create your order across `delay_type` and `mean_delay`).

3.  Graph the **number of departing planes** by the **year they were
    manufactured** faceted by the three origin airports using the full
    airport names. (Hints for R: You have to join data here twice
    (planes and airports to flights). Warning: There maybe a
    complication with variables names in planes. You could solve it by
    using `rename`. Further on, you have to check on which variables to
    join the airports. When you have the joined data frame, you can
    `group_by` the year manufactured and the airports from which they
    departed. `summarize` by counting the number of flights using the
    convenience function `n()`. Alternatively you could also use
    `count`. Make a ggplot using the count on the y-axis and the
    manufactured year on the x-axis. `facet_wrap` by the name of the
    airport of departure. With `facet_wrap` you can change the graph
    such that the facets are in one row or in one column. Try both and
    select the one, in which you can compare the distributions best.)

4.  Graph the total **weekly percipation** at the three airports with a
    line plot with lines of different color for each airport. (Hints for
    R: Practice string and date manipulations in the following way.
    Create a new variable `date` for which you first create a string
    which concatenates the variables `year`, `month`, and `day` into a
    string of the format “YYYY-M-D” using the function `paste` with a
    custom separator `sep = "-"`. Then apply the function `as.Date` to
    create the date variable in the `<date>` format. (Ignore the
    existing time_hour variable here to practice.) Now, use the function
    `week` to create a variables with the week number. Group by the week
    and the airport and sum the percipation of the week. Make a line
    plot using the week for x and the total percipation for y and the
    airport for color.)

Render, commit and push!

**Milestone achieved ✅ ✅ ✅ ✅ ✅ ✅**

## 7. Your own data science question

Think about an interesting question about flights from New York City.
Formulate it and write it down. Try to answer it with a graphic, a
table, and text (maybe using inline code). If you cannot answer your
question, refine your question and try again.

Also make a new headline before your own question.

Render, commit with message “Project done.” and push!

**Project finished!** ✅ ✅ ✅ ✅ ✅ ✅ ✅
