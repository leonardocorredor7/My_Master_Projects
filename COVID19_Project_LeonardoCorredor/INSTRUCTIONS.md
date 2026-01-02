# Project COVID-19


- [0. Data](#0-data)
- [1. Time evolution](#1-time-evolution)
  - [1.1 Covid Cases and Deaths in Germany’s 1st
    wave](#11-covid-cases-and-deaths-in-germanys-1st-wave)
  - [1.2 Cumulative cases in Germany, Italy, France, and
    UK](#12-cumulative-cases-in-germany-italy-france-and-uk)
  - [1.3 Smoothing daily data](#13-smoothing-daily-data)
  - [1.4 How do deaths follow cases?](#14-how-do-deaths-follow-cases)
  - [1.5 When does the wave break?](#15-when-does-the-wave-break)
- [2. World Development Indicators](#2-world-development-indicators)
  - [2.1 Correlation](#21-correlation)
  - [2.2 Principal Component Analysis](#22-principal-component-analysis)
- [3. Potential Data Science Projects
  (OPTIONAL)](#3-potential-data-science-projects-optional)

In this homework you will explore and model the development of the
**COVID-19 pandemic 2019-2022** and write a report about it.

**Learning goals:**

- Work with time series. A times series is a sequence of data points,
  typically consisting of successive measurements made over a time
  interval. Here we have daily measurements of new cases and new deaths
  in most countries of the world.
- Smoothing time series.
- Apply calculus thinking: What is the derivative (differences)? What is
  the integral (cumulative sum)?
- Do parameter fitting *by hand* and *by eyes*
- Explore indicators for potential models relating socio-economic
  indicators to the development of the pandemic.

There is a starter document `report.qmd` in the repository. This will
become your report. Render it to HTML, check that it looks good and
commit intermediate versions to receive help and feedback.

The starter document includes some basic structure with YAML, headlines,
and one initial chunk, but you need to add your own chunks
independently. You also should care about always writing a short
concluding text in each section.

# 0. Data

Two data sets are provided in the repository:

1.  Daily numbers of new cases of COVID-19 and new COVID-19 related
    deaths in most countries in the world as collected by the World
    Health Organization (WHO) on a daily basis. The data is from
    2022-09-30.
2.  World Bank Development Indicators (WDI) with some socio-economic
    indicators as provided for most countries in the world.

Use the chunk `packages-data-functions` to load the `tidyverse` package
and read in two dataframes `who` and `wdi`.

In the following come back to this chunk and do data transformations and
mutations there, except for those you need only for a particular
visualization. In the following you will also write some functions to
use in your data manipulation. Also put these in this chunk. It can
become a longer introductory code chunk.

# 1. Time evolution

## 1.1 Covid Cases and Deaths in Germany’s 1st wave

- Plot a time series of the number of daily cases and daily death in
  Germany before 2020-08-31 in one diagram. (Hints for R: For plotting
  cases and deaths in one plot use `pivot_longer` before the plot.)
- Describe the development of cases in Germany answering questions like:
  When did the wave start? When did it end? When was the peak? How many
  cases were there at the peak? How many deaths were there at the peak?
  What are the fluctuations and why could they be there?

## 1.2 Cumulative cases in Germany, Italy, France, and UK

- Plot the cumulative cases for the four countries until 2020-08-31s in
  one panel. Provide the cumulative deaths in another panel. In the
  terms of calculus, we are doing and integration of the new cases time
  series. (Hints for R: In the chunk `data`, create additional variables
  for the cumulative cases and cumulative deaths using `cumsum`. Do not
  forget to group by country! Use `pivot_longer` for cumulative cases
  and deaths before the plot and then `facet_wrap` by cases and deaths.)
- Describe how the pandemic in Italy, France, and UK unfolded
  differently than in Germany.

## 1.3 Smoothing daily data

- Create three functions `smooth3`, `smooth7`, and `smooth10` which
  smoothes the data with *moving averages* of the last 3, 7, and 10
  days. The function should take a timeseries input as a vector
  `function(x)` and output a vector or the same length. Then use these
  functions to create new variables `New_cases_smooth3`,
  `New_cases_smooth7`, `New_cases_smooth10`, `New_deaths_smooth3`,
  `New_deaths_smooth7`, and `New_deaths_smooth10`. Do all of these
  mutations in the chunk `data` and do not forget to group by country!
  (Hints for R: To compute a moving average for a time series `x` for
  the last 3 days, use
  `1/3 * (x + lag(x, n = 1, default = 0) + lag(x, n = 2, default = 0))`.)  
- Make a plot to compare the smoothed three types of smoothed daily
  cases for Germany until 2020-08-31. Make one panel for each smoothing
  window (3 days, 7 days, 10 days).
- Describe: Which window smoothes the data best? Normally, the more days
  you average, the smoother will be the data. Why is this not the case
  here?

## 1.4 How do deaths follow cases?

- We continue with Germany as for the former task.  
- Create a new variable `shiftscale_cases` which is a shifted and scaled
  version of `New_cases_smooth7`. Use trial and error playing with
  different values for shift and scale. Your goal shall be to fix the
  shift and the scale parameter such that the plots for
  `shiftscale_cases` and `New_deaths_smooth7` overlap as good as
  possible for the days when cases where increasing exponentially
  (second half of March). That way you can analyze how many days we need
  to shift the cases until they match cases and how much less deaths
  there are than cases.  
  How to in R: Write a function
  `shiftscale <- function(x, shift, scale)` where you shift the
  timeseries `x` using `lag` by `shift` days and scaling the magnitude
  of `x` by multiplication with `scale`. Then create the new variable
  using `shift = 0` and `scale = 1` and plot the time series of
  `shiftscale_cases` and `New_deaths_smooth7` in one panel. This plot
  should look like the smooth version of the plot from the first
  visualization. Now play with different numbers for `shift` and `scale`
  until you reach the best overlap of both graphs focusing on the time
  in the second half of March. Only put your best solution in the
  report.  
- Describe: Write down the parameters you used to shift and scale cases.
  How well is the overlap in the exponential growth phase? How can you
  use your two numbers for `shift` and `scale` to describe the relation
  between deaths and cases?  
- Now, create a second visualization where you use the same shift and
  scale but plot the time from 2020-07-01 to 2020-12-31 in Germany. Do
  the two time series still overlap? If not, how do they differ? What
  has changed in the relation between cases and deaths in the second
  wave?  
- (BONUS) Select two countries of your choice and repeat the exercise to
  *fit* the shift and scale parameters by guessing and visual
  assessments in the first wave’s exponential growth phase. (Hint:
  First, assess visually a good time range to show for these particular
  countries.) Are the parameters similar to the ones you found for
  Germany?

**Learning:** What you did by playing with parameters with the goal to
match two lines is a *hand-made* search optimization procedure where
your objective is to find *the best visual match*. In *mathematical
optimization*, an algorithm does the same with a certain procedure to
move through the *space of possible parameters*, and a mathematical
*objective function* which quantifies how good a function (here the
shiftscale of new cases) matches the target (here the new deaths).
*Mathematical optimization* is the basis of fitting models. You did that
*by hand* playing with parameters and *by eyes* looking at how good you
find the match.

## 1.5 When does the wave break?

- Plot the change of the smoothed (7 days) new cases (= derivative of
  new cases = 2nd derivative of cumulative cases) in Germany in the time
  range 2020-03-01 to 2020-04-15. Compute the variable
  `Diff_cases_smooth7` and make a visualization with two panels, one for
  the smoothed new cases and on for the diff. (Hint for R: Subtract
  `lag(x, n = 1)` from the time series `x` to compute the derivative.)
- Describe how the two two graphs are related. At what day did was the
  peak of the diff, at what day was the peak of the smoothed new cases?
  (Visualization hint: Use
  `+ scale_x_date(date_breaks = "2 days", date_labels = "%d")` to show
  detailed days on the x-axis.

# 2. World Development Indicators

The exercises are based on the data set `wdi` which you created in the
chunk `data`, however the variable names are very long. For convenience
you can `rename` them to shorter names, for example
`urban_pop, rural_pop, pop_lower_half_median, pop, pop_older65, pop_density, physicians_per_1000, life_expectancy, gdp_per_capita`.

## 2.1 Correlation

- Make a plot of the correlation matrix of all numerical indicators in
  the WDI data set. (Hint for R: For example you can use `cor` to
  compute the correlation matrix and `corrplot` to plot it.)
- Describe: Which indicators are correlated? Which are not? What does
  this mean? (Use `correlation` from the package `correlation` and plot
  the results using `|> summary(redundant = TRUE) |> plot()`.) Describe
  some interesting correlations. There are two variables which are
  essentially one, can you spot them in the correlation matrix?

## 2.2 Principal Component Analysis

- For PCA’s we need to remove NA’s. We can either remove countries with
  NA’s or variables with NA’s. The first option is not very good,
  because we would lose many countries. The second option is not very
  good, because we would lose many variables. So we will do both and
  compare the results. Create a data frame `wdi_noNA_small` where you
  remove all countries with NA’s (use `na.omit`), and a data frame
  `wdi_noNA_large` where you first remove the two variables with most
  NA’s (find out using `summary(wdi)`) and then the countries with
  remaining NA’s.
  1.  Write a sentence which explains how many countries are in each
      data frame. (Hint: Use [inline
      code](https://quarto.org/docs/computations/execution-options.html#inline-code)
      like `` `r nrow(wdi_noNA_large)` ``). Make a table for the small
      data frame where you list all countries which are in `wdi` but not
      in `wdi_noNA_small` and which have more than one million
      population. (Hint: Use `anti_join` to select the rows of `wdi`,
      use `knitr::kable` to make the table nice in the output.). Are
      large countries missing? Make the same type of table for the data
      frame `wdi_noNA_large`. 2. Make a subsubsection (`###`) “PCA
      small” where you visualize the explained variance, the first four
      principal components from the rotation matrix, and the countries
      in the coordinates of PC1 and PC2. For each describe your main
      observations. In particular describe, what PC1 and PC2 represent.
      (Visualization hint: Color by `region` and use the additional
      aesthetic `label = iso3c`. Then use `geom_text(size = 3)` instead
      of `geom_point`. That you can see the country’s iso codes to
      describe where some countries lie.)
  2.  Repeat the former exercise for the data frame `wdi_noNA_large`.

# 3. Potential Data Science Projects (OPTIONAL)

Here are a few questions and ideas for data science projects.

- Decide for a certain day and compute the total deaths for each
  country. Create a new variable which count deaths per 100.000 people.
  Then develop linear models (maybe with categorical variables and
  interaction effects) which inform us about the impact of certain World
  Development Indicators of your choice.  
- Use a linear model to fit exponential growth curves. You would fit the
  linear model on the log-cases and then use the fitted intercept and
  slope to plot the exponential function together with the empirical the
  new cases. To that end you need to identify the day ranges looking
  like exponential growth. As a following question estimate exponential
  growth curve for the cumulative cases of the same country. Compare the
  fitted slopes of new and cumulative cases. What should we expect
  theoretically?
- Automatize a shift-scale optimization by writing an objective function
  measuring the distance between the shiftscales function and the target
  and then use a function like `fminsearch` to find the best shift and
  scale parameter. Then fit shift and scale parameters for all countries
  for the first wave and analyze if you find a typical pattern. (To that
  end you also need to find a way how to select the day when the first
  wave was at each peak in each country.)
