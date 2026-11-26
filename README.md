# CISC 480 Portfolio

A selection of projects from my B.S. in Computer Science at the University of St. Thomas (graduated December 2023). They span robotics, machine learning and statistical modeling. More are on the [Projects page of my personal website](https://nfriesen1.github.io/pages/projects.html).

| Project | Course | Tools |
|---|---|---|
| [1. Drawing robot](#project-1-drawing-robot) | CISC 440: AI and Robotics | Python, ev3dev2, Lego Mindstorms EV3 |
| [2. Predicting stock movement with neural networks](#project-2-predicting-stock-movement-with-neural-networks) | STAT 400: Data Mining and Machine Learning | Python (pandas), JMP |
| [3. What makes car crashes deadlier](#project-3-what-makes-car-crashes-deadlier) | STAT 360: Computational Statistics and Data Analysis | R (lavaan, psych), draw.io |

---

## Project 1: Drawing robot

**Goal:** program a Lego Mindstorms EV3 robot to draw letters and short words with a pen.

The Python script ([`Project 1 Files/Project 1.py`](Project%201%20Files/Project%201.py)) treats each letter as a path through points on a grid. For every move, it works out the turn angle and distance from geometry, then converts them into wheel rotations, adjusted for the robot's wheel size and wheel spacing. A medium motor raises and lowers the pen between strokes. For the final test, the robot drew the word **MILE**.

**To run it**
1. Build the robot in "drawing" mode: wheels, plus a pen held in place with rubber bands.
2. Raise the pen, connect to the robot, and run the script. `my_string` can be any word made from the letters defined in `sequence` (currently M, I, L and E).

---

## Project 2: Predicting stock movement with neural networks

**Goal:** see whether a neural network could predict if a stock would close higher or lower than the day before. I did this project with two classmates.

We used five years of daily prices for large tech stocks. A Python script ([`StockPriceUpOrDown.py`](Project%202%20Files/StockPriceUpOrDown.py)) labeled each day "up" or "down" by comparing its close with the previous close. We then trained and compared neural network models in JMP.

**Files**
- [`Stock Data/`](Project%202%20Files/Stock%20Data): raw price history (CSV)
- [`Final Dataset.xlsx`](Project%202%20Files/Final%20Dataset.xlsx): the cleaned, combined dataset
- [`Final_Data - Neural.jrp`](Project%202%20Files/Final_Data%20-%20Neural.jrp): the JMP neural network report
- [`Final Project Paper Updated.docx`](Project%202%20Files/Final%20Project%20Paper%20Updated.docx): the full write-up

**To reproduce**
1. Run `StockPriceUpOrDown.py` on each CSV in `Stock Data/` to add the up/down label.
2. Load the result (or `Final Dataset.xlsx`) into [JMP](https://www.jmp.com/), then go to **Analyze → Predictive Modeling → Neural** and fit a model.

---

## Project 3: What makes car crashes deadlier

**Goal:** find which factors are linked to higher death rates in car crashes, and show how they connect. I did this project with two classmates.

We cleaned and explored crash data in R. We then used **exploratory factor analysis** to group related variables into underlying factors, and **structural equation modeling** to estimate how those factors relate to crash mortality. The result is a path diagram:

![Path diagram of factors related to crash mortality](Project%203%20Files/Finished.drawio.png)

**Files**
- [`EDA.Rmd`](Project%203%20Files/EDA.Rmd): exploratory data analysis
- [`Project EFA.Rmd`](Project%203%20Files/Project%20EFA.Rmd): exploratory factor analysis (`psych`, `GPArotation`)
- [`SEM.Rmd`](Project%203%20Files/SEM.Rmd): structural equation model (`lavaan`)
- [`Project_Data.xlsx`](Project%203%20Files/Project_Data.xlsx): the cleaned dataset
- [Abstract](Project%203%20Files/Abstract.pdf) · [Presentation](Project%203%20Files/STAT%20360%20Group%20Project%20Presentation.pptx)

**To reproduce:** open the `.Rmd` files in RStudio, point them at `Project_Data.xlsx`, and knit them in order: EDA, then EFA, then SEM.
