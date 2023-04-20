import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from datetime import datetime   
from sqlalchemy import create_engine


import streamlit.components.v1 as components
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="⚡", page_title='DUKAPAQ')
# set_page_config => https://github.com/streamlit/streamlit/issues/1770

key_menu = ['DUKAPAQ MERCHANTS ANALYTICS', 'DUKAPAQ MEMBERS ANALYTICS']
main_selection = st.sidebar.selectbox("Select The analytics you want to check ", key_menu)


if main_selection == 'DUKAPAQ MERCHANTS ANALYTICS':
    st.header("Dukapaq Merchant App Metrics")
    # Load the available data and overview
    #duka_data = "survey_final_data.json"
    st.sidebar.header('Merchant Analytics')
    # Check for uploaded dataset.
    #df_duka = pd.read_json(member_data, encoding="ISO-8859-1")

elif main_selection == 'DUKAPAQ MEMBERS ANALYTICS':
    st.header("Dukapaq Members App Metrics")
    # Load the available data and overview 
    data = "survey_final_data.json"
    st.sidebar.header('Survey Analytics')
    # Check for uploaded dataset.
    df = pd.read_json(data, encoding="ISO-8859-1")

    # Add select boxes for different commands and functionalities.
    menu = df['question_text'].unique()
    selection = st.sidebar.selectbox("Select survey question", menu)

    st.subheader('Display data')
    st.dataframe(df.head())

    col1, col2=st.columns(2)
    with col1:
        question_data = df[df['question_text'] == selection]
        choice_counts = question_data['selected_choices'].value_counts()
        choice_df = pd.DataFrame({'selected_choice': choice_counts.index, 'count': choice_counts.values})
        st.write(f'{selection} : ')
        st.dataframe(choice_df, width=500)
        
    with col2:
            plt.figure(figsize=(8,5))
            sns.set_style('whitegrid')
            choice_df['selected_choice'] = choice_df['selected_choice'].apply(tuple)
            sns.barplot(data=choice_df, x='selected_choice', y="count",)
            sns.set_palette(['#1DA7DF', '#7AC9E9', '#99DFDE', '#9FB5BE', '#64B3D0', '#C7C9CB'])            
            plt.xlabel('selected_choice', fontsize=14)
            plt.ylabel("Counts", size=14)
            #plt.title("Number of facilities per location", size=14)
            ax = plt.gca()
            for p in ax.patches:
                ax.annotate(f'{p.get_height()}',
                            (p.get_x() + p.get_width() / 2, p.get_height() + 0.5),
                            ha='center', va='bottom', fontsize=12)
            # display the plot
            #plt.tight_layout()
            st.pyplot(plt)
