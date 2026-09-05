import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import pathlib
import scipy.stats as stats
import matplotlib.pyplot as plt
import nbformat
from matplotlib.ticker import MultipleLocator
import numpy as np
import joblib
#
#  Created 05/09/2026 By Roger Williams
#  
# dashboard for sales analysis project
#  
#

#VARS

#file paths
CNST_STR_LINEAR_PIPELINE_HYPOTHESIS8_TEST_PATH =  "assets/pipelines/linear_regression_hypothesis8_test_pipeline.pkl"
CNST_STR_FOREST_PIPELINE_HYPOTHESIS8_TEST_PATH = "assets/pipelines/randomforest_hypothesis8_test_pipeline.pkl"

CNST_STR_LINEAR_PIPELINE_HYPOTHESIS8_PREDICTION_PATH =  "assets/pipelines/linear_regression_hypothesis8_predictions_pipeline.pkl"
CNST_STR_FOREST_PIPELINE_HYPOTHESIS8_PREDICTION_PATH =  "assets/pipelines/randomforest_hypothesis8_predictions_pipeline.pkl"

CNST_STR_LINEAR_PIPELINE_HYPOTHESIS9_TEST_PATH =  "assets/pipelines/linear_regression_hypothesis9_test_pipeline.pkl"
CNST_STR_FOREST_PIPELINE_HYPOTHESIS9_TEST_PATH = "assets/pipelines/randomforest_hypothesis9_test_pipeline.pkl"

CNST_STR_LINEAR_PIPELINE_HYPOTHESIS9_PREDICTION_PATH =  "assets/pipelines/linear_regression_hypothesis9_predictions_pipeline.pkl"
CNST_STR_FOREST_PIPELINE_HYPOTHESIS9_PREDICTION_PATH =  "assets/pipelines/randomforest_hypothesis9_predictions_pipeline.pkl"
                                              
CNST_STR_SALES_DATASET = "assets/csv/Data/VisualisationFiles/Sales_InvoiceData_Visualisation.csv"
CNST_STR_SALES_GROUPBY_CUSTOMER_DATASET = "assets/csv/Data/VisualisationFiles/Sales_InvoiceData_GroupedByCustomer_Visualisation.csv"
CNST_STR_SALES_GROUPBY_TERRITORY_DATASET = "assets/csv/Data/VisualisationFiles/Sales_InvoiceData_GroupedByTerritory_Visualisation.csv"

#sidebar radio button control
radRadioButtons = None
#containers 
conContainerMain = None
conMainFooter1 = None
conMainFooter2 = None

conContainerEthicsMain = None
conContainerEthicsSub = None
conContainerTab2_Sub = None
conContainerTab3_Sub = None
conContainerTab4_Sub = None
conContainerTab5_Sub = None
conContainerTab6_Sub = None
conContainerTab7_Sub = None
conContainerTab8_Sub = None
conContainerTab9_Sub = None
conContainerTab10_Sub = None
conContainerTab11_Sub = None
conContainerTab12_Sub = None
conContainerTab13_Sub = None
conContainerTab14_Sub = None
conContainerTab15_Sub = None
conContainerTab16_Sub = None
conContainerTab17_Sub = None
conContainerTab18_Sub = None
conContainerTab19_Sub = None

conSection1 = None
conSection2 = None
conSection3 = None
conSection4 = None
conSection5 = None
conSection6 = None
conSection7 = None
conSection8 = None

conSection1Title = None
conSection2Title = None
conSection3Title = None
conSection4Title = None
conSection5Title = None
conSection6Title = None
conSection7Title = None
conSection8Title = None
conSection9Title = None
conSection10Title = None

conSectionEthicsTitle = None

conSection1Tab = None
conSection2Tab = None
conSection3Tab = None
conSection4Tab = None
conSection5Tab = None
conSection6Tab = None
conSection7Tab = None
conSection8Tab = None
conSection9Tab = None
conSection10Tab = None 

conSectionFooter1 = None
conSectionFooter2 = None
conSectionFooter3 = None
conSectionFooter4 = None
conSectionFooter5 = None
conSectionFooter6 = None
conSectionFooter7 = None
conSectionFooter8 = None
conSectionFooter9 = None
conSectionFooter10 = None
conSectionFooter11 = None
conSectionFooter12 = None
conSectionFooter13 = None
conSectionFooter14 = None
conSectionFooter15 = None
conSectionFooter16 = None
#tab 1
conOverview = None

expExpander1 = None
expExpander2 = None
expExpander3 = None
expExpander4 = None
expExpander5 = None
expExpander6 = None
expExpander7 = None
expExpander8 = None
expExpander9 = None
expExpander10 = None
expExpander11 = None
expExpander12 = None
expExpander13 = None
expExpander14 = None
expExpander15 = None

tabTab1 = None
tabTab2 = None
tabTab3 = None
tabTab4 = None
tabTab5 = None
tabTab5 = None
tabTab6 = None
tabTab7 = None
tabTab8 = None
tabTab9 = None
tabTab10 = None
tabTab11 = None
tabTab12 = None
tabTab13 = None
tabTab14 = None
tabTab15 = None
tabTab16 = None
tabTab17 = None
tabTab18 = None
tabTab19 = None


#sliders for user interaction
sldSliderFrom1 = None
sldSliderFrom2 = None

#DataFrames vars for csv files for ML
dfSales_InvoiceData_GroupByCustomer = pd.DataFrame()
dfSales_InvoiceData_GroupByTerritory = pd.DataFrame()
dfSalesDataML_Temp = pd.DataFrame()

#DataFrames vars
dfSales_InvoiceData = pd.DataFrame()
dfSales_InvoiceData_Temp = pd.DataFrame()
dfSales_InvoiceData_Work = pd.DataFrame()
dfSales_DataSet_Filtered = pd.DataFrame()
dfSalesDataML_Work = pd.DataFrame()



#other vars
objPipeline = None
ax = None
fig = None

 
# Function to load custom CSS
def funcLoadCSS(fileName):
    with open(fileName) as fileCSS:
        st.markdown(f"<style>{fileCSS.read()}</style>", unsafe_allow_html=True)


#******** main code ********
import os
dfSales_InvoiceData = pd.read_csv(CNST_STR_SALES_DATASET)
dfSales_InvoiceData_GroupByCustomer = pd.read_csv(CNST_STR_SALES_GROUPBY_CUSTOMER_DATASET)
dfSales_InvoiceData_GroupByTerritory = pd.read_csv(CNST_STR_SALES_GROUPBY_TERRITORY_DATASET)
#try and load csvs from assets folder

#convert InvoiceDate to datetime
dfSales_InvoiceData["InvoiceDate"] = pd.to_datetime(dfSales_InvoiceData["InvoiceDate"], format="%d/%m/%Y")

# #convert InvoiceID to string
# dfSales_InvoiceData["InvoiceID"] = dfSales_InvoiceData["InvoiceID"].astype(str)


#init streamlit dashboard 
# Load the CSS file
funcLoadCSS(pathlib.Path("assets/css/style.css") )

#configure streamlit page
st.set_page_config(
   page_title = "Sales Analysis",
   page_icon =":temperature:",
   layout = "wide",
   initial_sidebar_state = "expanded"
)
 
st.session_state.sidebar_state = 'expanded'
 
# if: @st.cache_data  - put before function means if run any results are reused i.e. on loading data

st.title("Sales Analysis")
st.subheader("What We See In The Data")

#create page controls container why will it not stretch to fill the page???
conContainerMain = st.container(border=True, width="stretch", key="conMain", height="stretch" ) #height=780

#create footer container
conMainFooter1 = st.container(border=True, width="stretch", key="conMainFooter1", height=40 )
conMainFooter1.write("Created by Roger Williams - 2026")
conMainFooter2 = st.container(border=True, width="stretch", key="conMainFooter2", height=50 )
conMainFooter2.write("Each Page With A Plot Has A Data Table and Description - Use Scroll Bar On Right (Or Mouse Wheel If It Is Not Visible)" +
                     "To Move Down and See All Contents If Only Plot Visible")

#create sidebar
st.sidebar.title("Analysis Options",width="content",anchor="left")

#add radio button group for options
radRadioButtons = st.sidebar.radio("Select:", ["Overview", "Hypothesis 1 -4", "Hypothesis 5 - 7",  
                                               "ML Hypothesis 8", "ML Hypothesis 9", "Ethics & Data Privacy"], 
                                   index=0, key="radRadioButtons")

if st.button("🔄 Reset UI"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.rerun()
    
#populate container with page controls
match radRadioButtons:
   case "Overview":
        conOverview = conContainerMain.container(border=False, width="stretch", key="conSection1", height=860) 
        # conContainerMain.markdown("<div style='background-color:#222; color:#00FF00; padding:10px; border-radius:5px;'>"
        #  "This is green text on a dark background"
        #  "</div>",
        #  unsafe_allow_html=True)
        conOverview.info("Overview")
        conOverview.markdown("### Purpose of The Analysis")
        conOverview.write("Provides insights into the performance of the business in key areas such as: " +
                          "sales trends and the impact of various external factors on sales.")
        conOverview.write("All analysis is done as requested based on the last 12 months of data")
        conOverview.write()
        conOverview.write("Analysis Produced:")
        conOverview.write("What were the highest sales per territory for last year?")
        conOverview.write("Who were the top 20 customers by sales for last year?")
        conOverview.write("Who were the bottom 20 customer by sales for last year?")
        conOverview.write("What was the total amount of credits issued for last year?")
        conOverview.write("What was the percentage of ship methods used last year?")
        conOverview.write("*What were the sales per customer per territory for last year?")
        conOverview.write("What was the sales by product family for last the two years?")
        conOverview.write("What are the predicted sales per month for next year?")
        conOverview.write("What are the predicted sales per territory for next year?")
   
        
   case "Hypothesis 1 -4": 
 #******tab 1*******  
        #plotly visualisation for hypothesis 1 - are sales increased if weather is hotter or colder in the last 12 months? 
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher

        conSection1 = conContainerMain.container(border=False, width="stretch", key="conSection1", height=860)
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab1, tabTab2, tabTab3, tabTab4 = conSection1.tabs([
           "Hypothesis 1", "Hypothesis 2", "Hypothesis 3", "Hypothesis 4"
        ])   
   
        conSection1Tab = tabTab1.container(border=True, width="stretch", height=780)         
        conSection1Title = conSection1Tab.container(border=False, width="stretch", key="conSection1Title", height=40)
        conSection1Title.info("What Were The Highest Sales Per Territory For Last Year?")

        #visualisation for hypothesis 1 - what were the highest sales per territory for last year?

        #get 12 months from last date in DataFrame
        dteStartDate = dfSales_InvoiceData["Year"].max() -1

        #filter DataFrame for last 12 months
        dfSales_DataSet_Filtered = dfSales_InvoiceData[dfSales_InvoiceData["Year"] == dfSales_InvoiceData["Year"].max() -1]

        #create new DataFrame with one TerritoryCodes entry per YearMonth with the MAX InvoiceAmt in it
        dfSales_DataSet_Temp = dfSales_DataSet_Filtered.groupby(["TerritoryCodes"], as_index=False)["InvoiceAmt"].max()                                                                 
         
        fig = px.scatter(dfSales_DataSet_Temp,
             x="TerritoryCodes",
             y="InvoiceAmt",
             title="Highest Sales Per Territory For Last Year Over Last 12 Months",
             labels={
               "TerritoryCodes": "Territory Codes",
               "InvoiceAmt": "Invoice Amount"
             },
             #set plot size
             height=500,
             width=1050,
         )

        fig.update_layout(title_x = 0.35,             #make axis labels readable
               xaxis=dict(tickangle=90),
               xaxis_color="white",
               yaxis_color="white", 
               plot_bgcolor="#070707", 
               paper_bgcolor ="#070707"
             )
        fig.update_yaxes(minor=dict(
             ticks="outside",
             ticklen=6,
             dtick=2000
             ))
 
        conSection1Tab.plotly_chart(fig, use_container_width=True, key="figTab1") 
        
        expExpander1 =  conSection1Tab.expander("Show Data Used For Plot", expanded=False, key="expExpander1")
        expExpander1.dataframe(dfSales_DataSet_Temp, use_container_width=True)
        conSection1Tab.write("Note: in order for the 'ticks' to show on the axes Plotly needs to be version 5.8 or higher") 
   
        conSectionFooter1 = conSection1Tab.container(border=False, width="stretch", key="conSectionFooter1", height=400)
        conSectionFooter1.write("As we can see Non EU is the primary territory with Northwest and EU next closest in sales.")
        conSectionFooter1.write("The rest of the territories hover around the 17-20K mark")
        conSectionFooter1.write("Suggest a big marketing push to raise Midlands sales across the board")
         
 
 #******tab 2*******   
        #plotly visualisation for hypothesis 2 - Sales Differences Between holiday and Non Holiday Weeks per Store Over last 12 Months
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab2_Sub = tabTab2.container(border=True, width="stretch", key="conTab2Sub", height=780)
        conContainerTab2_Sub.info("Who Were The Top 20 Customers by Sales for Last Year?")
 
        #first filter by last year (2016)
        dfSales_DataSet_Filtered = dfSales_InvoiceData[dfSales_InvoiceData["Year"] == dfSales_InvoiceData["Year"].max() -1]

        #to stop customer being shown who have NO sales delete all records where InvoiceAmt is 0
        dfSales_DataSet_Filtered = dfSales_DataSet_Filtered[dfSales_DataSet_Filtered["InvoiceAmt"] > 0]

        #group by CustomerID and get sum of InvoiceAmt
        dfSales_DataSet_Filtered = (
           dfSales_DataSet_Filtered
           .groupby("CustomerID")["InvoiceAmt"]
           .sum()
           .sort_values(ascending=False)
           .head(20)
           .reset_index()
        )

        #sort data
        dfSales_DataSet_Filtered.sort_values("InvoiceAmt", ascending=False)

        fig = px.bar(
           dfSales_DataSet_Filtered.head(20),
           x="CustomerID",
           y="InvoiceAmt",
           color="InvoiceAmt",
           color_continuous_scale="Solar",
           title="Top 20 Customers By Sales For Last 12 Months"
        )

        fig.update_layout(
            xaxis_title="Customer ID",
            yaxis_title="Total Sales (£)",
            coloraxis_colorbar=dict(title="Total Sales (£)"),
            template="plotly_white",
            title_x=0.3,
            title_font=dict(size=20, family="Arial", color="white"),
            xaxis_color="white",
            yaxis_color="white", 
            plot_bgcolor="#070707", 
            paper_bgcolor ="#070707"            
         )
        
        fig.update_yaxes(minor=dict(
             ticks="outside",
             ticklen=6,
             dtick=20000
             ))                      
                        
        conContainerTab2_Sub.plotly_chart(fig, use_container_width=True, key="figTab2") 
        expExpander2 =  conContainerTab2_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander2")
        expExpander2.dataframe(dfSales_DataSet_Filtered.head(20), use_container_width=True)         
  
        conSectionFooter2 = conContainerTab2_Sub.container(border=False, width="stretch", key="conSectionFooter2", height=400)
        conSectionFooter2.write("Custmers 628 and 1028 are the top 2 customer by a huge margin." +
                                "The average sales amoungst the rests sits around 110-130K.")
        conSectionFooter2.write("Customers with IDs starting with 'S' are not fairing as well as the other customers, " +
                                "would be interesting to see what sales territories they are for, a marketing push perhaps?")

#******tab 3a******  
        #plotly visualisation for hypothesis 3 - What is most profitable store type over the last 12 months?
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab3_Sub = tabTab3.container(border=True, width="stretch", key="conTab3aSub", height=780)
        conContainerTab3_Sub.info("Who Were The Bottom 20 Customer by Sales for Last Year?")

       #first filter by last year (2016)
        dfSales_DataSet_Filtered = dfSales_InvoiceData[dfSales_InvoiceData["Year"] == dfSales_InvoiceData["Year"].max() -1]

        #to stop customer being shown who have NO sales delete all records where InvoiceAmt is 0
        dfSales_DataSet_Filtered = dfSales_DataSet_Filtered[dfSales_DataSet_Filtered["InvoiceAmt"] > 0]

        #group by CustomerID and get sum of InvoiceAmt
        dfSales_DataSet_Filtered = (
           dfSales_DataSet_Filtered
           .groupby("CustomerID")["InvoiceAmt"]
           .sum()
           .sort_values(ascending=False)
           .tail(20)
           .reset_index()
        )

        #sort data
        dfSales_DataSet_Filtered.sort_values("InvoiceAmt", ascending=False)

        fig = px.bar(
           dfSales_DataSet_Filtered.tail(20),
           x="CustomerID",
           y="InvoiceAmt",
           color="InvoiceAmt",
           color_continuous_scale="Solar",
           title="Bottom 20 Customers By Sales For Last 12 Months"
        )

        fig.update_layout(
            xaxis_title="Customer ID",
            yaxis_title="Total Sales (£)",
            coloraxis_colorbar=dict(title="Total Sales (£)"),
            template="plotly_white",
            title_x=0.3,
            title_font=dict(size=20, family="Arial", color="white"),
            xaxis_color="white",
            yaxis_color="white", 
            plot_bgcolor="#070707", 
            paper_bgcolor ="#070707"            
         )
        
        fig.update_yaxes(minor=dict(
             ticks="outside",
             ticklen=6,
             dtick=2
             ))                      
                          
          
        conContainerTab3_Sub.plotly_chart(fig, use_container_width=True, key="figTab3") 
        expExpander3 =  conContainerTab3_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander3")
        expExpander3.dataframe(dfSales_DataSet_Filtered.tail(20) , use_container_width=True)         
        conSectionFooter3 = conContainerTab3_Sub.container(border=False, width="stretch", key="conSectionFooter3", height=400)   
        conSectionFooter3.write("This plot shows quite a significant result, the plot sales here are not shown it 1,000s but £s!")
        conSectionFooter3.write("Questions This Data Poses:") 
        conSectionFooter3.write("- Is there a real business need to entertain sales of such low values")
        conSectionFooter3.write("- Are these customers viable to keep based on last years turnover from them?")
                      
            
            
#*****tab 4*******
        #special plot for *all* customers with sales *below* zero!
        conContainerTab4_Sub = tabTab4.container(border=True, width="stretch", key="conTab4Sub", height=780)
        conContainerTab4_Sub.info("Who Were The Bottom 20 Customer by Sales for Last Year?")
  
        #first filter
        # by last year (2016)
        dfSales_DataSet_Filtered = dfSales_InvoiceData[dfSales_InvoiceData["Year"] == dfSales_InvoiceData["Year"].max() -1]
        
        #to stop customer being shown who have NO sales delete all records where InvoiceAmt is 0
        dfSales_DataSet_Filtered = dfSales_DataSet_Filtered[dfSales_DataSet_Filtered["InvoiceAmt"] < 0]

        #group by CustomerID and get sum of InvoiceAmt
        dfSales_DataSet_Filtered = (
            dfSales_DataSet_Filtered
            .groupby("CustomerID")["InvoiceAmt"]
            .sum()
            .sort_values(ascending=False)
         #  .tail(20)
            .reset_index()
        )

        #sort data
        dfSales_DataSet_Filtered.sort_values("InvoiceAmt", ascending=False)

        fig = px.bar(
            dfSales_DataSet_Filtered.head(20),
            x="CustomerID",
            y="InvoiceAmt",
            color="InvoiceAmt",
            color_continuous_scale="Solar",
            title="All Customers With Negative Sales For Last 12 Months"
        )

        fig.update_layout(
            xaxis_title="Customer ID",
            yaxis_title="Total Sales (£)",
            coloraxis_colorbar=dict(title="Total Sales (£)"),
            template="plotly_white",
            title_x=0.3,
            title_font=dict(size=20, family="Arial", color="white"),
            xaxis_color="white",
            yaxis_color="white", 
            plot_bgcolor="#070707", 
            paper_bgcolor ="#070707" 
        )
 
        conContainerTab4_Sub.plotly_chart(fig, use_container_width=True) 
        expExpander4 = conContainerTab4_Sub.expander("Show Data Used For Plot", expanded=False, key=f"expExpander4")
        expExpander4.dataframe(dfSales_DataSet_Filtered.head(20), use_container_width=True)         

        conSectionFooter4 = conContainerTab4_Sub.container(border=False, width="stretch", key="conSectionFooter4", height=400)
        conSectionFooter4.write("An interesting visualisation as we can see customer with NEGATIVE sales values.")
        conSectionFooter4.write("These are due to credit memos, what is good is that the amount of credit memos is signifiantly " +
                                 "lower than mean sales which is a great metric.")
        conSectionFooter4.write("In plain English it means you are not 'giving away' a large percentage of profit due to issues" + 
                                 "requiring credit memo adjustments.")
        conSectionFooter4.write("In stores: 9, 19, 26, 37 all have high sales but store 26 is the highest. Further analysis of theses stores by" +
                                "_type_ could yield some fascinating insights.")                      
                                
         
   case "Hypothesis 5 - 7":                
  #******tab 5*******    

      
        conSection2 = conContainerMain.container(border=False, width="stretch", key="conSection2", height=860)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab5, tabTab6, tabTab7 = conSection2.tabs([
          "Hypothesis 5", "Hypothesis 6", "Hypothesis 7"
        ])
     
        conSection2Tab = tabTab5.container(border=True, width="stretch", height=780)
        conSection2Title = conSection2Tab.container(border=False, width="stretch", key="conSection2Title", height=40)
        conSection2Title.info("What Was The Percentage of Ship Methods Used Last Year?")
 
        # by last year (2016)
        dfSales_DataSet_Filtered = dfSales_InvoiceData[dfSales_InvoiceData["Year"] == dfSales_InvoiceData["Year"].max() -1]
        
        #create new DataFrame with one ShipMethod entry per YearMonth with the MAX InvoiceAmt in it
        dfSales_DataSet_Temp = dfSales_DataSet_Filtered.groupby(["ShipMethod"], as_index=False)["InvoiceAmt"].max()      
                                    
        #group by ShipMethodand get sum of InvoiceAmt
        dfSales_DataSet_Filtered = (
           dfSales_DataSet_Filtered
           .groupby("ShipMethod")["InvoiceAmt"]
           .sum()
           .sort_values(ascending=False)
           .reset_index()
        )

        fig = px.pie(
           dfSales_DataSet_Filtered,
           names="ShipMethod",
           values="InvoiceAmt",
           title="Percentage of Ship Methods Used Last Year",
           color_discrete_sequence=px.colors.qualitative.Set3,
           height=800,
           width=800,
           )                       
        
        fig.update_layout(
           title_x=0.3,
           title_font=dict(size=20, family="Arial", color="White")
        )
   
  
        conSection2Tab.plotly_chart(fig, use_container_width=True, key="figTab5") 
        expExpander5 =  conSection2Tab.expander("Show Data Used For Plot", expanded=False, key="expExpander5")
        expExpander5.dataframe(dfSales_DataSet_Filtered, use_container_width=True)         
        conSectionFooter5 = conSection2Tab.container(border=False, width="stretch", key="conSectionFooter5", height=400)
        conSectionFooter5.write("We can see that export delivery is most popular followed by UK carrier.")
        conSectionFooter5.write("Question is UK carrier an actual company or a generic placeholder?")
        conSectionFooter5.write("If it is might be worth considering segregating the data so when a customer places an order " +
                                "instead of recording 'UK carrier' record the ACTUAL carrier name.")
 
 #******tab 6*******  
        #What were the sales per customer per territory for last year?
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab6_Sub = tabTab6.container(border=True, width="stretch", key="conTab6Sub", height=800)
        conContainerTab6_Sub.info("What Were The Sales Per Customer Per Territory For Last Year?")

        # by last year (2016)
        dfSales_DataSet_Filtered = dfSales_InvoiceData[dfSales_InvoiceData["Year"] == dfSales_InvoiceData["Year"].max() -1]
        intStartYear = dfSales_InvoiceData["Year"].max() -1

        # Remove zero/negative amounts
        dfSales_DataSet_Filtered  = dfSales_DataSet_Filtered [dfSales_DataSet_Filtered ["InvoiceAmt"] > 0]

        fig = px.sunburst(
           dfSales_DataSet_Filtered,
           path=[
              "TerritoryCodes",
              "CustomerID",
              "Month",
              "InvoiceID"
           ],
           values="InvoiceAmt",
           color="InvoiceAmt",
           color_continuous_scale="Solar",
           title=f"Sales Per Customer Per Territory For {intStartYear}",
           height=800,
           width=800,
           hover_data={
              "InvoiceAmt": ":,.2f",
              "TerritoryCodes": True,
              "CustomerID": True,
              "Month": True,
           }
        )

        fig.update_layout(
           title_x=0.5,
           title_font=dict(
              size=20,
              family="Arial",
              color="black"
           )
        )

        fig.update_traces(
           hovertemplate=
              "Invoice Amount: £%{customdata[0]:,.2f}<br>" +
              "Territory: %{customdata[1]}<br>" +
              "Customer: %{customdata[2]}<br>" +
              "Month: %{customdata[3]}<br>" +
              "<extra></extra>"
        )
 
        conContainerTab6_Sub.plotly_chart(fig, use_container_width=True, key="figTab6") 
        expExpander6 = conContainerTab6_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander6")
        expExpander6.dataframe(dfSales_DataSet_Filtered, use_container_width=True)         
        conSectionFooter6 = conContainerTab6_Sub.container(border=False, width="stretch", key="conSectionFooter6", height=400)
        conSectionFooter6.write("This is a nice detailed yet not too complex visualisation that just as you have discovered is the same methodology")
        conSectionFooter6.write("as the previous visualisation in that it is interactive, so we can \"drill down\" into finer detail.")
        conSectionFooter6.write("As we can see when we hover the mouse over a markdown section we can see the store number, the markdown amount" +
                                "and the sales for that store during the holiday period.")
        conSectionFooter6.write("When we double click on a store number we can see detailed markdown information for the store:")
        conSectionFooter6.write("Interactive insights are great when dealing (as we are) with a lot of data e,g. number of stores and their" +
                                "departments, and act as a great presentation tool for internal Q&A session regarding store performance and" +
                                "profitability.")   
     
 
 #******tab 7*******  
        #What Was The Sales By Product Family For Last The Two Years?
        #Note: last year in data is: 2012
      
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab7_Sub = tabTab7.container(border=True, width="stretch", key="conTab7Sub", height=780)
        conContainerTab7_Sub.info("What Are The Most Profitable Departments Per Store In The Last 12 Months?")
 
        # by last year (2016)
        intStartYear = dfSales_InvoiceData["Year"].max() -1
        intEndYear = dfSales_InvoiceData["Year"].max()
        #filter DataFrame for last 12 months
        dfSales_DataSet_Filtered = dfSales_InvoiceData[dfSales_InvoiceData["Year"] >= dfSales_InvoiceData["Year"].max() -1]

        #remove zero/negative amounts
        dfSales_DataSet_Filtered  = dfSales_DataSet_Filtered [dfSales_DataSet_Filtered ["InvoiceAmt"] > 0]

        #sort by year
        dfSales_DataSet_Filtered = dfSales_DataSet_Filtered.sort_values(by=["Year"], ascending=[True])

        #group by CustomerID and get sum of InvoiceAmt
        dfSales_DataSet_Filtered = (
            dfSales_DataSet_Filtered
            .groupby(["Year", "ProductFamily"])["InvoiceAmt"]
            .sum()
            .reset_index()
        )

        #print first 3 dataframes in each column 
        dfSales_DataSet_Temp = dfSales_DataSet_Filtered.loc[ dfSales_DataSet_Filtered["Year"].isin([intStartYear, intEndYear]),
                                             ["Year", "ProductFamily", "InvoiceAmt"] ]    
        #convert year to string
        dfSales_DataSet_Temp = dfSales_DataSet_Temp.astype({"Year": str})
        
        #print first 3 dataframes in each column 
        dfSales_DataSet_Temp = dfSales_DataSet_Filtered.loc[ dfSales_DataSet_Filtered["Year"].isin([intStartYear, intEndYear]),
                                            ["Year", "ProductFamily", "InvoiceAmt"] ]    
        #convert year to string
        dfSales_DataSet_Temp = dfSales_DataSet_Temp.astype({"Year": str})

               
        fig = px.scatter(
           dfSales_DataSet_Temp,
           x="ProductFamily",
           y="InvoiceAmt",
           color="Year",
           height=800,
           width=1000,
           title=f"Comparing Sales By Product Family For {intEndYear} Against {intStartYear}"
        )

        plt.style.use("dark_background")
        #from chatGPT
        fig.update_xaxes(type="category", categoryorder="category ascending")
        #end from chatGPT
        fig.update_layout(
           xaxis_title="Product Family", 
           yaxis_title="Invoice Amount", 
          # template="plotly_dark",          
           title_x=0.3,
           title_font=dict(size=20, family="Arial", color="white"),
           xaxis_color="white",
           yaxis_color="white", 
           plot_bgcolor="#070707", 
           paper_bgcolor ="#070707"
        )

        fig.update_yaxes(minor=dict(
             ticks="outside",
             ticklen=6,
             dtick=2000
             ))

        #make so dots on plot are more readable
        fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))

        conContainerTab7_Sub.plotly_chart(fig, use_container_width=True, key="figTab7") 
        expExpander7 = conContainerTab7_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander7")
        expExpander7.dataframe(dfSales_DataSet_Temp , use_container_width=True)         
        conSectionFooter7 = conContainerTab7_Sub.container(border=False, width="stretch", key="conSectionFooter7", height=400)
        conSectionFooter7.write("We can see consistently Electronic Components, Fire Products, Odet, Pescara and Arc are high sellers ")
        conSectionFooter7.write("The overall trend is quite stable which is a good business sign, with some areas such as " +
                                "Arrian, M-Range and Odet showing increased growth.")
        
        

   case "ML Hypothesis 8":     

        #add slider so user can play with the report
      #   sdlSliderFrom = conContainerTab8_Sub.slider("Select Amount of Stores", min_value=10, 
      #                                               max_value=dfSales_DataSet_Work["Store"].nunique(), value=10, step=1, 
      #                                               key="sdlSliderFrom1")

      #   #group by Store and get sum of Weekly_Sales
      #   dfSales_DataSet_Work = (
      #      dfSales_DataSet_Work
      #      .groupby("Store")["Weekly_Sales"]
      #      .sum()
      #      .sort_values(ascending=False)
      #      .head(sdlSliderFrom)
      #      .reset_index()
      #   )


#******tab 8*******  
        #plotly visualisation for hypothesis 8 - What are the predicted sales per month for next year?
        #Note: last year in data is: 2012
        conSection4 = conContainerMain.container(border=False, width="stretch", key="conSection4", height=860)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab8, tabTab9, tabTab10, tabTab11  = conSection4.tabs([
          "Hypothesis 8 - Linear Regression", "Hypothesis 8 - Random Forest", "2018 Prediction - Linear Regression",
          "2018 Prediction - Random Forest"
        ])  

        conSection4Tab = tabTab8.container(border=True, width="stretch", height=780)
        conSection4Title = conSection4Tab.container(border=False, width="stretch", key="conSection4Title", height=40)      
        conSection4Title.info("What Are The Predicted Sales Per Month For Next Year?")
  
        objPipeline = joblib.load(CNST_STR_LINEAR_PIPELINE_HYPOTHESIS8_TEST_PATH)
 
        #get above DataFrame and filter for JUST 2017
        dfSalesDataML_Temp = dfSales_InvoiceData_GroupByTerritory[dfSales_InvoiceData_GroupByTerritory["Year"] == 2017].copy()

        #use special csv file grouped by territory and yearmonth
        dfSalesDataML_Work = dfSales_InvoiceData_GroupByTerritory.copy() 
        
        #sort by yearmonth
        dfSalesDataML_Temp.sort_values(by=["YearMonth"], inplace=True)

        dfSalesDataML_Work["Month"] = (
             dfSalesDataML_Work["YearMonth"] % 100
        )

        #filter for year 2017 only
        dfSalesDataML_Temp = dfSalesDataML_Work[ dfSalesDataML_Work["Year"] == 2017].copy()
 
        lstFeatures = [
            "TerritoryCodes",
            "Year",
            "Month"
        ]
 
        dfSalesDataML_Temp["Predicted_InvoiceAmt"] = objPipeline.predict(dfSalesDataML_Temp[lstFeatures]) 
 
 
        dfPlot = (
           dfSalesDataML_Temp
            .groupby("YearMonth")[
               ["InvoiceAmt", "Predicted_InvoiceAmt"]
            ]
           .sum()
           .reset_index()
        )


        fig, ax = plt.subplots(figsize=(14, 7))

        #configure plot
        ax.plot(
            dfPlot["YearMonth"].astype(str),
            dfPlot["InvoiceAmt"],
            marker="o",
            linewidth=2,
            label="Actual"
        )

        ax.plot(
            dfPlot["YearMonth"].astype(str),
            dfPlot["Predicted_InvoiceAmt"],
            marker="o",
            linestyle="--",
            linewidth=2,
            label="Predicted"
        )

        ax.set_title("2017 Actual vs Predicted Invoice Amount -  Linear Regression")
        ax.set_xlabel("Month")
        ax.set_ylabel("Invoice Amount")
        #make x-axis labels more readable
        ax.set_xticklabels(dfPlot["YearMonth"].astype(str), rotation=45)
        #show legend and grid
        ax.legend()
        ax.grid(True, alpha=0.3)
                                 
        conSection4Tab.pyplot(fig, use_container_width=True) 
        expExpander8 = conSection4Tab.expander("Show Data Used For Plot", expanded=False, key="expExpander8")
        expExpander8.dataframe(dfPlot, use_container_width=True)      

        conSectionFooter8 = conSection4Tab.container(border=False, width="stretch", key="conSectionFooter8", height=400) 
        conSectionFooter8.write("As we can see the predicted values start off reasonably close but veer off dramatically quite" +
                                "quickly and ends in a surprising downward motion.")  
        conSectionFooter8.write("I would not recommend using this model, it is here for contrast only!")  
        
#****tab 9*****
        #plotly visualisation for hypothesis8 - What are the predicted sales per month for next year?
        #Note: last year in data is: 2012
        conContainerTab9_Sub = tabTab9.container(border=True, width="stretch", key="conTab9Sub", height=780)
        conContainerTab9_Sub.info("What Are The Predicted Sales Per Month For Next Year?")

        objPipeline = joblib.load(CNST_STR_FOREST_PIPELINE_HYPOTHESIS8_TEST_PATH)
 
        #get above DataFrame and filter for JUST 2017
        dfSalesDataML_Temp = dfSales_InvoiceData_GroupByTerritory[dfSales_InvoiceData_GroupByTerritory["Year"] == 2017].copy()

        #use special csv file grouped by territory and yearmonth
        dfSalesDataML_Work = dfSales_InvoiceData_GroupByTerritory.copy() 
        
        #sort by yearmonth
        dfSalesDataML_Temp.sort_values(by=["YearMonth"], inplace=True)

        dfSalesDataML_Work["Month"] = (
             dfSalesDataML_Work["YearMonth"] % 100
        )

        #filter for year 2017 only
        dfSalesDataML_Temp = dfSalesDataML_Work[ dfSalesDataML_Work["Year"] == 2017].copy()
 
        lstFeatures = [
            "TerritoryCodes",
            "Year",
            "Month"
        ]
 
        dfSalesDataML_Temp["Predicted_InvoiceAmt"] = objPipeline.predict(dfSalesDataML_Temp[lstFeatures]) 
 
 
        dfPlot = (
           dfSalesDataML_Temp
            .groupby("YearMonth")[
               ["InvoiceAmt", "Predicted_InvoiceAmt"]
            ]
           .sum()
           .reset_index()
        )


        fig, ax = plt.subplots(figsize=(14, 7))

        #configure plot
        ax.plot(
            dfPlot["YearMonth"].astype(str),
            dfPlot["InvoiceAmt"],
            marker="o",
            linewidth=2,
            label="Actual"
        )

        ax.plot(
            dfPlot["YearMonth"].astype(str),
            dfPlot["Predicted_InvoiceAmt"],
            marker="o",
            linestyle="--",
            linewidth=2,
            label="Predicted"
        )

        ax.set_title("2017 Actual vs Predicted Invoice Amount -  Random Forest")
        ax.set_xlabel("Month")
        ax.set_ylabel("Invoice Amount")
        #make x-axis labels more readable
        ax.set_xticklabels(dfPlot["YearMonth"].astype(str), rotation=45)
        #show legend and grid
        ax.legend()
        ax.grid(True, alpha=0.3)
                                 
        conContainerTab9_Sub.pyplot(fig, use_container_width=True) 
        expExpander9 = conContainerTab9_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander9")
        expExpander9.dataframe(dfPlot, use_container_width=True)      
        conSectionFooter9 = conContainerTab9_Sub.container(border=False, width="stretch", key="conSectionFooter9", height=400) 
        conSectionFooter9.write("This modles results are a lot more stable than the previous shows a more refined curve that matches " + 
                                "the actual values more closely.")  
        conSectionFooter9.write("This is the model I recommend using for prediction of next years sales.")  

#****tab 10*****
        #2018 prediction - linear regression
        #Note: last year in data is: 2012
        conContainerTab10_Sub = tabTab10.container(border=True, width="stretch", key="conTab10Sub", height=780)
        conContainerTab10_Sub.info("What Are The Predicted Sales Per Month For Next Year?")

        objPipeline = joblib.load(CNST_STR_LINEAR_PIPELINE_HYPOTHESIS8_PREDICTION_PATH)
   
        #use special csv file grouped by territory and yearmonth
        dfSalesDataML_Work = dfSales_InvoiceData_GroupByTerritory.copy() 
          
        #create special Month column (which incidentally overwrites the existing one!)
        dfSalesDataML_Work["Month"] = (dfSalesDataML_Work["YearMonth"] % 100).astype(int)

        #cyclic features - no idea what htis does but ML with dates seems to cause problems!
        dfSalesDataML_Work["MonthSin"] = np.sin(2 * np.pi * dfSalesDataML_Work["Month"] / 12)
        dfSalesDataML_Work["MonthCos"] = np.cos(2 * np.pi * dfSalesDataML_Work["Month"] / 12)

 
        #configure features
        lstFeatures = [
            "TerritoryCodes",
            "Year",
            "MonthSin",
            "MonthCos"
        ]

 
        # Get all territories that existed in 2017
        lstTerritories = sorted(
            dfSalesDataML_Work[
               dfSalesDataML_Work["Year"] == 2017
            ]["TerritoryCodes"]
            .dropna()
            .unique()
        )

        # Create 12 months for every territory
        df2018Predict = pd.DataFrame(
           [
              {
                     "TerritoryCodes": territory,
                     "Year": 2018,
                     "Month": month,
                     "YearMonth": 201800 + month
              }
              for territory in lstTerritories
              for month in range(1, 13)
           ]
        )


        #add cyclic features
        df2018Predict["MonthSin"] = np.sin(
            2 * np.pi * df2018Predict["Month"] / 12
        )

        df2018Predict["MonthCos"] = np.cos(
            2 * np.pi * df2018Predict["Month"] / 12
        )

        #predict 2018
        dfX2018 = df2018Predict[
            lstFeatures
        ]

        obj2018Predictions = (
            objPipeline.predict(
               dfX2018
            )
        )

        # Add predictions
        df2018Predict[
            "Predicted_InvoiceAmt"
        ] = obj2018Predictions

        df2018Monthly = (
            df2018Predict
            .groupby("YearMonth")[
               "Predicted_InvoiceAmt"
            ]
            .sum()
            .reset_index()
        )

        fig, ax = plt.subplots(figsize=(14, 7))

        #configure plot
        ax.plot(
            df2018Monthly["YearMonth"].astype(str),
            df2018Monthly["Predicted_InvoiceAmt"],
            marker="o",
            linestyle="--",
            linewidth=2,
            label="Predicted"
        )

        plt.title("2018 Predicted Invoice Amount - Linear Regression")
        ax.set_xlabel("Month")
        ax.set_ylabel("Predicted Invoice Amount (£)")
        #make x-axis labels more readable
        ax.set_xticklabels(df2018Monthly["YearMonth"].astype(str), rotation=45)
        #show legend and grid
        ax.legend()
        ax.grid(True, alpha=0.3)

                                         
        conContainerTab10_Sub.pyplot(fig, use_container_width=True) 

        conSectionFooter10 = conContainerTab10_Sub.container(border=False, width="stretch", key="conSectionFooter10", height=400) 
        conSectionFooter10.write("This model produces a plot more like a hill than the previous plots using actual data.")  
        conSectionFooter10.write("Am not seeing a trend related to historic values, this model does not work!")  
        conSectionFooter10.write("Included for comparison only.")  


#****tab 11*****
        #2018 prediction - random forest
        conContainerTab11_Sub = tabTab11.container(border=True, width="stretch", key="conTab11Sub", height=780)
        conContainerTab11_Sub.info("What Are The Predicted Sales Per Month For Next Year?")

        objPipeline = joblib.load(CNST_STR_FOREST_PIPELINE_HYPOTHESIS8_PREDICTION_PATH)
   
        #use special csv file grouped by territory and yearmonth
        dfSalesDataML_Work = dfSales_InvoiceData_GroupByTerritory.copy() 
          
        #create special Month column (which incidentally overwrites the existing one!)
        dfSalesDataML_Work["Month"] = (dfSalesDataML_Work["YearMonth"] % 100).astype(int)

        #cyclic features - no idea what htis does but ML with dates seems to cause problems!
        dfSalesDataML_Work["MonthSin"] = np.sin(2 * np.pi * dfSalesDataML_Work["Month"] / 12)
        dfSalesDataML_Work["MonthCos"] = np.cos(2 * np.pi * dfSalesDataML_Work["Month"] / 12)

 
        #configure features
        lstFeatures = [
            "TerritoryCodes",
            "Year",
            "MonthSin",
            "MonthCos"
        ]

 
        # Get all territories that existed in 2017
        lstTerritories = sorted(
            dfSalesDataML_Work[
               dfSalesDataML_Work["Year"] == 2017
            ]["TerritoryCodes"]
            .dropna()
            .unique()
        )

        # Create 12 months for every territory
        df2018Predict = pd.DataFrame(
           [
              {
                     "TerritoryCodes": territory,
                     "Year": 2018,
                     "Month": month,
                     "YearMonth": 201800 + month
              }
              for territory in lstTerritories
              for month in range(1, 13)
           ]
        )


        #add cyclic features
        df2018Predict["MonthSin"] = np.sin(
            2 * np.pi * df2018Predict["Month"] / 12
        )

        df2018Predict["MonthCos"] = np.cos(
            2 * np.pi * df2018Predict["Month"] / 12
        )

        #predict 2018
        dfX2018 = df2018Predict[
            lstFeatures
        ]

        obj2018Predictions = (
            objPipeline.predict(
               dfX2018
            )
        )

        # Add predictions
        df2018Predict[
            "Predicted_InvoiceAmt"
        ] = obj2018Predictions

        df2018Monthly = (
            df2018Predict
            .groupby("YearMonth")[
               "Predicted_InvoiceAmt"
            ]
            .sum()
            .reset_index()
        )

        fig, ax = plt.subplots(figsize=(14, 7))

        #configure plot
        ax.plot(
            df2018Monthly["YearMonth"].astype(str),
            df2018Monthly["Predicted_InvoiceAmt"],
            marker="o",
            linestyle="--",
            linewidth=2,
            label="Predicted"
        )

        plt.title("2018 Predicted Invoice Amount - Random Forest")
        ax.set_xlabel("Month")
        ax.set_ylabel("Predicted Invoice Amount (£)")
        #make x-axis labels more readable
        ax.set_xticklabels(df2018Monthly["YearMonth"].astype(str), rotation=45)
        #show legend and grid
        ax.legend()
        ax.grid(True, alpha=0.3)

                                         
        conContainerTab11_Sub.pyplot(fig, use_container_width=True) 

        conSectionFooter11 = conContainerTab11_Sub.container(border=False, width="stretch", key="conSectionFooter11", height=400) 
        conSectionFooter11.write("Much closer to historic data, has similar peaks and troughs and looks feasible as a prediction for 2018 sales.")  
        conSectionFooter11.write("I would suggest using this model.")  


#***hypothesis 9 ML****

   case "ML Hypothesis 9":     


#******tab 12*******  

        #visualisation for hypothesis 9 - What are the predicted sales per territory for next year?
        #Note: last year in data is: 2012
        conSection5 = conContainerMain.container(border=False, width="stretch", key="conSection5", height=860)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab12, tabTab13, tabTab14, tabTab15  = conSection5.tabs([
          "Hypothesis 9 - Linear Regression", "Hypothesis 9 - Random Forest", "2018 Prediction - Linear Regression",
          "2018 Prediction - Random Forest"
        ])  

        conSection5Tab = tabTab12.container(border=True, width="stretch", height=780)
        conSection5Title = conSection5Tab.container(border=False, width="stretch", key="conSection5Title", height=40)      
        conSection5Title.info("What Are The Predicted Sales Per Territory For Next Year?")
  
        objPipeline = joblib.load(CNST_STR_LINEAR_PIPELINE_HYPOTHESIS9_TEST_PATH)
 
        #get above DataFrame and filter for JUST 2017
        dfSalesDataML_Temp = dfSales_InvoiceData_GroupByTerritory[dfSales_InvoiceData_GroupByTerritory["Year"] == 2017].copy()

        #use special csv file grouped by territory and yearmonth
        dfSalesDataML_Work = dfSales_InvoiceData_GroupByTerritory.copy()          
 
        #sort by yearmonth
        dfSalesDataML_Temp.sort_values(by=["YearMonth"], inplace=True)

        dfSalesDataML_Work["Month"] = (
            dfSalesDataML_Work["YearMonth"] % 100
        )

        #filter for year 2017 only
        dfSalesDataML_Temp = dfSalesDataML_Work[ dfSalesDataML_Work["Year"] == 2017].copy()
 
        lstFeatures = [
            "TerritoryCodes",
            "Year",
            "Month"
        ]
 
        dfSalesDataML_Temp["Predicted_InvoiceAmt"] = objPipeline.predict(dfSalesDataML_Temp[lstFeatures]) 
 
        #for statistical comparison 
        dfPlot = (
            dfSalesDataML_Temp
            .groupby(["YearMonth","TerritoryCodes"])[
               ["InvoiceAmt", "Predicted_InvoiceAmt"]
            ]
            .sum()
            .reset_index()
        )

        dfPlot["Difference"] = (
            dfPlot["InvoiceAmt"]
            - dfPlot["Predicted_InvoiceAmt"]
        )

        dfPlot["DifferencePercent"] = (
            dfPlot["Difference"]
            / dfPlot["InvoiceAmt"]
        ) * 100



        fig, ax = plt.subplots(figsize=(14, 7))
        #configure plot
        ax.bar(
            dfPlot["TerritoryCodes"], 
            dfPlot["InvoiceAmt"],
            label="Actual"
        )

        ax.bar(
            dfPlot["TerritoryCodes"],      
            dfPlot["Predicted_InvoiceAmt"],
            label="Predicted"
        )

        ax.set_title("2017 Actual vs Predicted Territory Sales - Linear Regression")
        ax.set_xlabel("Territory")
        ax.set_ylabel("Invoice Amount")
        #make x-axis labels more readable
        ax.set_xticklabels(dfPlot["TerritoryCodes"].astype(str), rotation=90)
        #show legend and grid
        ax.legend()
        ax.grid(True, alpha=0.3)

                                 
        conSection5Tab.pyplot(fig, use_container_width=True) 
        expExpander12 = conSection5Tab.expander("Show Data Used For Plot", expanded=False, key="expExpander12")
        expExpander12.dataframe(dfPlot, use_container_width=True)      

        conSectionFooter12 = conSection5Tab.container(border=False, width="stretch", key="conSectionFooter12", height=400) 
        conSectionFooter12.write("looks ok until we see it sis predicting NEGATIVE values against actial positive ones")  
        conSectionFooter12.write("I would not recommend using this model, it is here for contrast only!")  
        
#****tab 13*****
        #visualisation for hypothesis 9 - What are the predicted sales per territory for next year?
        #Note: last year in data is: 2012
        conContainerTab13_Sub = tabTab13.container(border=True, width="stretch", key="conTab13Sub", height=780)
        conContainerTab13_Sub.info("What Are The Predicted Sales Per Month For Next Year?")

        objPipeline = joblib.load(CNST_STR_FOREST_PIPELINE_HYPOTHESIS9_TEST_PATH)
 
        #get above DataFrame and filter for JUST 2017
        dfSalesDataML_Temp = dfSales_InvoiceData_GroupByTerritory[dfSales_InvoiceData_GroupByTerritory["Year"] == 2017].copy()
 
        #use special csv file grouped by territory and yearmonth
        dfSalesDataML_Work = dfSales_InvoiceData_GroupByTerritory.copy()          
  
        #sort by yearmonth
        dfSalesDataML_Temp.sort_values(by=["YearMonth"], inplace=True)
 
        dfSalesDataML_Work["Month"] = (
             dfSalesDataML_Work["YearMonth"] % 100
        )
 
        #filter for year 2017 only
        dfSalesDataML_Temp = dfSalesDataML_Work[ dfSalesDataML_Work["Year"] == 2017].copy()
  
        lstFeatures = [
             "TerritoryCodes",
             "Year",
             "Month"
        ]
 
        dfSalesDataML_Temp["Predicted_InvoiceAmt"] = objPipeline.predict(dfSalesDataML_Temp[lstFeatures]) 
  
        #for statistical comparison 
        dfPlot = (
          dfSalesDataML_Temp
            .groupby(["YearMonth","TerritoryCodes"])[
               ["InvoiceAmt", "Predicted_InvoiceAmt"]
            ]
            .sum()
            .reset_index()
        )

 
        dfPlot["Difference"] = (
             dfPlot["InvoiceAmt"]
             - dfPlot["Predicted_InvoiceAmt"]
        )
 
        dfPlot["DifferencePercent"] = (
             dfPlot["Difference"]
             / dfPlot["InvoiceAmt"]
        ) * 100
  
 
        fig, ax = plt.subplots(figsize=(14, 7))
         #configure plot
        ax.bar(
             dfPlot["TerritoryCodes"], 
             dfPlot["InvoiceAmt"],
             label="Actual"
        )
 
        ax.bar(
             dfPlot["TerritoryCodes"],      
             dfPlot["Predicted_InvoiceAmt"],
             label="Predicted"
        )
 
        ax.set_title("2017 Actual vs Predicted Territory Sales - Linear Regression")
        ax.set_xlabel("Territory")
        ax.set_ylabel("Invoice Amount")
        #make x-axis labels more readable
        ax.set_xticklabels(dfPlot["TerritoryCodes"].astype(str), rotation=90)
        #show legend and grid
        ax.legend()
        ax.grid(True, alpha=0.3)
                                
        conContainerTab13_Sub.pyplot(fig, use_container_width=True) 
        expExpander13 = conContainerTab13_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander13")
        expExpander13.dataframe(dfPlot, use_container_width=True)      
        conSectionFooter13 = conContainerTab13_Sub.container(border=False, width="stretch", key="conSectionFooter13", height=400) 
        conSectionFooter13.write("This model results are a lot more stable than the previous no negative values and a close match to acutal values.")  
        conSectionFooter13.write("This is the model I recommend using for prediction of next years sales.")  

#****tab 14*****
        #2018 prediction - linear regression

        conContainerTab14_Sub = tabTab14.container(border=True, width="stretch", key="conTab14Sub", height=780)
        conContainerTab14_Sub.info("What Are The Predicted Sales Per Month For Next Year?")

        objPipeline = joblib.load(CNST_STR_LINEAR_PIPELINE_HYPOTHESIS9_PREDICTION_PATH)
   
        #use special csv file grouped by territory and yearmonth
        dfSalesDataML_Work = dfSales_InvoiceData_GroupByTerritory.copy() 
          
        #create special Month column (which incidentally overwrites the existing one!)
        dfSalesDataML_Work["Month"] = (dfSalesDataML_Work["YearMonth"] % 100).astype(int)

        #cyclic features - no idea what htis does but ML with dates seems to cause problems!
        dfSalesDataML_Work["MonthSin"] = np.sin(2 * np.pi * dfSalesDataML_Work["Month"] / 12)
        dfSalesDataML_Work["MonthCos"] = np.cos(2 * np.pi * dfSalesDataML_Work["Month"] / 12)

 
        #configure features
        lstFeatures = [
         "TerritoryCodes",
         "Year",
         "MonthSin",
         "MonthCos"
        ]

 
        # Get all territories that existed in 2017
        lstTerritories = sorted(
            dfSalesDataML_Work[
               dfSalesDataML_Work["Year"] == 2017
            ]["TerritoryCodes"]
            .dropna()
            .unique()
        )

        # Create 12 months for every territory
        df2018Predict = pd.DataFrame(
           [
              {
                     "TerritoryCodes": territory,
                     "Year": 2018,
                     "Month": month,
                     "YearMonth": 201800 + month
              }
              for territory in lstTerritories
              for month in range(1, 13)
           ]
        )


        #add cyclic features
        df2018Predict["MonthSin"] = np.sin(
            2 * np.pi * df2018Predict["Month"] / 12
        )

        df2018Predict["MonthCos"] = np.cos(
            2 * np.pi * df2018Predict["Month"] / 12
        )

        #predict 2018
        dfX2018 = df2018Predict[
            lstFeatures
        ]

        obj2018Predictions = (
            objPipeline.predict(
               dfX2018
            )
        )

        # Add predictions
        df2018Predict[
            "Predicted_InvoiceAmt"
        ] = obj2018Predictions

        df2018Territory = (
          df2018Predict
          .groupby("TerritoryCodes")[
            "Predicted_InvoiceAmt"
          ]
          .sum()
          .reset_index()
       )

        fig, ax = plt.subplots(figsize=(14, 7))

        #configure plot
        ax.bar(
            df2018Territory["TerritoryCodes"].astype(str),
            df2018Territory["Predicted_InvoiceAmt"],
            label="Predicted"
        )

        plt.title("2018 Predicted Invoice Amount - Linear Regression")
        ax.set_xlabel("TerritoryCodes")
        ax.set_ylabel("Predicted Invoice Amount (£)")
        #make x-axis labels more readable
        ax.set_xticklabels(df2018Territory["TerritoryCodes"].astype(str), rotation=90)
        #show legend and grid
        ax.legend()
        ax.grid(True, alpha=0.3)

                                         
        conContainerTab14_Sub.pyplot(fig, use_container_width=True) 

        conSectionFooter14 = conContainerTab14_Sub.container(border=False, width="stretch", key="conSectionFooter14", height=400) 
        conSectionFooter14.write("This model produces NEGATIVE values for a prediction where the actual data is largely free of negative values" +
                                 "this is not a good sign, and therefore not a goot moddel, but put here for comparison.") 


#****tab 15*****
        #2018 prediction - random forest
        #Note: last year in data is: 2012
        conContainerTab15_Sub = tabTab15.container(border=True, width="stretch", key="conTab15Sub", height=780)
        conContainerTab15_Sub.info("What Are The Predicted Sales Per Month For Next Year?")


        objPipeline = joblib.load(CNST_STR_FOREST_PIPELINE_HYPOTHESIS9_PREDICTION_PATH)
   
        #use special csv file grouped by territory and yearmonth
        dfSalesDataML_Work = dfSales_InvoiceData_GroupByTerritory.copy() 
          
        #create special Month column (which incidentally overwrites the existing one!)
        dfSalesDataML_Work["Month"] = (dfSalesDataML_Work["YearMonth"] % 100).astype(int)

        #cyclic features - no idea what htis does but ML with dates seems to cause problems!
        dfSalesDataML_Work["MonthSin"] = np.sin(2 * np.pi * dfSalesDataML_Work["Month"] / 12)
        dfSalesDataML_Work["MonthCos"] = np.cos(2 * np.pi * dfSalesDataML_Work["Month"] / 12)

 
        #configure features
        lstFeatures = [
         "TerritoryCodes",
         "Year",
         "MonthSin",
         "MonthCos"
        ]

 
        # Get all territories that existed in 2017
        lstTerritories = sorted(
            dfSalesDataML_Work[
               dfSalesDataML_Work["Year"] == 2017
            ]["TerritoryCodes"]
            .dropna()
            .unique()
        )

        # Create 12 months for every territory
        df2018Predict = pd.DataFrame(
           [
              {
                     "TerritoryCodes": territory,
                     "Year": 2018,
                     "Month": month,
                     "YearMonth": 201800 + month
              }
              for territory in lstTerritories
              for month in range(1, 13)
           ]
        )


        #add cyclic features
        df2018Predict["MonthSin"] = np.sin(
            2 * np.pi * df2018Predict["Month"] / 12
        )

        df2018Predict["MonthCos"] = np.cos(
            2 * np.pi * df2018Predict["Month"] / 12
        )

        #predict 2018
        dfX2018 = df2018Predict[
            lstFeatures
        ]

        obj2018Predictions = (
            objPipeline.predict(
               dfX2018
            )
        )

        # Add predictions
        df2018Predict[
            "Predicted_InvoiceAmt"
        ] = obj2018Predictions

        df2018Territory = (
          df2018Predict
          .groupby("TerritoryCodes")[
            "Predicted_InvoiceAmt"
          ]
          .sum()
          .reset_index()
       )

        fig, ax = plt.subplots(figsize=(14, 7))

        #configure plot
        ax.bar(
            df2018Territory["TerritoryCodes"].astype(str),
            df2018Territory["Predicted_InvoiceAmt"],
            label="Predicted"
        )

        plt.title("2018 Predicted Invoice Amount - Linear Regression")
        ax.set_xlabel("TerritoryCodes")
        ax.set_ylabel("Predicted Invoice Amount (£)")
        #make x-axis labels more readable
        ax.set_xticklabels(df2018Territory["TerritoryCodes"].astype(str), rotation=90)
        #show legend and grid
        ax.legend()
        ax.grid(True, alpha=0.3)
                                         
        conContainerTab15_Sub.pyplot(fig, use_container_width=True) 

        conSectionFooter15 = conContainerTab15_Sub.container(border=False, width="stretch", key="conSectionFooter15", height=400) 
        conSectionFooter15.write("Much closer to historic data, no negative value and strong in a lot of areas the actual data is.")  
        conSectionFooter15.write("I would suggest using this model.")  


   case "Ethics & Data Privacy":
        conContainerEthicsMain = conContainerMain.container(border=False, width="stretch", key="conSectionEthics", height=860) 
        conSectionEthicsTitle = conContainerEthicsMain.container(border=False, width="stretch", key="conSectionEthicsTitle", height=40)
        conSectionEthicsTitle.info("Ethical Considerations & Data Governance")
        conContainerEthicsMain.write("")
        conContainerEthicsMain.write("")               
        conContainerEthicsMain.write("We are committed to ensuring the responsible use of data and protecting the privacy of our customers")
        conContainerEthicsMain.write("and ensuring ethical and responsible use.")
        conContainerEthicsMain.write("")
        conContainerEthicsMain.write("Generative AI was used for machine learning of which any potential personal data or sensitive data")
        conContainerEthicsMain.write("was anonymised beforehand to ensure customer privacy is maintained.")
        conContainerEthicsMain.write("")
        conContainerEthicsMain.write("No data on this dashboard contains any data that could be used to identify any individual or business.")
        conContainerEthicsMain.write("We are committed to monitoring and improving our data privacy practices to ensure that we are always in ")
        conContainerEthicsMain.write("compliance with relevant regulations and best practices.")
        conContainerEthicsMain.write(" ")     
        conContainerEthicsMain.write("No sensitive customer data is processed or stored on non local servers as per ISO270001")  
        conContainerEthicsMain.write("No machine learning is performed on non local servers")
        conContainerEthicsMain.write(" ")        
        conContainerEthicsMain.write("We handle data provided to us from UK and European customers in line with GDPR and EU regulations")
        

       