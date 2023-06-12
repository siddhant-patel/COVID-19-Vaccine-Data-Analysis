# COVID-19-Vaccine-Data-Analysis
This project focuses on utilizing social media mining techniques to analyze data related to COVID-19 vaccine discussions on Twitter. The objective is to crawl Twitter data, process and perform exploratory analysis, and generate intuitive network models to gain insights into the topics and trends surrounding the COVID-19 vaccine.

Project Objectives

    Crawl Twitter data using a non-API based method (snscrape library)
    Collect data for two different time periods to compare and analyze the networks
    Construct and visualize networks using Networkx and Pyvis
    Calculate various network measures such as degree distribution, clustering coefficient, Pagerank, diameter, closeness, and betweenness
    Analyze and compare network characteristics between the two time periods

Features

    Data crawling using snscrape library to scrape tweet attributes (date, ID, content, username, etc.)
    Storage of scraped data in CSV and JSON files
    Creation of directed and undirected networks based on username and hashtag attributes
    Generation of multiple graph visualizations using Networkx, Pyvis, and Matplotlib
    Calculation and storage of network measures in text files
    Plotting of degree distributions and Pagerank distributions for analysis

Observations

The analysis of the network models reveals interesting insights:

    Despite a decrease in COVID-19 cases, discussions about COVID-19 remained prevalent, indicating the continued impact of the pandemic on social media.
    Hashtags related to the COVID-19 vaccine gained popularity over time, indicating increasing awareness and discussion surrounding vaccination efforts.
    The degree of vaccination-related hashtags increased significantly, highlighting the positive impact of social media in disseminating information and raising awareness.

Repository Structure

    data/: Contains the scraped data files (CSV and JSON) for the two time periods.
    network_models/: Contains the generated network models (text files) with information on nodes, edges, and network types.
    graphs/: Contains the generated visualizations of the networks in various graph layouts.
    measures/: Contains the calculated network measures (text files) for further analysis.
    readme.md: Provides an overview of the project and its objectives.

References

    Pyvis documentation: https://pyvis.readthedocs.io/en/latest/documentation.html
    Networkx documentation: https://networkx.org/documentation/stable/reference/index.html
    Matplotlib documentation: https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.html
    snscrape GitHub repository: https://github.com/JustAnotherArchivist/snscrape
    Medium article on scraping tweets with snscrape: https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-531fa919571b
    CDC COVID Data Tracker: Daily and Total Trends: [CDC COVID Data Tracker: Daily and Total Trends](CDC COVID Data Tracker: Daily and Total Trends)

