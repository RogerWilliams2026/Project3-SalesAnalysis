# Analysis and Conclusion

The customer required insights into key performance areas of the business, and this analysis provides a comprehensive look at the customers questions and visualises the answers in a clear and concise manner.

This document provides insights into the performance of the business in key areas such as: sales trends and territory performance.

All analysis is done as requested based on the last 12 months of data unless otherwise stated.

Analysis Produced:

- What were the highest sales per territory for last year?
- Who were the top 20 customers by sales for last year?
- Who were the bottom 20 customer by sales for last year?
- What was the total amount of credits issued for last year by customer?
- What was the percentage of ship methods used last year?
- What were the total sales per customer per territory for last year?
- What was the sales by product family for last the two years?
- What are the predicted sales per month for next year?
- What are the predicted sales per territory for next year?

## The Journey

The journey to create this data story has been an interesting one. Providing me with lots of challenges and learning opportunities while colating the data and presenting it here for your edification.

## The Analysis

**First Question Asked: What Were The Highest Sales Per Territory For Last Year?**

Let us look at the visualisation that answers that question:

![no image](/reports/Images/Hypothesis1_plotly.png)

Simple but effective reporting, clearly show the most lucrative territories, could be used for targeted marketing for those areas with low sales.

As we can see 'Non EU' is the primary territory with 'Northwest' and 'EU' next closest in sales. Where as territories 'none' and 'services' are quite low, do these territories _need_ to be in the data as they seem ambiguous names?

The rest of the territories hover around the 12-20K mark which show steady sales across the boarrd, which is a good sign for maintaining a healthy business, but perhaps a marketing push in the sub 12K areas could be beneficial to raise sales.

**Second Question Asked: Who Were The Top 20 Customers By Sales For Last Year?**

Let us analyse the visualisation that answers that question:

![no image](/reports/Images/Hypothesis2_plotly.png)

Very clear plot, the simplicity of the visualisation allows us to grasp the gravity of the data shown.

Customers 628 and 1028 are the top 2 customers by a huge margin, could be an interesting investigation to see what territories they are in, it does ponder some more questions for more insights:

- Do they spread across multiple territories or are they concentrated in just one geo-location?
- Are they a single business or a conglomerate of businesses?
- Are they a head office of a larger business with multiple branches?

The average sales amongst the rests sits around 120-130K which is healthy figure.

Customers with IDs starting with 'S' are not fairing as well as the other customers, would be interesting to see what sales territories they are for, a marketing push is due perhaps?

**Third Question Asked: Who Were The Bottom 20 Customers By Sales For Last Year?**

Let us analyse the visualisation that answers that question:

![no image](/reports/Images/Hypothesis3_plotly.png)

Answers the hypothesis, clean, simple, direct and potentially shocking!

This plot shows quite a significant result, the plot sales here are not shown it 1,000s but £s!

Questions This Data Poses:

- Is there a real business need to entertain sales of such low sales values from customers?
- Are these customers viable to keep based on last years turnover from them?
- Why are there so many of them?
- What practicies are in place to reduce such customers?

**Fourth Question Asked: What Was The Total Amount Of Credits Issued For Last Year By Customer?**

Let us analyse the visualisation that answers that question:

![no image](/reports/Images/Hypothesis4_plotly.png)

Answers the hypothesis, nice and simple.

What is good is that the amount of credit memos issued is _signifiantly_ lower than mean sales which is a great metric to have.

In plain English it means you are not 'giving away' a large percentage of profit due to issues requiring credit memo adjustments which suggest strong business practicies in quality control and customer service.

**Question Five Asked: What Was The Percentage Of Ship Methods Used Last Year?**

Let us analyse the visualisation that answers that question:

![no image](/reports/Images/Hypothesis5_plotly.png)

Nice plot, again easy to see,

We can see that export delivery is most popular followed by UK carrier.

Question is UK carrier an actual company or a generic placeholder?

If it is might be worth considering segregating the data so when a customer places an order instead of recording 'UK carrier' record the ACTUAL carrier name.

If you hover the muouse a section it will also show the total invoices for that ship method, which is a nice touch.

![no image](/reports/Images/Hypothesis5a_plotly.png)

**Question Six Asked: What Were The Total Sales Per Customer Per Territory For Last Year?**

Nice interactive plot:

![no image](/reports/Images/Hypothesis6a_plotly.png)

Non EU, house account and northwest are the biggest territories with customers 628, 1028 being the largest.

Hovering over a territory shows the total sales for that territory:

![no image](/reports/Images/Hypothesis6b_plotly.png)

Hovering over a customer shows the total sales for that customer:

![no image](/reports/Images/Hypothesis6c_plotly.png)

Double clicking on a territory will zoom in on that territory, and double clicking again will zoom out:

![no image](/reports/Images/Hypothesis6d_plotly.png)

This a great way to explore the data as there are so many customer invoices per month such as in Jaunary over 838 customers purchased items/services, too much to show in a normal chart but with this visualisation if becomes an easy task to find answers to the hypothesis asked.

**Question Seven Asked: What Were The Sales By Product Family For Last The Two Years?**

This is a great question for analysis, let look at the chart:

![no image](/reports/Images/Hypothesis7_plotly.png)

We can see consistently Electronic Components, Fire Products, Odet, Pescara and Arc are high sellers.

The overall trend is quite stable which is a good business sign, with some areas such as Arrian, M-Range and Odet showing increased growth compared to the previous year.

Might be worth looking at the sub 10K product families and checking with previous years to see if sales are consistently low or that they should be for some buiness reason, if not then perhaps a marketing push is required to increase sales in those product famiilies or even a cull of the least profitable ones.

**Question Eight Asked: What Are The Predicted Sales Per Month For Next Year?**

We started to answer this question by using a machine learning model to predict next years sales based on the last 12 months of data, but first we needed to test models to see which was the best it, typically it is a choice between linear regression and random forest, we tested both.

First was to test the linear regression model by askig it to predict 2017s sales based on data from 2011-2016, the results are shown here:

![no image](/reports/Images/linear_regression_hypothesis8_test_forecast.png)

As we can see the predicted values start off reasonably close but veer off dramatically quite quickly and ends in a surprising downward motion.

I would not recommend using this model, it is here for contrast only!

Now let us see what the random forest model predicted:

![no image](/reports/Images/forest_regression_hypothesis8_test_forecast.png)

This models results are a lot more stable than the previous shows a more refined curve that matches the actual values more closely.

Now lets us get to the exciting bit! Not let us see what linear regression predicted 2018 saves by month would be:

![no image](/reports/Images/linear_regression_hypothesis8_predictions_forecast.png)

This model produces a plot more like a hill than the previous plots using actual data, if this was true either the economy is suddenly going into a deep recession or the company is planning to close its doors permenently!

Included for comparison only.

Let us see what random forest predicted for 2018:

![no image](/reports/Images/forest_regression_hypothesis8_predictions_forecast.png)

Looks a lot closer to historical data, unlike the Linear Regression model. use this as a _suggested_ sales prediction for 2018, it is only a prediction and not cast iron fact.

**Question Nine Asked: What are the predicted sales per territory for next year?**

We started to answer this question by using a machine learning model to predict next years sales based on the last 12 months of data, but first we needed to test models to see which was the best it, typically it is a choice between linear regression and random forest, we tested both.

First was to test the linear regression model by askig it to predict 2017s sales based on data from 2011-2016, the results are shown here:

![no image](/reports/Images/linear_regression_hypothesis9_test_forecast.png)

The prediction model is close to the original but it also has NEGATIVE values not in the original data so I am urged to ignore this model.

Lets have a look at Random Forest and see if that is closer

![no image](/reports/Images/forest_regression_hypothesis9_test_forecast.png)

This models results are a lot more stable than the previous models andshows no negative values.

Now lets us get to the exciting bit! Not let us see what linear regression predicted 2018 saves by month would be:

![no image](/reports/Images/linear_regression_hypothesis9_predictions_forecast.png)

This model produces NEGATIVE values for a prediction where the actual data is largely free of negative values this is not a good sign, and therefore not a good model, but put here for comparison.

Included for comparison only.

Let us see what random forest predicted for 2018:

![no image](/reports/Images/forest_regression_hypothesis9_predictions_forecast.png)

Much closer to historic data, no negative values and strong in a lot of areas the actual data is.

I would suggest using this model and remember it is only a prediction and not cast iron fact.

## Conclusion

The brief was to perform analysis based on a 12 month dataset looking at many contributing factors that can affect business profitability and performance such as drop in sales by large territory and amasing of credit memos over time, as well as predicting next years global sales figures by month and territory.

This small glimpse into these factors yields interesting insights and starts conversations as to how and why and identifies operational factors that could be affecting or enhancing performance.

Questions are raised such as why are there only two large customers and what steps are made to ensure that smaller customers (sub 10K) are not being neglected and what steps are being taken to ensure that they are not lost to competitors?

Sales seem focused heavily in the non EU area, and to a lesser degree the UK market, with the obvious success in the non EU territories, is there a marketing opportunity to increase sales in the EU by perhaps using UK contacts/marketing insights to promote the brand more there?

Interesting questions can be asked about the 20 top and bottom performing customers, which could give valuable insights into how effective marketing is for certain customer types and how to improve sales performance, other factors such as local economic conditions which could effect customers buying habits and how are these metrics measured by the business?

The interactive visualisations provide a powerful tool for exploring the data story and excruding insights from data provided. Allowing managers to identify trends, investigate individual customers, analysis as to the true effectiveness of certain product families, as well measure the actual effect crdit memos have on the bottom line. These tools provide evidence based insights by taking complex data and presenting it in a clear concise manner.

While several meaningful insights have been attained it does not establish causality. Variables such as competition, local economic conditions, and customer demographics were outside the scope of this project, and could also impact (if not actually) sales performance.

Future analysis incorporating these factors would provide a more comprehensive understanding of the drivers of profitability and valuable insights into their cause and effect. It would be also interesting to look more into the product side of the business and look at whether large volumes of more affordable products are via for sustained sales in comparison to more expensive products with lower volumes when seasonal trends occur.

Overall the analysis provides clear evidence that product family popularity, customer demographics, and seasonal trends all contribute to variations in sales performance.

These insights can be used for inventory planning, marketing strategies, and identify opportunities to improve the performance of individual stores and perhaps even regional expansion.

By continuing to build upon these findings with more detailed regional and operational analysis, the business can make better informed strategic decisions and further enhance profitability with the goal of expanding market share, profit margins and overall business growth while exploiting potential marketing opportunities both for sales and public exposure.
