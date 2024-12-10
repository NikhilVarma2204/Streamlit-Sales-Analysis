import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def df_tabs_for_grouped_data(df1,df2):
    
   with st.container(border=True):
       tab1,tab2 = st.tabs(['Transaction Type', 'Gender'])
       with tab1:
            st.table(df1)
            
       with tab2:
            st.table(df2)
    
def total_sales_data(value):
    
    with st.container(border=True):
        st.metric('Total Sales in USD',value=value)

def coast_based_sales(df_city,df_state,df_coast):
    with st.container(border=True):
        tab1,tab2,tab3 = st.tabs(['City','State','Coast'])
        with tab1:
            st.table(df_city)
        with tab2:
            st.table(df_state)
        with tab3:
            st.table(df_coast)




if __name__ == '__main__':

    df = pd.read_csv('transactions_2024-12-10_12-50-21.csv')
    st.title(body='Peroidic Data Analysis of Sales Data')
    #grouping based on transaction type and sale_amount sum
    df_group_1 = df.groupby('transaction_type')['sale_amount'].sum().reset_index()

    #data grouping based on gender
    df_group_2 = df.groupby('gender')['sale_amount'].sum().reset_index()
   
    df_total_sales = df['sale_amount'].sum()

   #container - Total Sales
    total_sales_data(df_total_sales)

    
   #container - Group by
    st.subheader('Based on Gender and Trasaction Type: ')
    df_tabs_for_grouped_data(df1=df_group_1,df2=df_group_2)


   
    st.subheader('Based on Region: ')
    #groupinng based on city
    df_group_by_city_and_sales = df.groupby('city')['sale_amount'].sum().reset_index()
    #grouping based on state
    df_group_by_state_and_sales = df.groupby('state')['sale_amount'].sum().reset_index()
    #grouping based on coast
    df_group_by_coast_and_sales = df.groupby('coast')['sale_amount'].sum().reset_index()

    coast_based_sales(
        df_city=df_group_by_city_and_sales,
        df_state=df_group_by_state_and_sales,
        df_coast=df_group_by_coast_and_sales
        )


