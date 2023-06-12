import snscrape.modules.twitter as sntwitter
import networkx as nx 
import pandas as pd
import json
from pyvis.network import Network
import matplotlib.pyplot as plt
import codecs

tweets_list = []
tweets_list2 = []

for i,tweet_attributes in enumerate(sntwitter.TwitterSearchScraper('COVID19 Vaccine since:2021-12-01 until:2022-02-01').get_items()):
    if i>300:
        break
    tweets_list.append([tweet_attributes.date, tweet_attributes.id, tweet_attributes.rawContent, tweet_attributes.url, tweet_attributes.user.username, tweet_attributes.user.followersCount, tweet_attributes.replyCount, 
                        tweet_attributes.retweetCount, tweet_attributes.likeCount, tweet_attributes.quoteCount, tweet_attributes.lang, tweet_attributes.links, tweet_attributes.media, tweet_attributes.retweetedTweet, 
                        tweet_attributes.quotedTweet, tweet_attributes.inReplyToTweetId, tweet_attributes.inReplyToUser, tweet_attributes.mentionedUsers, tweet_attributes.coordinates, tweet_attributes.place, 
                        tweet_attributes.hashtags])
    
tweets_df = pd.DataFrame(tweets_list, columns=['Date','ID', 'Tweet Text', 'Tweet URL', 'Username', 'Follower Count', 'Reply Count', 'Retweet Count',
                                              'Like Count', 'Quote Count', 'Language', 'Outlinks', 'Media', 'Retweeted Tweet', 'Quoted Tweet', 'Replier ID',
                                               'Replier Username', 'Mentioned Users', 'Coordinates', 'Place', 'Hashtags'])

for i,tweet_attributes in enumerate(sntwitter.TwitterSearchScraper('COVID19 Vaccine since:2021-05-15 until:2021-07-15').get_items()):
    if i>300:
        break
    tweets_list2.append([tweet_attributes.date, tweet_attributes.id, tweet_attributes.rawContent, tweet_attributes.url, tweet_attributes.user.username, tweet_attributes.user.followersCount, tweet_attributes.replyCount, 
                        tweet_attributes.retweetCount, tweet_attributes.likeCount, tweet_attributes.quoteCount, tweet_attributes.lang, tweet_attributes.links, tweet_attributes.media, tweet_attributes.retweetedTweet, 
                        tweet_attributes.quotedTweet, tweet_attributes.inReplyToTweetId, tweet_attributes.inReplyToUser, tweet_attributes.mentionedUsers, tweet_attributes.coordinates, tweet_attributes.place, 
                        tweet_attributes.hashtags])
    

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Date','ID', 'Tweet Text', 'Tweet URL', 'Username', 'Follower Count', 'Reply Count', 'Retweet Count',
                                              'Like Count', 'Quote Count', 'Language', 'Outlinks', 'Media', 'Retweeted Tweet', 'Quoted Tweet', 'Replier ID',
                                               'Replier Username', 'Mentioned Users', 'Coordinates', 'Place', 'Hashtags'])

tweets_df.to_csv("CSV Data\\Recent Data.csv")
tweets_df2.to_csv("CSV Data\\Old Data.csv")


f1 = open("Scraped Data\\twitter_data_1.json","w")
j = json.dumps(tweets_list, indent=4, sort_keys=True, default=str)
f1.write(j)
f1.close()

f2 = open("Scraped Data\\twitter_data_2.json","w")
j = json.dumps(tweets_list2, indent=4, sort_keys=True, default=str)
f2.write(j)
f2.close()


network_df = tweets_df[['Username','Hashtags']]
network_df = network_df.dropna()
network_df = network_df.explode('Hashtags')

network_df2 = tweets_df2[['Username','Hashtags']]
network_df2 = network_df2.dropna()
network_df2 = network_df2.explode('Hashtags')

network_df.to_csv("Network Model Testing Attributes\\Network_Data_Recent.csv")
network_df2.to_csv("Network Model Testing Attributes\\Network_Data_Old.csv")


network_graph = nx.from_pandas_edgelist(network_df, source = "Username", target = "Hashtags", create_using=nx.DiGraph())
network_graph2 = nx.from_pandas_edgelist(network_df2, source = "Username", target = "Hashtags", create_using=nx.DiGraph())

network_graph_undirected = nx.from_pandas_edgelist(network_df, source = "Username", target = "Hashtags")
network_graph2_undirected = nx.from_pandas_edgelist(network_df2, source = "Username", target = "Hashtags")

f = codecs.open("Network Model Characteristics Directed\\Network_Info_Recent.txt", "w+", "utf-8")
recent_info=nx.info(network_graph)
f.write(recent_info)
f.write("\n\nNodes:\n\n")
f.write(str(network_graph.nodes))
f.write("\n\nEdges:\n\n")
f.write(str(network_graph.edges))

f2 = codecs.open("Network Model Characteristics Directed\\Network_Info_Old.txt", "w+", "utf-8")
old_info=nx.info(network_graph2)
f2.write(old_info)
f2.write("\n\nNodes:\n\n")
f2.write(str(network_graph2.nodes))
f2.write("\n\nEdges:\n\n")
f2.write(str(network_graph2.edges))

f3 = codecs.open("Network Model Characteristics Undirected\\Network_Info_Recent.txt", "w+", "utf-8")
recent_info=nx.info(network_graph_undirected)
f3.write(recent_info)
f3.write("\n\nNodes:\n\n")
f3.write(str(network_graph_undirected.nodes))
f3.write("\n\nEdges:\n\n")
f3.write(str(network_graph_undirected.edges))

f4 = codecs.open("Network Model Characteristics Undirected\\Network_Info_Old.txt", "w+", "utf-8")
old_info=nx.info(network_graph2_undirected)
f4.write(old_info)
f4.write("\n\nNodes:\n\n")
f4.write(str(network_graph2_undirected.nodes))
f4.write("\n\nEdges:\n\n")
f4.write(str(network_graph2_undirected.edges))


net = Network(height = "750px", width = "100%", notebook=True, directed = True)

sources = network_df['Username']
targets = network_df['Hashtags']

edgelist = zip(sources, targets)

for nodelist in edgelist:
    src = nodelist[0]
    dst = nodelist[1]

    net.add_node(src, title=src, color="#FF0000")
    net.add_node(dst, title=dst, color="#00D100")
    net.add_edge(src, dst)

adjacency_list = net.get_adj_list()
f.write("\n\nAdjacency List:\n\n")
f.write(str(adjacency_list))
net.show("Network Model Graphs Directed\\Network_Graph_Recent.html")

net = Network(height = "750px", width = "100%", notebook=True, directed = True)

sources = network_df2['Username']
targets = network_df2['Hashtags']

edgelist = zip(sources, targets)

for nodelist in edgelist:
    src = nodelist[0]
    dst = nodelist[1]

    net.add_node(src, title=src, color="#FF0000")
    net.add_node(dst, title=dst, color="#00D100")
    net.add_edge(src, dst)

adjacency_list2 = net.get_adj_list()
f2.write("\n\nAdjacency List:\n\n")
f2.write(str(adjacency_list2))
net.show("Network Model Graphs Directed\\Network_Graph_Old.html")

net = Network(height = "750px", width = "100%", notebook=True, directed = False)

sources = network_df['Username']
targets = network_df['Hashtags']

edgelist = zip(sources, targets)

for nodelist in edgelist:
    src = nodelist[0]
    dst = nodelist[1]

    net.add_node(src, title=src, color="#FF0000")
    net.add_node(dst, title=dst, color="#00D100")
    net.add_edge(src, dst)

adjacency_list_undirected = net.get_adj_list()
f3.write("\n\nAdjacency List:\n\n")
f3.write(str(adjacency_list_undirected))
net.show("Network Model Graphs Undirected\\Network_Graph_Recent.html")

net = Network(height = "750px", width = "100%", notebook=True, directed = False)

sources = network_df2['Username']
targets = network_df2['Hashtags']

edgelist = zip(sources, targets)

for nodelist in edgelist:
    src = nodelist[0]
    dst = nodelist[1]

    net.add_node(src, title=src, color="#FF0000")
    net.add_node(dst, title=dst, color="#00D100")
    net.add_edge(src, dst)

adjacency_list2_undirected = net.get_adj_list()
f4.write("\n\nAdjacency List:\n\n")
f4.write(str(adjacency_list2_undirected))
net.show("Network Model Graphs Undirected\\Network_Graph_Old.html")


plt.figure(figsize=(12,12))
nx.draw_networkx(network_graph, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Recent_Data_Graph.png", format="PNG")


plt.figure(figsize=(12,12))
nx.draw_networkx(network_graph2, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Old_Data_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_networkx(network_graph_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Recent_Data_Graph.png", format="PNG")


plt.figure(figsize=(12,12))
nx.draw_networkx(network_graph2_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Old_Data_Graph.png", format="PNG")


plt.figure(figsize=(12,12))
nx.draw_circular(network_graph, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Recent_Data_Circular_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_circular(network_graph2, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Old_Data_Circular_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_circular(network_graph_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Recent_Data_Circular_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_circular(network_graph2_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Old_Data_Circular_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_kamada_kawai(network_graph, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Recent_Data_KamadaKawai_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_kamada_kawai(network_graph2, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Old_Data_KamadaKawai_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_kamada_kawai(network_graph_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Recent_Data_KamadaKawai_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_kamada_kawai(network_graph2_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Old_Data_KamadaKawai_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_spring(network_graph, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Recent_Data_Spring_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_spring(network_graph2, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Old_Data_Spring_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_spring(network_graph_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Recent_Data_Spring_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_spring(network_graph2_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Old_Data_Spring_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_random(network_graph, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Recent_Data_Random_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_random(network_graph2, with_labels=True)
plt.savefig("Network Model Graphs Directed\\Old_Data_Random_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_random(network_graph_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Recent_Data_Random_Graph.png", format="PNG")

plt.figure(figsize=(12,12))
nx.draw_random(network_graph2_undirected, with_labels=True)
plt.savefig("Network Model Graphs Undirected\\Old_Data_Random_Graph.png", format="PNG")

network_graph_degree=sorted(network_graph.degree, key=lambda x: x[1], reverse=True)
f.write("\n\nRecent Data Model Degree:\n\n")
f.write(str(network_graph_degree))

network_graph2_degree=sorted(network_graph2.degree, key=lambda x: x[1], reverse=True)
f2.write("\n\nOld Data Model Degree:\n\n")
f2.write(str(network_graph2_degree))

network_graph_undirected_degree=sorted(network_graph_undirected.degree, key=lambda x: x[1], reverse=True)
f3.write("\n\nRecent Data Model Degree:\n\n")
f3.write(str(network_graph_degree))

network_graph2_undirected_degree=sorted(network_graph2_undirected.degree, key=lambda x: x[1], reverse=True)
f4.write("\n\nOld Data Model Degree:\n\n")
f4.write(str(network_graph2_degree))

degree_name, degree_count = zip(*network_graph_degree)
plt.figure(figsize=(40, 15))
plt.bar(degree_name[0:20], degree_count[0:20])
plt.savefig("Network Model Graphs Directed\\Recent_Data_Degree_Histogram.png", format="PNG")

degree_name, degree_count = zip(*network_graph2_degree)
plt.figure(figsize=(40, 15))
plt.bar(degree_name[0:20], degree_count[0:20])
plt.savefig("Network Model Graphs Directed\\Old_Data_Degree_Histogram.png", format="PNG")

degree_name, degree_count = zip(*network_graph_undirected_degree)
plt.figure(figsize=(40, 15))
plt.bar(degree_name[0:20], degree_count[0:20])
plt.savefig("Network Model Graphs Undirected\\Recent_Data_Degree_Histogram.png", format="PNG")

degree_name, degree_count = zip(*network_graph2_undirected_degree)
plt.figure(figsize=(40, 15))
plt.bar(degree_name[0:20], degree_count[0:20])
plt.savefig("Network Model Graphs Undirected\\Old_Data_Degree_Histogram.png", format="PNG")

pageranks = nx.pagerank(network_graph)
pageranks = {key: value for key, value in sorted(pageranks.items(), key=lambda item: item[1], reverse = True)}
pagerank_name = list(pageranks.keys())
pagerank_value = list(pageranks.values())
(pagerank_name,pagerank_value) = zip(*pageranks.items())
f.write("\n\nRecent Data Model PageRanks:\n\n")
f.write(str(pageranks))
plt.figure(figsize=(40, 15))
plt.bar(pagerank_name[0:20],pagerank_value[0:20])
plt.savefig("Network Model Graphs Directed\\Recent_Data_Pagerank_Histogram.png", format="PNG")

pageranks = nx.pagerank(network_graph2) 
pageranks = {key: value for key, value in sorted(pageranks.items(), key=lambda item: item[1], reverse = True)}
pagerank_name = list(pageranks.keys())
pagerank_value = list(pageranks.values())
(pagerank_name,pagerank_value) = zip(*pageranks.items())
f2.write("\n\nOld Data Model PageRanks:\n\n")
f2.write(str(pageranks))
plt.figure(figsize=(40, 15))
plt.bar(pagerank_name[0:20],pagerank_value[0:20])
plt.savefig("Network Model Graphs Directed\\Old_Data_Pagerank_Histogram.png", format="PNG")


pageranks = nx.pagerank(network_graph_undirected) 
pageranks = {key: value for key, value in sorted(pageranks.items(), key=lambda item: item[1], reverse = True)}
pagerank_name = list(pageranks.keys())
pagerank_value = list(pageranks.values())
f3.write("\n\nRecent Data Model PageRanks:\n\n")
f3.write(str(pageranks))
plt.figure(figsize=(40, 15))
plt.bar(pagerank_name[0:20],pagerank_value[0:20])
plt.savefig("Network Model Graphs Undirected\\Recent_Data_Pagerank_Histogram.png", format="PNG")

pageranks = nx.pagerank(network_graph2_undirected)
pageranks = {key: value for key, value in sorted(pageranks.items(), key=lambda item: item[1], reverse = True)}
pagerank_name = list(pageranks.keys())
pagerank_value = list(pageranks.values())
f4.write("\n\nOld Data Model PageRanks:\n\n")
f4.write(str(pageranks))
plt.figure(figsize=(40, 15))
plt.bar(pagerank_name[0:20],pagerank_value[0:20])
plt.savefig("Network Model Graphs Undirected\\Old_Data_Pagerank_Histogram.png", format="PNG")

cc=nx.clustering(network_graph)
f.write("\n\nRecent Data Model Clustering Coefficients:\n\n")
f.write(str(cc))

cc=nx.clustering(network_graph2)
f2.write("\n\nOld Data Model Clustering Coefficients:\n\n")
f2.write(str(cc))

cc=nx.clustering(network_graph_undirected)
f3.write("\n\nRecent Data Model Clustering Coefficients:\n\n")
f3.write(str(cc))

cc=nx.clustering(network_graph2_undirected)
f4.write("\n\nOld Data Model Clusterinf Coefficients:\n\n")
f4.write(str(cc))

dc=nx.degree_centrality(network_graph)
f.write("\n\nRecent Data Model Degree Centrality:\n\n")
f.write(str(dc))

dc=nx.degree_centrality(network_graph2)
f2.write("\n\nOld Data Model Degree Centrality:\n\n")
f2.write(str(dc))

dc=nx.degree_centrality(network_graph_undirected)
f3.write("\n\nRecent Data Model Degree Centrality:\n\n")
f3.write(str(dc))

dc=nx.degree_centrality(network_graph2_undirected)
f4.write("\n\nOld Data Model Degree Centrality:\n\n")
f4.write(str(dc))

idc=nx.in_degree_centrality(network_graph)
f.write("\n\nRecent Data Model In-Degree Centrality:\n\n")
f.write(str(idc))

idc=nx.in_degree_centrality(network_graph2)
f2.write("\n\nOld Data Model In-Degree Centrality:\n\n")
f2.write(str(idc))

evc=nx.eigenvector_centrality(network_graph)
f.write("\n\nRecent Data Model Eigenvector Centrality:\n\n")
f.write(str(evc))

evc=nx.eigenvector_centrality(network_graph2)
f2.write("\n\nOld Data Model Eigenvector Centrality:\n\n")
f2.write(str(evc))

evc=nx.eigenvector_centrality(network_graph_undirected)
f3.write("\n\nRecent Data Model Eigenvector Centrality:\n\n")
f3.write(str(evc))

evc=nx.eigenvector_centrality(network_graph2_undirected)
f4.write("\n\nOld Data Model Eigenvector Centrality:\n\n")
f4.write(str(evc))

kc=nx.katz_centrality(network_graph)
f.write("\n\nRecent Data Model Katz Centrality:\n\n")
f.write(str(kc))

kc=nx.katz_centrality(network_graph2)
f2.write("\n\nOld Data Model Katz Centrality:\n\n")
f2.write(str(kc))

bc=nx.betweenness_centrality(network_graph)
f.write("\n\nRecent Data Model (Shortest Paths) Betweenness Centrality:\n\n")
f.write(str(bc))

bc=nx.betweenness_centrality(network_graph2)
f2.write("\n\nOld Data Model (Shortest Paths) Betweenness Centrality:\n\n")
f2.write(str(kc))

bc=nx.betweenness_centrality(network_graph_undirected)
f3.write("\n\nRecent Data Model (Shortest Paths) Betweenness Centrality:\n\n")
f3.write(str(bc))

bc=nx.betweenness_centrality(network_graph2_undirected)
f4.write("\n\nOld Data Model (Shortest Paths) Betweenness Centrality:\n\n")
f4.write(str(kc))


f.close()
f2.close()
f3.close()
f4.close()