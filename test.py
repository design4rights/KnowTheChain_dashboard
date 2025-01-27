import streamlit as st

# Add a dropdown menu to the sidebar
menu = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "Dashboard",
        "Settings",
    ],
)

# Display the appropriate page based on the menu selection
if menu == "Home":
    # Define the layout of the landing page
    with st.container():
        st.header("KnowTheChain ICT Benchmark Dashboard")
        st.markdown("""
        This dashboard provides a visual interface to explore and analyze benchmark data on forced labour risks in the ICT sector's global supply chains.  The datasets were compiled during 2018, 2020, and 2022 by KnowTheChain, a multistakeholder initiative that collects data on forced labour risks in global supply chains.
        The benchmark includes data on the performance of 60 leading global electronics manufacturing companies, with regards to their efforts to address forced labor risks in their global supply chains.""")
        with st.expander("About Know the Chain"):
            st.markdown("""
            [KnowTheChain]('https://knowthechain.org/') is a resource for companies and investors to understand and address forced labor risks within their global supply chains. It is a partnership between Humanity United, the Business & Human Rights Resource Centre, Sustainalytics, and Verite. 
            
            KnowTheChain focuses on assessing the largest companies (based on market capitalisation) in high-risk sectors. The [KnowTheChain benchmarks]('https://knowthechain.org/benchmark/') evaluate corporate efforts to assess forced labour risks in their supply chains and publishes sector-specific benchmarks every two years. Companies are assessed using a methodology which is based on the UN Guiding Principles on Business and Human Rights and which covers themes such as recruitment and worker voice.
            
            The KnowTheChain datasets and assessment methodology used to develop this app are accessible, along with official summary reports and briefings, from the [KnowTheChain website]('https://knowthechain.org/using-our-data/). """) 

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
            
            Note that due to changes in the assessment methodology year-on-year, the Know the Chain benchmark datasets are not suitable for observing trends over time.
        """)

elif menu == "Dashboard":
    st.sidebar.image("https://knowthechain.org/wp-content/uploads/large-1-e1481137870510.png")
    st.sidebar.markdown("""
    To get started, select a year, region, theme, and plot type from the sidebar. You can also select 'All' for the region to see data for all regions.
