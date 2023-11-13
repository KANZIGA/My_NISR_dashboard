import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objects as go
@st.cache
def load_data(file_path, sheet_name):
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    return data

# Load the data 
data = load_data('C:/Users/Seth H/Desktop/research/RLFS Tables_ Annual_2022.xlsx', 'new')
def main():
    st.title("Labour force survey 2022")

if __name__ == "__main__":
    main()
#  charts based on the selected category and subcategory
def update_charts(selected_category, selected_subcategory):
    if selected_category == "Total Population":
        population = data.iloc[3, 1] 
        st.title("Population 16 years old and over ")
        st.markdown(f'<p style="color:white; font-size:96px;">{population}</p>', unsafe_allow_html=True)
        st.subheader("Labour force and gender in Unemployed population 16+")

        # First pie chart
        col5, col6 = st.columns(2)
        employed = data.iloc[5, 1]
        unemployed = data.iloc[8, 1]
        labels_emp = ["Labour force", "Outside Labour force"]
        values_pyt = [employed, unemployed]

        # Set custom colors
        colors_emp = ["#C5D9DC", "blue"]

        fig_pyt_pie1 = go.Figure(data=[go.Pie(labels=labels_emp, values=values_pyt, marker=dict(colors=colors_emp))])
        fig_pyt_pie1.update_layout(title="Labour force vs Outside Labour force", height=400, width=400)

        col5.plotly_chart(fig_pyt_pie1)

        # Second pie chart
        employed = data.iloc[3, 2]
        unemployed = data.iloc[3, 3]
        labels_emp = ["Men", "Women"]
        values_pyt = [employed, unemployed]

         # Set custom colors
        colors_emp = ["#C5D9DC", "pink"]

        fig_pyt_pie2 = go.Figure(data=[go.Pie(labels=labels_emp, values=values_pyt, marker=dict(colors=colors_emp))])
        fig_pyt_pie2.update_layout(title=" Employed vs Unemployed", height=400, width=400)

        col6.plotly_chart(fig_pyt_pie2)
       

          
        st.subheader("Employed and Unemployed in Labour force")

       
        col5, col6 = st.columns(2)
        employed = data.iloc[5, 1]
        unemployed = data.iloc[8, 1]
        labels_emp = ["Labour force", "Outside Labour force"]
        values_pyt = [employed, unemployed]

           
        colors_emp = ["blue", "pink"]

        fig_pyt_pie1 = go.Figure(data=[go.Pie(labels=labels_emp, values=values_pyt, marker=dict(colors=colors_emp))])
        fig_pyt_pie1.update_layout(title="Labour force vs Outside Labour force", height=400, width=400)

        col5.plotly_chart(fig_pyt_pie1)

        
        employed = data.iloc[6, 1]
        unemployed = data.iloc[7, 1]
        labels_emp = ["Employed", "Unemployed"]
        values_pyt = [employed, unemployed]

        
        colors_emp = ["#C5D9DC", "blue"]

        fig_pyt_pie2 = go.Figure(data=[go.Pie(labels=labels_emp, values=values_pyt, marker=dict(colors=colors_emp))])
        fig_pyt_pie2.update_layout(title="Employed VS Unemployed in Labour force", height=400, width=400)

        col6.plotly_chart(fig_pyt_pie2)

        st.subheader("Agriculture Parcipant and Rural vs urban")
        col70, col80 = st.columns(2)
        Participated= data.iloc[3, 6]
        Notparticipated = data.iloc[3, 7]
        labels_e = ["Participatedinsubsistenceagriculture", "Notparticipatedinsubsistenceagriculture"]
        values_pyt = [Participated,Notparticipated]
        fig_pyt_pie = go.Figure(data=[go.Pie(labels=labels_e, values=values_pyt)])
        fig_pyt_pie.update_layout(title="Participated in  subsistence agriculture vs Not participated in subsistence agriculture")
        col70.plotly_chart(fig_pyt_pie)

        
        st.subheader("Technical skills learned")
        employed = data.iloc[3, 4]
        unemployed = data.iloc[3, 5]
        labels_emp = ["Urban", "Rural"]
        values_pyt = [employed, unemployed]
        fig_pyt_pie = go.Figure(data=[go.Pie(labels=labels_emp, values=values_pyt)])
        fig_pyt_pie.update_layout(title="Urban vs Rural")
        col80.plotly_chart(fig_pyt_pie)

    elif selected_category == "IN GENERAL":
            if selected_subcategory == "in general":
            
             x_values = data.iloc[130:145, 0]
             y_values = data.iloc[130:145, 1]

             # Set custom 
             colors_bars = ["#FF5733", "#FF8247", "#FFA07A", "#FFD700", "#FFEC8B", "#FFFF00",
                   "#ADFF2F", "#7FFF00", "#32CD32", "#228B22", "#008000", "#006400",
                   "#8B4513", "#A52A2A"]

             fig_bars = go.Figure(go.Bar(
              x=x_values,
              y=y_values,
              marker=dict(color=colors_bars),  
              ))

           
             fig_bars.update_layout(height=600, width=800,title="Employed population 16+")
             st.plotly_chart(fig_bars)

            # Set up 
            bar_data1 = data.iloc[30:35, 1]
            bar_labels1 = data.iloc[30:35, 0]
            fig_bar_chart1 = go.Figure(go.Bar(
                x=bar_labels1,
                y=bar_data1,
                name='Set1',
                text=bar_data1,
                textposition='auto',
                marker_color='indianred'
            ))
            fig_bar_chart1.update_layout(title="Education level")

            # Set up the bar
            bar_data2 = data.iloc[11:14, 1]
            bar_labels2 = data.iloc[11:14, 0]
            fig_bar_chart2 = go.Figure(go.Bar(
                x=bar_labels2,
                y=bar_data2,
                name='Set2',
                text=bar_data2,
                textposition='auto',
                marker_color='blue'
            ))
            fig_bar_chart2.update_layout(title="Labour underutilization")

            # Set up the bar chart for rows 41-50 data
            bar_data3 = data.iloc[41:51, 1]
            bar_labels3 = data.iloc[41:51, 0]
            fig_bar_chart3 = go.Figure(go.Bar(
                x=bar_labels3,
                y=bar_data3,
                name='Set3',
                text=bar_data3,
                textposition='auto',
                marker_color='green'
            ))
            fig_bar_chart3.update_layout(title="Program Classification")

            # Set up
            waterfall_data = data.iloc[56:61, 1]
            waterfall_labels = data.iloc[56:61, 0]
            fig_waterfall = go.Figure(go.Waterfall(
                orientation="v",
                measure=["absolute"] * len(waterfall_data),
                x=waterfall_labels,
                y=waterfall_data,
            ))
            fig_waterfall.update_layout(title="Timeframe Options")

            # Set up additional 
            bar_data4 = data.iloc[170:192, 1]
            bar_labels4 = data.iloc[170:192, 0]
 
             
            sorted_indices = bar_data4.argsort()[::-1]
            bar_data4_sorted = bar_data4.iloc[sorted_indices]
            bar_labels4_sorted = bar_labels4.iloc[sorted_indices]

            
            bar_chart_size = 800
            bar_chart_color = 'blue'

            fig_horizontal_bar = go.Figure(go.Bar(
            y=bar_labels4_sorted,
            x=bar_data4_sorted,
            text=bar_data4_sorted,
            textposition='auto',
            orientation='h',  
            marker_color=bar_chart_color,  
          ))
            fig_horizontal_bar.update_layout(title="Employment Sectors Overview", height=bar_chart_size)

             
            st.subheader("Employment Sectors Overview")
            st.plotly_chart(fig_horizontal_bar, use_container_width=True)
            # Set up grouped bar chart for rows 222-236 data
            bar_data_set1 = data.iloc[223:228, 1]
            bar_labels_set1 = data.iloc[223:228, 0]

            bar_data_set2 = data.iloc[231:236, 1]
            bar_labels_set2 = data.iloc[231:236, 0]

            # Sort Set1 data from highest to lowest
            sorted_indices_set1 = bar_data_set1.argsort()[::-1]
            bar_data_set1_sorted = bar_data_set1.iloc[sorted_indices_set1]
            bar_labels_set1_sorted = bar_labels_set1.iloc[sorted_indices_set1]

            # Sort Set2 data from highest to lowest
            sorted_indices_set2 = bar_data_set2.argsort()[::-1]
            bar_data_set2_sorted = bar_data_set2.iloc[sorted_indices_set2]
            bar_labels_set2_sorted = bar_labels_set2.iloc[sorted_indices_set2]
            
            # Create a paired bar chart
            fig_paired_bar = go.Figure()

            
            for i in range(len(bar_data_set1_sorted)):
                fig_paired_bar.add_trace(go.Bar(
                    x=[bar_labels_set1_sorted.iloc[i], bar_labels_set2_sorted.iloc[i]],
                    y=[bar_data_set1_sorted.iloc[i], bar_data_set2_sorted.iloc[i]],
                    name=f'Pair {i+1}',
                    text=[bar_data_set1_sorted.iloc[i], bar_data_set2_sorted.iloc[i]],
                    textposition='auto',
                    marker_color=['#FFA033', '#33FF57']  # Different colors for Set1 and Set2 bars
                ))
            fig_paired_bar.update_layout(barmode='group', title="Formal sector vs Informal sector(Formal=orange)")
            
            # Display the paired bar chart
            st.subheader("Formal sector vs Informal sector)")
            st.plotly_chart(fig_paired_bar, use_container_width=True)

            
            col3, col4 = st.columns(2)
            col3.plotly_chart(fig_bar_chart1, use_container_width=True)
            col4.plotly_chart(fig_bar_chart2, use_container_width=True)

            
            st.subheader("Currently studying and Currently studying")
            col5, col6 = st.columns(2)
            employed = data.iloc[6, 1]
            unemployed = data.iloc[7, 1]
            labels_emp = ["Employed", "Unemployed"]
            values_pyt = [employed, unemployed]
            fig_pyt_pie = go.Figure(data=[go.Pie(labels=labels_emp, values=values_pyt)])
            fig_pyt_pie.update_layout(title="Employed vs Unemployed in Labour force ")

            
            additional_data1 = data.iloc[26:30, 1]
            additional_labels1 = data.iloc[28:30, 0]
            additional_labels1 = ["Currently studying", "Not Currently studying"]
            fig_additional_pie1 = go.Figure(data=[go.Pie(labels=additional_labels1, values=additional_data1)])
            col5.plotly_chart(fig_additional_pie1, use_container_width=True)

            
            additional_data2 = data.iloc[256:261, 1]
            additional_labels2 = data.iloc[256:261, 0]
            dditional_labels2 = ["unempolyment"]
            fig_additional_pie2 = go.Figure(data=[go.Pie(labels=additional_labels2, values=additional_data2)])
            col6.plotly_chart(fig_additional_pie2, use_container_width=True)

            
            st.subheader("Technical skills learned")

            additional_data_line = data.iloc[79:126, 2]
            additional_labels_line = data.iloc[79:126, 0]

    
            additional_data_line = additional_data_line[::-1]

            fig_line_male_urban = go.Figure()

    
            fig_line_male_urban.add_trace(go.Scatter(x=additional_labels_line, y=additional_data_line,
                                             mode='lines+markers',
                                             name='Technical skills learned'))

    
            fig_line_male_urban.update_layout(height=1000, width=800)

    # Display the line chart
            st.plotly_chart(fig_line_male_urban)    
            if selected_subcategory == "MALE":
            
             x_values = data.iloc[130:145, 0]
             y_values = data.iloc[130:145, 2]

             # Set custom 
             colors_bars = ["#FF5733", "#FF8247", "#FFA07A", "#FF8247", "#FFA07A","#FFA07A","#FF8247", "#FFA07A","#FF8247", "#FFA07A","#FF8247", "#FFA07A", "#A52A2A"]

             fig_bars = go.Figure(go.Bar(
              x=x_values,
              y=y_values,
              marker=dict(color=colors_bars),  
              ))

           
             fig_bars.update_layout(height=600, width=800,title="Employed population 16+")
             

         
            st.plotly_chart(fig_bars)

            # Set up 
            bar_data1 = data.iloc[30:35, 2]
            bar_labels1 = data.iloc[30:35, 0]
            fig_bar_chart1 = go.Figure(go.Bar(
                x=bar_labels1,
                y=bar_data1,
                name='Set1',
                text=bar_data1,
                textposition='auto',
                marker_color='indianred'
            ))
            fig_bar_chart1.update_layout(title="Education level")

            # Set up the bar
            bar_data2 = data.iloc[11:14, 2]
            bar_labels2 = data.iloc[11:14, 0]
            fig_bar_chart2 = go.Figure(go.Bar(
                x=bar_labels2,
                y=bar_data2,
                name='Set2',
                text=bar_data2,
                textposition='auto',
                marker_color='blue'
            ))
            fig_bar_chart2.update_layout(title="Labour underutilization")

            # Set up the bar chart for rows 41-50 data
            bar_data3 = data.iloc[41:51, 2]
            bar_labels3 = data.iloc[41:51, 0]
            fig_bar_chart3 = go.Figure(go.Bar(
                x=bar_labels3,
                y=bar_data3,
                name='Set3',
                text=bar_data3,
                textposition='auto',
                marker_color='green'
            ))
            fig_bar_chart3.update_layout(title="Program Classification")

            # Set up
            waterfall_data = data.iloc[56:61, 2]
            waterfall_labels = data.iloc[56:61, 0]
            fig_waterfall = go.Figure(go.Waterfall(
                orientation="v",
                measure=["absolute"] * len(waterfall_data),
                x=waterfall_labels,
                y=waterfall_data,
            ))
            fig_waterfall.update_layout(title="Timeframe Options")

            # Set up additional 
            bar_data4 = data.iloc[170:192, 2]
            bar_labels4 = data.iloc[170:192, 0]
 
             
            sorted_indices = bar_data4.argsort()[::-1]
            bar_data4_sorted = bar_data4.iloc[sorted_indices]
            bar_labels4_sorted = bar_labels4.iloc[sorted_indices]

            
            bar_chart_size = 800
            bar_chart_color = 'blue'

            fig_horizontal_bar = go.Figure(go.Bar(
            y=bar_labels4_sorted,
            x=bar_data4_sorted,
            text=bar_data4_sorted,
            textposition='auto',
            orientation='h',  
            marker_color=bar_chart_color,  
          ))
            fig_horizontal_bar.update_layout(title="Employment Sectors Overview", height=bar_chart_size)

             
            st.subheader("Employment Sectors Overview")
            st.plotly_chart(fig_horizontal_bar, use_container_width=True)
            # Set up grouped bar chart for rows 222-236 data
            bar_data_set1 = data.iloc[223:228, 2]
            bar_labels_set1 = data.iloc[223:228, 0]

            bar_data_set2 = data.iloc[231:236, 2]
            bar_labels_set2 = data.iloc[231:236, 0]

            # Sort Set1 data from highest to lowest
            sorted_indices_set1 = bar_data_set1.argsort()[::-1]
            bar_data_set1_sorted = bar_data_set1.iloc[sorted_indices_set1]
            bar_labels_set1_sorted = bar_labels_set1.iloc[sorted_indices_set1]

            # Sort Set2 data from highest to lowest
            sorted_indices_set2 = bar_data_set2.argsort()[::-1]
            bar_data_set2_sorted = bar_data_set2.iloc[sorted_indices_set2]
            bar_labels_set2_sorted = bar_labels_set2.iloc[sorted_indices_set2]
            
            # Create a paired bar chart
            fig_paired_bar = go.Figure()

            
            for i in range(len(bar_data_set1_sorted)):
                fig_paired_bar.add_trace(go.Bar(
                    x=[bar_labels_set1_sorted.iloc[i], bar_labels_set2_sorted.iloc[i]],
                    y=[bar_data_set1_sorted.iloc[i], bar_data_set2_sorted.iloc[i]],
                    name=f'Pair {i+1}',
                    text=[bar_data_set1_sorted.iloc[i], bar_data_set2_sorted.iloc[i]],
                    textposition='auto',
                    marker_color=['#FFA033', '#33FF57']  # Different colors for Set1 and Set2 bars
                ))
            fig_paired_bar.update_layout(barmode='group', title="Formal sector vs Informal sector(Formal=orange)")
            
            # Display the paired bar chart
            st.subheader("Formal sector vs Informal sector)")
            st.plotly_chart(fig_paired_bar, use_container_width=True)

            
            col3, col4 = st.columns(2)
            col3.plotly_chart(fig_bar_chart1, use_container_width=True)
            col4.plotly_chart(fig_bar_chart2, use_container_width=True)

            
            st.subheader("Currently studying and Currently studying")
            col5, col6 = st.columns(2)
            employed = data.iloc[6, 2]
            unemployed = data.iloc[7, 2]
            labels_emp = ["Employed", "Unemployed"]
            values_pyt = [employed, unemployed]
            fig_pyt_pie = go.Figure(data=[go.Pie(labels=labels_emp, values=values_pyt)])
            fig_pyt_pie.update_layout(title="Employed vs Unemployed in Labour force ")

            
            additional_data1 = data.iloc[26:30, 2]
            additional_labels1 = data.iloc[28:30, 0]
            additional_labels1 = ["Currently studying", "Not Currently studying"]
            fig_additional_pie1 = go.Figure(data=[go.Pie(labels=additional_labels1, values=additional_data1)])
            col5.plotly_chart(fig_additional_pie1, use_container_width=True)

            
            additional_data2 = data.iloc[256:261, 2]
            additional_labels2 = data.iloc[256:261, 0]
            dditional_labels2 = ["unempolyment"]
            fig_additional_pie2 = go.Figure(data=[go.Pie(labels=additional_labels2, values=additional_data2)])
            col6.plotly_chart(fig_additional_pie2, use_container_width=True)

            
            st.subheader("Technical skills learned")
            
            
        

            
    additional_data_line = data.iloc[79:126, 2]
    additional_labels_line = data.iloc[79:126, 0]

    
    additional_data_line = additional_data_line[::-1]

    fig_line_male_urban = go.Figure()

    
    fig_line_male_urban.add_trace(go.Scatter(x=additional_labels_line, y=additional_data_line,
                                             mode='lines+markers',
                                             name='Technical skills learned'))

    
    fig_line_male_urban.update_layout(height=1000, width=800)

    # Display the line chart
    st.plotly_chart(fig_line_male_urban)            
        
selected_category = st.sidebar.radio("Select a category:", ["Total Population", "IN GENERAL"])


if selected_category == "IN GENERAL":
    selected_subcategory = st.sidebar.radio("Select a subcategory :", ["in general","MALE","FEMALE"])
else:
    selected_subcategory = None

# Update charts based on the selected category and subcategory
update_charts(selected_category, selected_subcategory)