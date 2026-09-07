# Project 3 - Sales Analysis

Project is a data analysis project that sales data to answer business questions and validate hypotheses. The project involves data cleaning, transformation, and visualisation using Python and various libraries.

As well as machine learning!

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset Content

Dataset package given by customer contains 1 raw CSV file:

- Sales_InvoiceData.csv

Custom created datasets:

Sales_InvoiceData_GroupedByTerritory.csv - Used by machine learning contains data grouped by TerritoryCode and YearMonth with sum of InvoiceAmt

Sales_InvoiceData_GroupedByCustomer.csv - Used by machine learning contains data grouped by CustomerID and YearMonth with sum of InvoiceAmt

**Project Folder Structure:**

Subfolders:

assets:  
&nbsp;&nbsp;&nbsp;&nbsp;csv/Data <- Contains csv files during processing from raw to visualisation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CleanedFiles <- Contains cleaned data as csv files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ExtractedFiles <- Contains files extracted from ZIP files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OriginalFiles <- Contains the original data csv files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VisualisationFiles <- Contains a csv file for visualisation  
&nbsp;&nbsp;&nbsp;&nbsp;pipelines - machine learning pipelines  
&nbsp;&nbsp;&nbsp;&nbsp;python_files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains my custom modules  
documents <- Contains files:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What_AI_Used_For.md (terrible grammar)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Project 3 Sales Analysis Dashboard Design.pdf  
jupyter_notebooks <- Contains the Jupyter Notebooks used for ETL/EDA/ML and Visualisation  
reports<- Contains the report for the project  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Images <- Contains images used in the report  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains file: AnalysisConclusion.mdwhich is the project report  
streamlitapp.py <- Contains the streamlit dashboard application

**Jupyter_Notebooks:**

ETL/EDA etc are purposely put into separate Jupyter notebooks for ease of use and debugging!

**Notebook Files:**

- Notebook_EDA_Sales_DataSet.ipynb <- EDA for Sales_InvoiceData_Visualization.csv
- Notebook_Notebook_ETL_Sales_DataSet.ipynb <- ETL for Sales_InvoiceData.csv
- Notebook_ML.ipynb <- Contains the machine learning model for experimentation has own visualisations
- Notebook_Visualisations1.ipynb <- Contains the visualisations for the hypotheses

**Report File**

- AnalysisConclusion.md <- Contains the report for the visualisations this is the final report for the
  project and contains the analysis and conclusions for each hypothesis, _however_ the plots are represented as images in the report and are not interactive. The interactive plots are in the dashboard
  This is report is two fold, is a great metric as to whether I can convey analysis in retrospect to the data story and test my ability to create an understandable report!

**Documents:**

- What_AI_Used_For.md:

Describes in detail how I used AI to help with issues with the project.

- Project 3 Sales Analysis Dashboard Design.pdf:

Outlines the dashboard design ethos.

**KANBAN**

In GitHub there is a KANBAN project, that was used for project management, used the road map feature to show required completion dates for various aspects e.g. ETL.

It wasn't explained if we needed to move each completed section to "Done" in KANBAN as the project progressed or leave them "as is", but I needed to do that so I knew where I was in the project and waht task were remaining!

**Dashboard**

The dashboard is available via Heroku at this URL:

zubzub

**GitHub**

Project GitHub URL is:

https://github.com/RogerWilliams2026/Project3-SalesAnalysis.git

### Using The Notebooks

In order to see the plots these notebooks need to be run in order from the Jupyter_notebooks folder:

- Notebook_ETL_Sales_DataSet.ipynb <- ETL for Sales_DataSet.csv
- Notebook_EDA_Sales_DataSet.ipynb <- Contains the EDA for the csv file
- Notebook_ML.ipynb <- Contains the machine learning model for experimentation has own visualisations
- Notebook_Visualisations1.ipynb <- Contains the visualisations for the hypotheses

## Business Requirements

A requirement for a wider view of sales performance in the business in key areas, including sales by territories and product families.

Special interest was shown in sales by territory and I got the feeling they are keen to identify profitable and less profitable customer by sales territory, as well as the amount of credits given to customer.

The customer hopes this information will help it plan its growth and marketing strategies to maximise profits in the areas that are shown to be profitable, but also focus on improvement for the areas that are not performing well.

## Ethics and GDPR Considerations

The dataset contains a column of contact names and a column of customer names. Based on the premise this data is going to be available via a public dashboard made the decision to _withhold_ the information from the public dataset which complies with GDPR and ensures data privacy.

There is a description in the dashboard as to how private data is treated.

## Hypothesis and How To Validate?

- What were the highest sales per territory for last year?
  Validation: Test with a suitable plot to show correlation between invoice amount sum and territory filtered for highest value

- Who were the top 20 customers by sales for last year?
  Validation: Test with a suitable plot to show customer ID and value

- Who were the bottom 20 customer by sales for last year?
  Validation: Test with a suitable plot to show customer ID and value

- What was the total amount of credits issued for last year by customer?
  Validation: Will group sales for a total for each customer then chose an appropriate plot

- What was the percentage of ship methods used last year?
  Validation: Thinking of a simple pie plot as percentages used, might not sum to 100% though, will test and see

- What were the total sales per customer per territory for last year?
  Validation: Will show plot grouped by territory, then customer ID sunburst seems ideal for this due to number of customers

- What were the sales by product family for last the two years?
  Validation: Will show with a comparison plot with each year in a different colour

Machine Learning Predictions:

- What are the predicted sales per month for next year?
  Validation: Test with linear regression and random forest to determine best model for hypothesis

- What are the predicted sales per territory for next year?
  Validation: Test with linear regression and random forest to determine best model for hypothesis

## Project Plan

- Acquire raw data as csv files from the customer
- Clean and transform the raw data into cleaned csv file
- Perform EDA to see if there are any correlations between the data (and the hypotheses if possible)
- Visualise the data to validate the hypotheses and answer the business questions
  using multiple visualisation libraries to find best fit for the customer requirements
  as well as the best looking visualisations for clear insights into the data and choosing
  the most appropriate visualisation for the hypothesis being validated
- Use machine learning to predict sales for the next year and visualise the results
- Create a report to present the findings to the customer
- Create a streamlit dashboard to showcase the results
  Note: Plots in the dashboard can be different to the ones done in the visualisation Jupyter notebook simply for asctetics

## The Rationale Used To Map The Business Requirements To The Data Visualisations

_Hypothesis 1: Are sales increased if weather is hotter or colder in the last 12 months?_
Chose scatter plot to show the correlation between temperature and sales. Due to the large amount of data, a scatter plot is the best way to visualise the data and show the correlation.

## Analysis Techniques Used

From the initial csv file 3 more are created 4 via ETL as it goes through the ETL stages all end with an applied naming convention:

- Sales_InvoiceData_Cleaned.csv
- Sales_InvoiceData_Working.csv
- Sales_InvoiceData_Visualisation.csv

For machine learning 4 pipelines are created:

- linear_regression_hypothesis8_test_pipeline.pkl
- randomforest_hypothesis8_test_pipeline.pkl

- linear_regression_hypothesis8_predictions_pipeline.pkl
- randomforest_hypothesis8_predictions_pipeline.pkl

- linear_regression_hypothesis9_test_pipeline.pkl
- randomforest_hypothesis9_test_pipeline.pkl

- randomforest_hypothesis9_predictions_pipeline.pkl
- linear_regression_hypothesis9_predictions_pipeline.pkl

Files with _test_ in the name are used to run test "prediction" by getting machine learning processes
to "predict" values for an existing year. This is used to compare with the previous year via a plot

The other files are used in machine learning to predict the next years values, again shown in a plot

**Methods Used:**

Generative AI tools were mostly used to solve code issues and occasionally for plotting ideas due to my lack of experience with visualisation libraries and complex plots.

Data was a limiting factor, not in terms of detail but sheer volume and breadth. I was stumped by one potential hypothesis by the fact I was trying to analyse sales data with one month alone having over 800 unique customers buy something! Lacking experience to know what plots and strategies are best to use to visualise this type data I simplified the approach and summised the invoice amounts and reduced the hypothesis to a more manageable scope.

Adapted with a "best guess Mr Sulu" approach to visualising large data, running plot tests to see what the libraries can handle and go beyond, bar, histogram and scatter plots which worked well, as I could now use more effective plot types and I have a huge attraction to the 3d scatter plot!.

Analysed plots compared to hypothesis, by checking expected values against queries with the raw data. If the dataset to use is corrupt or incorrect the plot will be useless.

Use external tools such as Microsoft Access to create queries to validate some of the hypothesis before translating the SQL query into pandas.

Decided to use both linear regression and random forest for the machine learning experiments, nice broad range of models that can be used with the data.

## Libraries Used

The requirements.txt has the full list, but here is a list taken from the Jupyter notebooks as well as my custom modules:

charset-normalizer
joblib  
matplotlib.pyplot  
matplotlib.ticker
nbformat  
numpy  
os  
pandas  
pathlib  
plotly.express  
scipy.stats  
seaborn  
sklearn.compose  
sklearn.ensemble  
sklearn.impute  
sklearn.linear_model  
sklearn.metrics  
sklearn.model_selection  
sklearn.pipeline  
sklearn.preprocessing  
sklearn.tree  
statsmodels.api  
statsmodels.formula.api  
sys
zipfile

Also included my own libraries:

modGlobal  
modETL_Library

The streamlit application uses these:

joblib  
matplotlib.pyplot  
matplotlib.ticker  
nbformat  
numpy  
pandas  
pathlib  
plotly.express  
scipy.stats  
seaborn  
streamlit

## Development Roadmap

### Basic Strategy:

- Get data into DataFrames and perform ETL using my custom library where possible
- Create a cleaned csv file for the raw csv files
- Copied the cleaned csv file for to a visualisation file
- Perform exploratory EDA to see if there are any correlations between the data (and the hypotheses if
  possible)
- Visualise the data using available plot libraries and chose bets library for each hypothesis
- Get data into a machine learning model for at least one hypothesis, choose example that could not
  achieved _without_ machine learning i.e. sales prediction for next year
- Put images of the hypothesis plots into the a findings report and construct as though a presentation to
  the customer (perhaps in concert with the dashboard?)
- Populate findings report with plots and analysis for each hypothesis a

### Challenges and Strategies

- VS Code repeatedly has a kernel hang randomly during development requiring restarting VS Code  
  as kernel restart rarely restarts. This only oocues when using Jupytper notebooks in a virtual
  environment, sometimes leading to 14+ restarts of VS Code in a day!
- Had issue with pandas not reading the csv file as it was not in UTF-8 format, chatGPT solved that issue
  and added new code into my ETL library to auto detect the csv file encoding
- Markdown markup language is irritating in that need to but two spaces at the end of line just to get it
  to keeps lines separate and most annoying of all it has no capacity for indenting!

## New Skills and Tools

- Generative AI tools (Copilot and chatGPT) helped hugely with strange library issues and code snippets
  and the generation of the first sunburst plot
- Learned about project management, and effective timeboxing for project sections e.g. documentation as
  well as the composite
- Discovered I preferred plotly as a visualisation tool due to its better appearence and options
- Some nice EDA skills and better ways to "know the data" than merely .shape/.describe etc. such as:
  Q-Q plots and the great eye opener the Parametric tests
- More plot skills, such as using sunbursts for drill-downs and finally found a use for my favourite plot
  the 3D scatter! In the LMS examples it was largely cosmetic and difficult to read but I found a hypothesis
  I had was the perfect fit, and it shows how can be more than a gimmick plot and actually show data in a
  way that would take many, many words to achieve
- Also got confident it applying lots of differing EDA styles to analyse columns and potential correlations
- Got quite handy with streamlit. Being familiar with HTML helped a lot for example I think of containers
  as HTML DIVs, and KEY as HTML ID
- Finally tamed MarkDown so I could add images using relative addressing, before it pretended to do it, then
  when MarkDown was previewed would _copy_ the image to the _root_ folder with a generic name and use that!
- Better understanding of how to look at raw data and see patterns and formulate hypothesis from them
- More confidence with plot type choice, now happy to experiment with newer chart types like sunbursts

## Dashboard Design

The dashboard is designed to be easy to "read" and and easy to use. Where possible each plot has a dataframe view for those more interested in the raw data. The dashboard is designed to be used by a non-technical person and is designed to be self explanatory, this is done on purpose as to broaden the acceptence of the dashboard and limit any specialist knowledge needed to understand it.

Purposefully the R-squared values were omittted from the machine learning plots as to the non technical user the values have no meaning, after all a large percentage of managements people looking for answers to question from data have almost no expsoure to data analysis science and to encourage inclusivity have kept the "low level" technical details to a minimum.

So the compromise was to include _all_ plot results from both machine learning models as the visual story explains the choices made better than a page full of complex numbers.

Where possible slider controls have been used to allow the user to play with the plots and see what other insights they can obtain, this was a concious decision to try and move the dashboard away from the traditional "point-click=and=stare" approach to something more engaging.

## Who Won The Generative AI Battle?

chatGPT won hands down, I found Copilot in VS Code largely irritating and invasive, and it was not very good at solving code issues a bit of a mixed bag. chatGPT on the other hand was very good at solving code issues and providing code snippets that worked first time. When I went of the rails and without knowing it and was using the wrong approach to visualising one hypothesis. Copilot's suggested plot was cramped, difficult to read and (as I discovered) the wrong plot type for the data, plus it was hugely convoluted.

Posted the code into chatGPT and over an hour it honed and rehoned the code to a 92% working solution with a better type of plot. Due to the massive size of the data it caused many rendering issues such as a huge gap between the plot title and the first actual plot and missing x axis labels.

Which of course after a good nights sleep I realised _I_ was using the wrong plot _and_ data visualisation concept and looking at the data visualisation backwards!

Did notice as time has gone by CoPilot in VS Code is making a lot more mistakes, might be better off if Microsoft concentrated on making an knowledge based system version instead... (bring back the wizards!!)

## Things To Learn Next

- Proper use of KANBAN for project management (there s a rumour it supports sprints..)
- Better understanding interactive plots and how determine which is best for the data being visualised
- More practice with machine learning, particularly with categorical data and dates
- More practive with streamlit makig plots more interactive via use of widgets
- Learn how to use streamlit callbacks to make plots more interactive. For example clicking on a sunburst
  plot to drill down into the data where a normal sunburst would slow the web browser hugely due to the
  sheer volume of data. Would be cool if I could re-populate the sunburst DataFrame query with each level
  until it reached a point whereby the volume of data had no performance effect on the web browser

## Unfixed Bugs and Things To Improve

- A slider in the dashboard for hypothesis 1 would have allowed the customer to look at the hypothesis for
  other years
- streamlit likes making sure containers cannot fill entire height of the screen, there is a good inch left
  it will not let me use with a single container so put two others in to fill the gap!
- streamlit likes having narrow scrollbars which can make scrolling difficult
- Would like to see if I can get the ML feature engineering into the pipeline, getting the ML to work took
  such a long time I didn't get the chance to try it!

## More Reflections

Creating the streamlit dashboard was fun! Having some very basic knowledge of HTML and CSS helped me to understand how streamlit structures its pages. I found making the assumption that streamlit containers were the same as HTML DIVs, and the KEY attribute was the same as HTMLs ID worked well when it came to structuring the page. Also having a basic design document for the dashboard was great in ensuring the visisualisation of the dashboard had a conformity - a standard.

While the machine learning part was quite hard, soley due to how models handle dates and the issues that occur when trying to use dates as a feature. THis utimately lead me to ask chtGPT for ideas as the standard methodoloy we were taught in the course produced seriously poor results.

Would have been nice if we had done just one example whereby we predicted something using a date range...

Still I now have a template to do it, and am focused on using and honing that template to make it more accurate. What I like about gettting code ideas that work from other sources is it give me someting to analyse and learn how it works so I can "make the code my own".

Having more experience with plotting and plot types this time around allowed me more time to think of hypothesis without subconciously limiting them by my ability to create plots! This led to some outlandish hypothesis that I would fettle into something more presentable. If I could have found a way to successfully handle sunburst plot click events could have created a monsterous visualisation that would have given substantial granularity to the data, but the way that streamlit works i.e. re-runs the page everytime something happens makes that a vertical technical challenge.

Looking back I think the elements of each project I enjoyed the most were the ETL, EDA and the documenatation. If it was possible to actually present the project to my peers that would have been fun as well, as sharing the data story would have made "come alive" and preparing for that presentation would have
honed the tone of the project, so I created the report as though it was to be used in a live presentation to try and give some energy and flow to the project.

## Credits

- chatGPT really good for solving issues so far everything suggested worked!
- StackOverlfow what a machine did not know these people did!

## Acknowledgements (optional)

- Thank the people who supported this project and didn't laugh too loud at the speeling mistooks
