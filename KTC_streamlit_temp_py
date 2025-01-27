# ktc_ict_2022 = pd.read_csv("C:/Users/kokuo/OneDrive/Study Files/Python/Visualisation Experiments/Know the Chain/KTC ICT Benchmark CSV Data/2022 KCT ICT.csv")
# ktc_ict_2020 = pd.read_csv("C:/Users/kokuo/OneDrive/Study Files/Python/Visualisation Experiments/Know the Chain/KTC ICT Benchmark CSV Data/2020 KCT ICT.csv")
# ktc_ict_2018 = pd.read_csv("C:/Users/kokuo/OneDrive/Study Files/Python/Visualisation Experiments/Know the Chain/KTC ICT Benchmark CSV Data/2018 KCT ICT.csv")

### NOTES ###

# Data sourced from https://knowthechain.org/benchmark/

# Data Pre-Processing:

# Excel files modified for Pandas CSV readable format
# Columns 'Total Benchmark Score' and '20XX rank' moved in all three files to columns 2 and 3
# Rows 2-4 consolidated and moved in all three files into row 1
# New sub-indicator 'score total' columns added in 2018 and 2020 files to match format of 2022 file
# Column headers edited as necessary to ensure consistency across all three files  

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

### User interface and style formatting ### 

st.set_page_config(page_title="KnowTheChain ICT Dashboard", page_icon="🔍", layout="wide", initial_sidebar_state="expanded")

with st.container():
    st.header("KnowTheChain ICT Benchmark Dashboard")
    st.markdown("""
    This dashboard was developed by Joanna Lovatt in May 2022 as a coursework project for an Introduction to Python module. The dashboard provides a visual interface to explore and analyze benchmark data on forced labour risks in the ICT sector's global supply chains. The benchmark includes data on the performance of 60 leading global electronics manufacturing companies. The datasets were compiled during 2018, 2020, and 2022 by KnowTheChain, a multistakeholder initiative that collects data on forced labour risks in global supply chains.""")
    
    with st.expander("About KnowTheChain"):
        st.markdown("""
        [KnowTheChain](https://knowthechain.org/) is a resource for companies and investors to understand and address forced labor risks within their global supply chains. It is a partnership between Humanity United, the Business & Human Rights Resource Centre, Sustainalytics, and Verite. 
        
        KnowTheChain focuses on assessing the largest companies (based on market capitalisation) in high-risk sectors. The [KnowTheChain benchmarks](https://knowthechain.org/benchmark/) evaluate corporate efforts to assess forced labour risks in their supply chains and publishes sector-specific benchmarks every two years. Companies are assessed using a methodology which is based on the [UN Guiding Principles on Business and Human Rights](https://www.ohchr.org/sites/default/files/documents/publications/guidingprinciplesbusinesshr_en.pdf) and the [OECD Responsible Business Conduct guidelines](https://www.oecd.org/investment/due-diligence-guidance-for-responsible-business-conduct.htm), and which covers themes such as recruitment and worker voice.
        
        The KnowTheChain datasets and assessment methodology used to develop this app are accessible, along with official summary reports and briefings, from the [KnowTheChain website](https://knowthechain.org/using-our-data/). """) 

    with st.expander("Why forced labour?"):
        st.markdown("""
        Forced labor is a pervasive problem across all corporate supply chains. Despite efforts from policy makers, civil society, investors, and companies themselves, the International Labour Organization estimates that 24.9 million people are victims of forced labor globally. Forced labor in the private economy generates USD$150 billion in illegal profits each year.
        
        In the wake of forced labor abuse revelations in global supply chains, companies are increasingly expected by consumers, investors, media, and governments to maintain transparent and responsible supply chains.""")
    
    with st.expander("How to use this dashboard"):
        st.markdown("""
        The data dashboard is designed to provide users with a comprehensive view of the performance of companies assessed in the ICT benchmark across several dimensions. 
        
        - Firstly, users can explore how companies perform in relation to their industry peers, using metrics such as the total benchmark score and individual theme scores.
        
        - Secondly, users can compare the performance of companies across different countries and regions included in the assessment, allowing for insights into regional trends and variations.
        
        - Additionally, users can filter the dataset by specific themes or regions to gain a more focused understanding of performance in these areas.
        
        Note that due to changes in the assessment methodology year-on-year, the KnowTheChain benchmark datasets are not suitable for observing trends over time.""")

st.sidebar.image("https://knowthechain.org/wp-content/uploads/large-1-e1481137870510.png")
st.sidebar.markdown("""
To get started, select a year, region, theme, and plot type from the sidebar. You can also select 'All' for the region to see data for all regions.
""")

ktc_ict_2022 = pd.read_csv("C:/Users/kokuo/OneDrive/Study Files/Python/Visualisation Experiments/Know the Chain/KTC ICT Benchmark CSV Data/2022 KCT ICT.csv")
ktc_ict_2020 = pd.read_csv("C:/Users/kokuo/OneDrive/Study Files/Python/Visualisation Experiments/Know the Chain/KTC ICT Benchmark CSV Data/2020 KCT ICT.csv")
ktc_ict_2018 = pd.read_csv("C:/Users/kokuo/OneDrive/Study Files/Python/Visualisation Experiments/Know the Chain/KTC ICT Benchmark CSV Data/2018 KCT ICT.csv")

# Dictionary of dataframes
data_dict = {"2022": ktc_ict_2022,
             "2020": ktc_ict_2020,
             "2018": ktc_ict_2018}

# List of regions for the selected year
selected_year = st.sidebar.selectbox("Select a year", options=list(data_dict.keys()))

# Selected dataframe display
selected_df = data_dict[selected_year]

# List of regions for the selected year
regions = ["All"] + selected_df["Region"].unique().tolist()

# User's selection for the region filter
selected_region = st.sidebar.selectbox("Select a region", options=regions)

# Dataframe filter for selected region
if selected_region != "All":
    selected_df = selected_df[selected_df["Region"] == selected_region]

# Dictionary of plot types
theme_dict = {"Overall ICT Benchmark Scores": "bar",
              "Theme 1: Commitment & Governance": "bar",
             "Theme 2: Traceability & Risk Assessment": "bar",
             "Theme 3: Purchasing Practices": "bar",
             "Theme 4: Recruitment": "bar",
             "Theme 5: Worker Voice": "bar",
             "Theme 6: Monitoring": "bar",
             "Theme 7: Remedy": "bar"}

# User's selection for the theme type
selected_theme = st.sidebar.selectbox("Select a theme", options=list(theme_dict.keys()))

# User's selection for plot type
plot_dict = {"Average score": "bar",
             "Relative score (by company)": "scatter",
             "Company score vs. market capitalization": "scatter"}

selected_plot = st.sidebar.selectbox("Select plot to display", options=list(plot_dict.keys()))


### Plot creation ###


# Total benchmark figures

if selected_theme == "Overall ICT Benchmark Scores":
    st.markdown("### Overall ICT Benchmark Scores")
    st.markdown("""
            The KnowTheChain ICT [benchmark methodology](https://knowthechain.org/benchmark-methodology/) assesses companies’ efforts to address forced labor risks in their supply chains. It is based on the UN Guiding Principles on Business and Human Rights and covers policy commitments, due diligence, and remedy. 
            
            The methodology uses the ILO core labor standards (which cover the human rights that the ILO has declared to be fundamental rights at work: freedom of association, the right to collective bargaining, and the elimination of forced labor, child labor, and discrimination) as a baseline standard. 
            
            The methodology has been developed through consultation with a wide range of stakeholders and a review of other benchmarks, frameworks, and guidelines such as the OECD Due Diligence Guidance on Responsible Business Conduct.""")
    if selected_plot == "Average score":
        mean_scores = selected_df.loc[:, 'Theme 1: Commitment & Governance':'Theme 7: Remedy'].mean()
        selected_columns = selected_df.iloc[:, [0, 2, 7, 8, 9, 10, 11, 12, 13]].sort_values(by=[selected_df.columns[2]], ascending=True)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=mean_scores, y=mean_scores.index, orientation='h'))
        fig.update_layout(title=f"Average Benchmark Scores for Each Theme ({selected_year} - {selected_region})", xaxis_title="Average benchmark scores by theme", yaxis_title='Theme')

    elif selected_plot == "Relative score (by company)":
        selected_columns = selected_df.iloc[:, [0, 1, 2, 3, 4, 5]].sort_values(by=[selected_df.columns[2]], ascending=True)
        fig = px.scatter(selected_df, x="Country", y="Total benchmark score", color="Region",
                 title=f"Total Benchmark Scores by Company and Country ({selected_year} - {selected_region})", symbol="Company Name", size_max=10)
        fig.update_layout(xaxis_title="Country", yaxis_title="Total benchmark score")

    elif selected_plot == "Company score vs. market capitalization":
        selected_columns = selected_df.iloc[:, [0, 1, 2, 3, 4, 5]].sort_values(by=[selected_df.columns[2]], ascending=True)
        fig = px.scatter(selected_df, x="Market cap (US$bn)", y="Total benchmark score", color="Region",
                 title=f"Total Benchmark Score vs Market Cap by Company ({selected_year} - {selected_region})", size_max=10)
        fig.update_layout(xaxis_title="Market Cap (US$bn)", yaxis_title="Total Benchmark Score")

# Theme 1 figures

elif selected_theme == "Theme 1: Commitment & Governance":
    st.markdown("### Theme 1: Commitment & Governance")
    st.markdown("""
            The Commitment & Governance theme assesses a company's policies and practices related to addressing forced labor and human trafficking in its operations and supply chain.
            """)
    with st.expander("Commitment & Governance Indicators"):
        st.markdown("""
        
            - **Supplier code of conduct and capacity building:** The company has a supplier code of conduct that requires suppliers throughout its supply chains to respect the ILO core labour standards, including elimination of forced labour.
            The company takes steps to ensure that suppliers in different tiers of its supply chains are aware of risks related to forced labour and are effectively implementing the company's policies.
        
            - **Management and accountability:** The company has established clear responsibilities and accountability for the implementation of its supply chain policies that address forced labour, both within the company and at board level.
        
            """)
    with st.expander("Commitment & Governance Sources"):
        st.markdown("""

        - **UN Guiding Principle 16:** "Policy commitment should be approved at senior level, is informed by relevant internal or external expertise, stipulates the human rights expectations of personnel, business partners, or other parties directly linked to its operations, products, or services, is publicly available and communicated, and is reflected in operational policies and procedures and embedded throughout the business."

        - **OECD Responsible Business Conduct Guidelines 1.1:** "Devise, adopt and disseminate a combination of policies on RBC issues that articulate the enterprise’s commitments to the principles and standards contained in the OECD Guidelines for MNEs and its plans for implementing due diligence, which will be relevant for the enterprise’s own operations, its supply chain and other business relationships."

        """)

    if selected_plot == "Average score":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 7]].sort_values(by=[selected_df.columns[7]], ascending=False)
        grouped_df = selected_df.groupby("Country", as_index=False)["Theme 1: Commitment & Governance"].mean()
        fig = px.bar(grouped_df, x="Country", y="Theme 1: Commitment & Governance", color="Country",
                 title=f"Average Benchmark Scores by Country ({selected_year} - {selected_region})")
        
    elif selected_plot == "Relative score (by company)":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 7]].sort_values(by=[selected_df.columns[7]], ascending=False)
        fig = px.scatter(selected_df, x="Country", y="Theme 1: Commitment & Governance", color="Region",
                 title=f"Commitment & Governance Scores by Company and Country ({selected_year} - {selected_region})", symbol="Company Name", size_max=10)
        fig.update_layout(xaxis_title="Country", yaxis_title="Theme 1: Commitment & Governance")

    elif selected_plot == "Company score vs. market capitalization":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 7]].sort_values(by=[selected_df.columns[7]], ascending=False)
        fig = px.scatter(selected_df, x="Market cap (US$bn)", y="Theme 1: Commitment & Governance", color="Region", hover_data=["Company Name", "Country"],
                 title=f"Theme 1: Commitment & Governance Scores vs Market Cap by Company ({selected_year} - {selected_region})")
        fig.update_layout(xaxis_title="Market Cap (US$bn)", yaxis_title="Theme 1: Commitment & Governance")

# Theme 2: Traceability & Risk Assessment

elif selected_theme == "Theme 2: Traceability & Risk Assessment":
    st.markdown("### Theme 2: Traceability & Risk Assessment")
    st.markdown("""
            The Traceability & Risk Assessment theme assesses a company's practices for assessing labour rights risks throughout its supply chain, as well as whether and how it discloses and takes action to address those risks.
            """)
    with st.expander("Traceability & Risk Assessment Indicators"):
        st.markdown("""
            - **Traceability and supply chain transparency:** The company demonstrates an understanding of where its supply chains are located by publicly disclosing the names and addresses of its first-tier suppliers, the names and locations of its below-first-tier suppliers, and the sourcing countries of raw materials at high risk of forced labour.
            
            - **Risk Assessment:** The company has a process to assess forced labour risks, discloses forced labour risks identified in different tiers of its supply chains, and discloses how it works with workers and other stakeholders to address the risks identified.
            """)
    with st.expander("Traceability & Risks Assessment Sources"):
        st.markdown("""
            - **UN Guiding Principle 17:** "Due diligence should include assessments of actual and potential adverse human rights impacts, integrating and acting upon these findings, tracking responses, and communicating how the impacts are addressed. Due diligence should also cover adverse impacts that a business causes, contributes, or is directly linked to, will vary in complexity according to the business, and should be ongoing and adaptive to the shifting context."
            
            - **UN Guiding Principle 18:** "In order to identify actual and potential adverse human rights impacts, business enterprises should draw on internal and/or independent external human rights expertise, and meaningfully consult with potentially affected groups and other affected stakeholders."
            
            - **OECD Responsible Business Conduct Guidelines 2.1:** "Carry  out a broad scoping exercise to identify all areas of the business, across its operations and relationships, including in its supply chains, where RBC risks are most likely to be present and most significant. Relevant elements include, among others, information about sectoral, geographic, product and enterprise risk factors, including known risks the enterprise has faced or is likely to face. The scoping exercise should enable the enterprise to carry out an initial prioritisation of the most significant risk areas for further assessment. For enterprises with less diverse operations, in particular smaller enterprises, a scoping exercise may not be necessary before moving to the stage of identifying and prioritising specific impacts."
            
            - **OECD Responsible Business Conduct Guidelines 2.2:** "Starting with the significant areas of risk identified above, carry out iterative and increasingly in-depth assessments of prioritised operations, suppliers and other business relationships in order to identify and assess specific actual and potential adverse RBC impacts."
            """)

    if selected_plot == "Average score":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 8]].sort_values(by=[selected_df.columns[8]], ascending=False)
        grouped_df = selected_df.groupby("Country", as_index=False)["Theme 2: Traceability & Risk Assessment"].mean()
        fig = px.bar(grouped_df, x="Country", y="Theme 2: Traceability & Risk Assessment", color="Country",
                 title=f"Average Benchmark Scores by Country ({selected_year} - {selected_region})")
        
    elif selected_plot == "Relative score (by company)":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 8]].sort_values(by=[selected_df.columns[8]], ascending=False)
        fig = px.scatter(selected_df, x="Country", y="Theme 2: Traceability & Risk Assessment", color="Region",
                 title=f"Theme 2: Traceability & Risk Assessment Scores by Company and Country ({selected_year} - {selected_region})", symbol="Company Name", size_max=10)
        fig.update_layout(xaxis_title="Country", yaxis_title="Theme 2: Traceability & Risk Assessment")

    elif selected_plot == "Company score vs. market capitalization":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 8]].sort_values(by=[selected_df.columns[8]], ascending=False)
        fig = px.scatter(selected_df, x="Market cap (US$bn)", y="Theme 2: Traceability & Risk Assessment", color="Region", hover_data=["Company Name", "Country"],
                 title=f"Theme 2: Traceability & Risk Assessment Scores vs Market Cap by Company ({selected_year} - {selected_region})")
        fig.update_layout(xaxis_title="Market Cap (US$bn)", yaxis_title="Theme 2: Traceability & Risk Assessment")

# Theme 3: Purchasing Practices

elif selected_theme == "Theme 3: Purchasing Practices":
    st.markdown("### Theme 3: Purchasing Practices")
    st.markdown("""
            The Purchasing Practices theme assesses a company's policies and processes for addressing labour risks related to purchasing practices and the first tier of its supply chains.
            """)
    with st.expander("Purchasing Practices Indicators"):
        st.markdown("""
            - **Purchasing Practices:** The company has adopted responsible purchasing practices in the first tier of its supply chains, which it demonstrates through disclosing quantitative data points. The company also integrates its own commitment to responsible buying practices into contracts with its suppliers.""")
    with st.expander("Purchasing Practices Sources"):
        st.markdown("""
            - **UN Guiding Principle 16:** "Policy commitment should be approved at senior level, is informed by relevant internal or external expertise, stipulates the human rights expectations of personnel, business partners, or other parties directly linked to its operations, products, or services, is publicly available and communicated, and is reflected in operational policies and procedures and embedded throughout the business."
            """)

    if selected_plot == "Average score":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 9]].sort_values(by=[selected_df.columns[9]], ascending=False)
        grouped_df = selected_df.groupby("Country", as_index=False)["Theme 3: Purchasing Practices"].mean()
        fig = px.bar(grouped_df, x="Country", y="Theme 3: Purchasing Practices", color="Country",
                 title=f"Average Benchmark Scores by Country ({selected_year} - {selected_region})")
        
    elif selected_plot == "Relative score (by company)":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 9]].sort_values(by=[selected_df.columns[9]], ascending=False)
        fig = px.scatter(selected_df, x="Country", y="Theme 3: Purchasing Practices", color="Region",
                 title=f"Theme 3: Purchasing Practices Scores by Company and Country ({selected_year} - {selected_region})", symbol="Company Name", size_max=10)
        fig.update_layout(xaxis_title="Country", yaxis_title="Theme 3: Purchasing Practices")

    elif selected_plot == "Company score vs. market capitalization":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 9]].sort_values(by=[selected_df.columns[9]], ascending=False)
        fig = px.scatter(selected_df, x="Market cap (US$bn)", y="Theme 3: Purchasing Practices", color="Region", hover_data=["Company Name", "Country"],
                 title=f"Theme 3: Purchasing Practices Scores vs Market Cap by Company ({selected_year} - {selected_region})")
        fig.update_layout(xaxis_title="Market Cap (US$bn)", yaxis_title="Theme 3: Purchasing Practices")

# Theme 4: Recruitment

elif selected_theme == "Theme 4: Recruitment":
    st.markdown("### Theme 4: Recruitment")
    st.markdown("""
            The Recruitment theme assesses a company's recruitment practices relating to recruitment fees and the use of recruitment agencies by its suppliers.
            """)
    with st.expander("Recruitment Indicators"):
        st.markdown("""
            - **Recruitment-related fees:** The company requires that no worker in its supply chains should pay for a job—the costs of recruitment (i.e., recruitment fees and related costs) should be borne not by the worker but by the employer ("Employer Pays Principle"). If it discovers that fees have been paid by workers in its supply chains, the company provides evidence that fees have been repaid to workers. The company discloses how it works to prevent worker payment of recruitment-related fees in different supply chain contexts.
            
            - **Responsible Recruitment:** The company maps its labour supply chains and discloses information on the recruitment agencies used by its suppliers. Further, it provides details of how it supports responsible recruitment in its supply chains.""")
    with st.expander("Recruitment Sources"):
        st.markdown("""
        - **UN Guiding Principle 15:** "Companies should have in place a human rights policy, a due diligence process, and a remedy process."
        
        - **UN Guiding Principle 17:** "Due diligence should include assessments of actual and potential adverse human rights impacts, integrating and acting upon these findings, tracking responses, and communicating how the impacts are addressed. Due diligence should also cover adverse impacts that a business causes, contributes, or is directly linked to, will vary in complexity according to the business, and should be ongoing and adaptive to the shifting context."
        
        - **UN Guiding Principle 22:** "Businesses should provide for or cooperate in remediation where they have caused or contributed towards adverse impacts."
        
        - **OECD Responsible Business Conduct Guidelines 2.2:** "Starting with the significant areas of risk identified above, carry out iterative and increasingly in-depth assessments of prioritised operations, suppliers and other business relationships in order to identify and assess specific actual and potential adverse RBC impacts."
        
        - **OECD Responsible Business Conduct Guidelines 6.1:** "When the enterprise identifies that it has caused or contributed to actual adverse impacts, address such impacts by providing for or cooperating in their remediation."
            """)

    if selected_plot == "Average score":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 10]].sort_values(by=[selected_df.columns[10]], ascending=False)
        grouped_df = selected_df.groupby("Country", as_index=False)["Theme 4: Recruitment"].mean()
        fig = px.bar(grouped_df, x="Country", y="Theme 4: Recruitment", color="Country",
                 title=f"Average Benchmark Scores by Country ({selected_year} - {selected_region})")
        
    elif selected_plot == "Relative score (by company)":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 10]].sort_values(by=[selected_df.columns[10]], ascending=False)
        fig = px.scatter(selected_df, x="Country", y="Theme 4: Recruitment", color="Region",
                 title=f"Theme 4: Recruitment Scores by Company and Country ({selected_year} - {selected_region})", symbol="Company Name", size_max=10)
        fig.update_layout(xaxis_title="Country", yaxis_title="Theme 4: Recruitment")

    elif selected_plot == "Company score vs. market capitalization":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 10]].sort_values(by=[selected_df.columns[10]], ascending=False)
        fig = px.scatter(selected_df, x="Market cap (US$bn)", y="Theme 4: Recruitment", color="Region", hover_data=["Company Name", "Country"],
                 title=f"Theme 4: Recruitment Scores vs Market Cap by Company ({selected_year} - {selected_region})")
        fig.update_layout(xaxis_title="Market Cap (US$bn)", yaxis_title="Theme 4: Recruitment")

# Theme 5: Worker Voice
    
elif selected_theme == "Theme 5: Worker Voice":
    st.markdown("### Theme 5: Worker Voice")
    st.markdown("""
            The Worker Voice theme assesses a company's efforts to support worker organising, collective bargaining, and the establishment of operational grievance mechanisms throughout the supply chain. 
            """)
    with st.expander("Worker Voice Indicators"):
        st.markdown("""
            - **Freedom of Association:** To support collective worker empowerment, the company works with local or global trade unions to support freedom of association in its supply chains. It enters into a global framework agreement that covers its supply chains and/or an enforceable supply chain labour rights agreement with trade unions or worker organisations
            
            - **Grievance Mechanism:** The company takes steps to ensure a formal mechanism to report a grievance to an impartial entity regarding labor conditions in the company's supply chains is available to its suppliers' workers and their legitimate representatives. The company ensures that the mechanism is effective across its supply chains.""")
    with st.expander("Worker Voice Sources"):
        st.markdown("""
            - **UN Guiding Principle 29:** "Businesses should establish or participate in effective operational grievance mechanisms for individuals and communities who may be adversely affected."
            
            - **UN Guiding Principle 31:** "Non-judicial grievance mechanisms should be legitimate, accessible, predictable, equitable, transparent, rights compatible, and a source of continuous learning."
            
            - **OECD Responsible Business Conduct Guidelines 6.2:** "When appropriate, provide for or cooperate with legitimate remediation mechanisms through which impacted stakeholders and rightsholders can raise complaints and seek to have them addressed with the enterprise. Referral of an alleged impact to a legitimate remediation mechanism may be particularly helpful in situations where there are disagreements on whether the enterprise caused or contributed to adverse impacts, or on the nature and extent of remediation to be provided." 
            """)

    if selected_plot == "Average score":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 11]].sort_values(by=[selected_df.columns[11]], ascending=False)
        grouped_df = selected_df.groupby("Country", as_index=False)["Theme 5: Worker Voice"].mean()
        fig = px.bar(grouped_df, x="Country", y="Theme 5: Worker Voice", color="Country",
                 title=f"Average Benchmark Scores by Country ({selected_year} - {selected_region})")
        
    elif selected_plot == "Relative score (by company)":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 11]].sort_values(by=[selected_df.columns[11]], ascending=False)
        fig = px.scatter(selected_df, x="Country", y="Theme 5: Worker Voice", color="Region",
                 title=f"Theme 5: Worker Voice by Company and Country ({selected_year} - {selected_region})", symbol="Company Name", size_max=10)
        fig.update_layout(xaxis_title="Country", yaxis_title="Theme 5: Worker Voice")

    elif selected_plot == "Company score vs. market capitalization":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 11]].sort_values(by=[selected_df.columns[11]], ascending=False)
        fig = px.scatter(selected_df, x="Market cap (US$bn)", y="Theme 5: Worker Voice", color="Region", hover_data=["Company Name", "Country"],
                 title=f"Theme 5: Worker Voice vs Market Cap by Company ({selected_year} - {selected_region})")
        fig.update_layout(xaxis_title="Market Cap (US$bn)", yaxis_title="Theme 5: Worker Voice")

# Theme 6: Monitoring

elif selected_theme == "Theme 6: Monitoring":
    st.markdown("### Theme 6: Monitoring")
    st.markdown("""
            The Monitoring theme assesses a company's efforts to engage with both internal and external stakeholders to track the effectiveness of its response to labour risks in the supply chain, as well as efforts to disclose the findings of these engagements.""")
    with st.expander("Monitoring Indicators"):
        st.markdown("""
            - **Monitoring:** The company discloses the findings of its monitoring processes, including details regarding any violations revealed across supply chain tiers. The company uses worker-driven monitoring (i.e., monitoring undertaken by independent organisations, such as local workerled organizations, unions, or local civil society partners) to ensure full identification of labor rights violations by those who are on the ground, all year round.
            """)
    with st.expander("Monitoring Sources"):
        st.markdown("""
            - **UN Guiding Principle 20:** "Businesses should track the effectiveness of their response, based on qualitative and quantitative feedback and feedback from both internal and external sources, including affected stakeholders."
            """)

    if selected_plot == "Average score":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 12]].sort_values(by=[selected_df.columns[12]], ascending=False)
        grouped_df = selected_df.groupby("Country", as_index=False)["Theme 6: Monitoring"].mean()
        fig = px.bar(grouped_df, x="Country", y="Theme 6: Monitoring", color="Country",
                 title=f"Average Benchmark Scores by Country ({selected_year} - {selected_region})")
        
    elif selected_plot == "Relative score (by company)":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 12]].sort_values(by=[selected_df.columns[12]], ascending=False)
        fig = px.scatter(selected_df, x="Country", y="Theme 6: Monitoring", color="Region",
                 title=f"Theme 6: Monitoring by Company and Country ({selected_year} - {selected_region})", symbol="Company Name", size_max=10)
        fig.update_layout(xaxis_title="Country", yaxis_title="Theme 6: Monitoring")

    elif selected_plot == "Company score vs. market capitalization":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 12]].sort_values(by=[selected_df.columns[12]], ascending=False)
        fig = px.scatter(selected_df, x="Market cap (US$bn)", y="Theme 6: Monitoring", color="Region", hover_data=["Company Name", "Country"],
                 title=f"Theme 6: Monitoring vs Market Cap by Company ({selected_year} - {selected_region})")
        fig.update_layout(xaxis_title="Market Cap (US$bn)", yaxis_title="Theme 6: Monitoring")

# Theme 7: Remedy

elif selected_theme == "Theme 7: Remedy":
    st.markdown("### Theme 7: Remedy")
    st.markdown("""
            The Remedy Theme assesses a company's policies and practices for providing remedy to workers in its supply chains in cases of forced labour, as well as the steps the company has taken to identify parts of its supply chain where the risk of forced labour is high, and the steps the company has taken to mitigate this risk in the future.""")
    with st.expander("Remedy Indicators"):
        st.markdown("""
            - **Remedy Programs and Response to Allegations:** 
                - The company has a process to provide remedy to workers in its supply chains in cases of forced labour and discloses examples of outcomes of its remedy process for its suppliers' workers
                - If one or more allegations regarding forced labor in the company's supply chains have been identified, the company engages in a dialogue with the stakeholders reportedly affected in the allegation and takes steps to ensure the provision of remedy that is satisfactory to the victims or groups representing the victims.
            """)
    with st.expander("Remedy Sources"):
        st.markdown("""
            - **UN Guiding Principle 15:** "Companies have in place a human rights policy, a due diligence process, and a remedy process"
            
            - **UN Guiding Principle 22:** "Businesses should provide for or cooperate in remediation where they have caused or contributed towards adverse impacts."
            
            - **OECD Responsible Business Conduct Guidelines 6.1:** "When the enterprise identifies that it has caused or contributed to actual adverse impacts, address such impacts by providing for or cooperating in their remediation."
            """)

    if selected_plot == "Average score":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 13]].sort_values(by=[selected_df.columns[13]], ascending=False)
        grouped_df = selected_df.groupby("Country", as_index=False)["Theme 7: Remedy"].mean()
        fig = px.bar(grouped_df, x="Country", y="Theme 7: Remedy", color="Country",
                 title=f"Average Benchmark Scores by Country ({selected_year} - {selected_region})")
        
    elif selected_plot == "Relative score (by company)":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 13]].sort_values(by=[selected_df.columns[13]], ascending=False)
        fig = px.scatter(selected_df, x="Country", y="Theme 7: Remedy", color="Region",
                 title=f"Theme 7: Remedy by Company and Country ({selected_year} - {selected_region})", symbol="Company Name", size_max=10)
        fig.update_layout(xaxis_title="Country", yaxis_title="Theme 7: Remedy")

    elif selected_plot == "Company score vs. market capitalization":
        selected_columns = selected_df.iloc[:, [0, 2, 3, 4, 5, 13]].sort_values(by=[selected_df.columns[13]], ascending=False)
        fig = px.scatter(selected_df, x="Market cap (US$bn)", y="Theme 7: Remedy", color="Region", hover_data=["Company Name", "Country"],
                 title=f"Theme 7: Remedy vs Market Cap by Company ({selected_year} - {selected_region})")
        fig.update_layout(xaxis_title="Market Cap (US$bn)", yaxis_title="Theme 7: Remedy")

# Display the plot

st.plotly_chart(fig)
st.table(selected_columns)

