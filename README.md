# Vanguard Customer Experience Analysis
<p align="center">
<img src="https://fondosindexados.es/wp-content/uploads/2018/08/fondos-vanguard-logo.jpg" alt="Vanguard Logo">
</p>

## Project Overview

This project involves analyzing the results of a digital experiment conducted by **Vanguard**, a US-based investment management company. The goal is to determine whether a modernized, more intuitive user interface (UI) and timely contextual cues could improve the online process completion rates for Vanguard customers.

The experiment involved an A/B test with a **control group** (using the traditional UI) and a **test group** (using the new UI). By analyzing the data from this experiment, the aim is to see if the changes in the UI led to an improved user experience and higher process completion rates.

## Relevant Insights and conclusions 
[Tableau story - Clients analysis.](https://public.tableau.com/views/ABTesting_Project_Clients_Analysis/Clientinsights?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
[PowerBI dashboard - Relevant Insights](https://youtu.be/risEWolXBHs)

## The Digital Challenge

Vanguard’s digital transformation aimed to enhance the online user experience by:
- Implementing a more intuitive UI.
- Adding contextual prompts such as messages, suggestions, or instructions.

The central question is: **Did these changes lead to more customers completing the process?**

### Experiment Overview
The A/B test was conducted from **March 15, 2017** to **June 20, 2017**, comparing:
- **Control Group**: Customers interacted with the traditional Vanguard online process.
- **Test Group**: Customers experienced the new, improved digital interface.

Both groups went through the same sequence: a landing page, three subsequent steps, and a confirmation page indicating process completion.

## Objectives

The main objective of this project is to:
- Analyze if the **new UI** leads to better **completion rates** compared to the traditional UI.
- Explore demographic factors that might influence the results, such as **age**, **gender**, or **account type**.
- Provide data-driven insights and recommendations based on the experiment results.

## Analysis Plan

1. **Data Cleaning & Preprocessing**:
   - Merge and clean the digital footprints dataset (`df_final_web_data` part 1 and part 2).
   - Handle missing values and ensure consistency in the customer profile data.
   
2. **Exploratory Data Analysis (EDA)**:
   - Analyze completion rates for both the control and test groups.
   - Investigate the impact of demographic factors on the experiment outcomes.

3. **Statistical Testing**:
   - Perform statistical tests to determine if the differences between the control and test groups are significant.
   - Use tools like **A/B testing** to quantify the effect of the new UI.

4. **Conclusion**:
   - Provide insights into whether the new UI improves the process completion rate.
   - Offer recommendations for future improvements based on data analysis.

## Tools & Technologies

- **Python** for data manipulation and analysis.
- **Pandas** for handling datasets.
- **Seaborn** and **Matplotlib** for data visualization.
- **SciPy/Statsmodels** for statistical testing (A/B test analysis).

## Datasets

The following datasets are used for this analysis:

1. **Customer Profiles (`df_final_demo`)**: Contains demographic data like age, gender, and account details of Vanguard's customers.
   
2. **Digital Footprints (`df_final_web_data`)**: Provides detailed records of online customer interactions, split into two parts (`pt_1` and `pt_2`). These parts must be merged before in-depth analysis.

3. **Experiment List (`df_final_experiment_clients`)**: Reveals which customers participated in the A/B experiment (either as part of the control or test group).

    [\[Link to source\]](https://github.com/ivanalonsom/Project5_EDA_Inferential_Stats/tree/main/original_data)

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/ivanalonsom/Project5_EDA_Inferential_Stats.git
2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
3. Open and run the Jupyter notebooks for data analysis and visualization. 
