# Project 3 - Sales Analysis

Project is a data analysis project that sales data to answer business questions and validate hypotheses. The project involves data cleaning, transformation, and visualisation using Python and various libraries.



# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset Content

Dataset package given by customer contains 1 related raw CSV file:

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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VisualisationFiles <- Contains a combined csv file for visualisation  
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
streamlit <- contains files needed for Heroku to show streamlit dashboard  
&nbsp;&nbsp;&nbsp;&nbsp;assets:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;css <- Contains file: style.css for streamlit  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;csv/Data <- Contains csv files for visualisation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pipelines - machine learning pipelines (copy from main project folder)

**Jupyter_Notebooks:**

ETL/EDA etc are purposely put into separate Jupyter notebooks for ease of use and debugging!


**Notebook Files:**

- Notebook_EDA_Sales_DataSet.ipynb <- EDA for Sales_Combined_Dataset_Visualization.csv
- Notebook_Notebook_ETL_Sales_DataSet.ipynb <- ETL for Sales_InvoiceData.csv
- Notebook_ML.ipynb <- Contains the machine learning model for experimentation has own visualisations
- Notebook_Visualisations1.ipynb <- Contains the visualisations for the hypotheses
- Notebook_Visualisations2.ipynb <- Contains the visualisations for the hypothesis for ML

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

In GitHub there is a KANBAN project, that was used for project management, used the road map feature to show required completion dates
for various aspects e.g. ETL.

**Dashboard**

The dashboard is available via Heroku at this URL:

  

**GitHub**

Project GitHub URL is:

https://github.com/RogerWilliams2026/Project3-SalesAnalysis.git




### Using The Notebooks

In order to create the combined csv file and see the plots these notebooks need to be run in order from the Jupyter_notebooks folder:

- Notebook_ETL_Sales_DataSet.ipynb <- ETL for Sales_DataSet.csv
- Notebook_EDA_Sales_DataSet.ipynb <- Contains the EDA for the combined csv file
- Notebook_ML.ipynb <- Contains the machine learning model for experimentation has own visualisations
- Notebook_Visualisations1.ipynb <- Contains the visualisations for the hypotheses
- Notebook_Visualisations2.ipynb <- Contains the visualisations for the hypothesis for ML

## Business Requirements

A requirement for a wider view of sales performance in the business in key areas, including sales by territories and product families.

Special interest was shown in sales by territory and I got the feeling they are keen to identify profitable and less profitable customer
by sales territory, as well as the amount of credits given to each customer and other analysis around it.

The customer hopes this information will help it plan its store growth and marketing strategies to maximise profits in the areas that are shown to be profitable, but also focus on improvement for the stores that are not performing well.

## Ethics and GDPR

The dataset contains a filed of contact names and a field of customer names. based on the premise this data is going to be 
available via a public dashboard will see if possible to create a login system so guest users will only see customer ID
and authorised users will be able to see the customer names.


## Hypothesis and How To Validate?

- What were the highest sales per territory for last year?
  Validation: Test with a suitable plot to show correlation between invoice amount sum and territory filtered for highest value

- *Who were the top 20 customers by sales for last year?
  Validation: Test with a suitable plot to show customer ID/name 

- Who were the bottom 20 customer by sales for last year?
  Validation: Test with a suitable plot to show customer ID/name 


- What was the total amount of credits issued for last year?
  Validation: Will show on same plot if possible, will divide into months for a more meaningful visualisation

- What was the percentage of ship methods used last year?
  Validation: Thinking of a simple pie plot as percentages used, might not sum to 100% though, will test and see

- *What were the sales per customer per territory for last year?
  Validation: Will show plot grouped by territory, then customer ID/name then month 

- What was the sales by product family for last the two years?
  Validation: Will show with a comparison plot with each year in a different colour, will divide into months for a more meaningful visualisation


Machine Learning Predictions:

- What are the predicted sales per month for next year?
  Validation: Test with linear regression and random forest to determine best model for hypothesis

- *What are the predicted sales per territory for next year?
  Validation: Test with linear regression and random forest to determine best model for hypothesis



* As data contains customer name as well as customer ID use customer ID as data will be public server




## Project Plan

- Acquire raw data as csv files from the customer
- Clean and transform the raw data into cleaned csv file
- Perform EDA to see if there are any correlations between the data and the hypotheses
- Visualise the data to validate the hypotheses and answer the business questions
  using multiple visualisation libraries to find best fit for the customer requirements
  as well as the best looking visualisations for clear insights into the data and choosing
  the most appropriate visualisation for the hypothesis being validated
- Use machine learning to predict sales for the next year and visualise the results
- Create a report to present the findings to the customer

## The Rationale Used To Map The Business Requirements To The Data Visualisations

_Hypothesis 1: Are sales increased if weather is hotter or colder in the last 12 months?_
Chose scatter plot to show the correlation between temperature and sales. Due to the large amount of data, a scatter plot is the best way to visualise the data and show the correlation.





## Analysis techniques used

From the initial csv file 3 more are created 4 via ETL as it goes through the ETL stages all end with an applied naming convention:


- Sales_InvoiceData_Cleaned.csv
- Sales_InvoiceData_Working.csv
- Sales_InvoiceData_Visualisation.csv

For machine learning 4 pipelines are created:


- forest_regression_hypothesis12_test_pipeline.pkl
- linear_regression_hypothesis12_pipeline.pkl
- forest_regression_hypothesis12_pipeline.pkl
- linear_regression_hypothesis12_test_pipeline.pkl


Files with _test_ in the name are used to run test "prediction" by getting machine learning processes
to "predict" values for an existing year. This is used to compare with the previous year via a plot

The other files are used in machine learning to predict the next years values, again shown in a plot

**Methods Used:**

Generative AI tools were mostly used to solve code issues and occasionally for plotting ideas due to my lack of experience with visualisation libraries particularly the first sunburst plot as I was unsure if my approach was the correct one.

Data was a limiting factor, not in terms of detail but sheer volume and breadth. I was stumped with some hypothesis by the fact I was trying to analyse sales data with 45 stores each with 97 departments and was lacking experience to know what plots and strategies are best to use to visualise this type data.

Adapted with a "best guess Mr Sulu" approach to visualising large data, running plot tests to see what the libraries can handle and go beyond, bar, histogram and scatter plots which worked well, as I could now use more effective plot types but ran out of time to reimagine the plots.

Analysed plots compared to hypothesis, by checking expected values against queries with the raw data. If the dataset to use is corrupt or incorrect the plot will be useless.

Discovered the features data set.csv file has 7 months of date values not in the other csv files, so that needed to be filtered before creating the combined csv file, easily achieved via a left join.

Decided to use both linear regression and random forest for the machine learning experiments, nice broad range of models that can be used with the data.

## Libraries Used

The requirements.txt has the full list, but here is a list taken from the Jupyter notebooks:

charset_normalizer
joblib  
matplotlib.pyplot  
matplotlib.ticker.
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
- Create cleaned csv files for each of the 3 raw csv files
- Merge the 3 cleaned csv files into a single csv file for visualisation
- Perform exploratory EDA to see if there are any correlations between the data and the hypotheses
- Visualise the data using all of the available plot libraries (where possible) to see which provide the
  best plot for the hypothesis I am testing. Then if have the time try and expand and develop them further
- Get data into a machine learning model for at least one hypothesis, choose example that could not achieved _without_ machine learning
- Choose best plots for each hypothesis (where there is a choice) to use in findings report
- Populate findings report with plots and analysis for each hypothesis and submit to customer

### Challenges and Strategies

- VS Code repeatedly has a kernel hang randomly during development requiring restarting VS Code  
  as kernel restart rarely fixes the issue
- Had issue with pandas not reading the csv file as it was not in UTF-8 format, chatGPT solved that issue and added new code
  into my ETL library to auto detect the csv file encoding
- Markdown markup language is irritating in that need to but two spaces at the end of line just to get it to keeps lines separate and most annoying of all it has no capacity for indenting!

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

## Who Won The Generative AI Battle?

chatGPT won hands down, I found Copilot in VS Code largely irritating and invasive, and it was not very good at solving code issues a bit of a mixed bag. chatGPT on the other hand was very good at solving code issues and providing code snippets that worked first time. When I went of the rails and without knowing it and was using the wrong approach to visualising one hypothesis. Copilot's suggested plot was cramped, difficult to read and (as I discovered) the wrong plot type for the data.

Posted the code into chatGPT and over an hour it honed and rehoned the code to a 92% working solution with a better type of plot. Due to the massive size of the data it caused many rendering issues such as a huge gap between the plot title and the first actual plot and missing x axis labels.

Which of course after a good nights sleep I realised _I_ was using the wrong plot _and_ data visualisation concept and looking at the data visualisation backwards!

Did notice as time has gone by CoPilot in VS Code is making a lot more mistakes, might be better off if Microsoft concentrated on making
an expert system version instead...

## Things To Learn Next

- Proper use of KANBAN for project management (there s a rumour it supports sprints..)
- Better understanding of the plotly.express library and its options for visualisation
- Better understanding interactive plots and how determine which is best for the data being visualised
- More practice with machine learning, particularly with categorical data and dates

## Unfixed Bugs and Things To Improve

- Had strange issue with first plot in hypothesis 3, where it puts: 1e9 in the top left corner of the
  pyplot plot. No idea why. Will have a look if there is a solution if I have time does not affect plot data.
- Uniformity regardling currency symbols in plots!
- streamlit likes making sure containers cannot fill entire height of the screen, there is a good inch left
  it will not let me use with a single container so put two others in to fill the gap!
- streamlit likes having narrow scrollbars which can make scrolling difficult
- 3D scatter chart is too big in streamlit but if I adjust the size it cuts off some X axis values and does not show a scroll bar
- Would like to see if I can get the ML feature engineering into the pipeline, getting the ML to work took such a long time I didn't
  get the chance to try it!
- Need more date data, for some reason while the csv files contain thousands of records, the date range for the first two ends at
  26/10/2012 (!) and the 3rd in July 2013 (?). Discovered this too late to hunt around for another dataset..

## Credits

- chatGPT really good for solving issues so far everything suggested worked!
- StackOverlfow what a machine did not know these people did!

## Acknowledgements (optional)

- Thank the people who supported this project and didn't laugh too loud at the speeling mistooks
