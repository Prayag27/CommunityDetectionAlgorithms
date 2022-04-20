import LouvainCommunityDetection
import CliquePercolation
import GN
import GraphGenerator
import networkx as nx
import time
import matplotlib.pyplot as plt

if __name__ == "__main__":
    G1 = GraphGenerator.gnp_random_connected_graph(10, .5)
    G2 = GraphGenerator.gnp_random_connected_graph(15,.5)
    G3 = GraphGenerator.gnp_random_connected_graph(20,.5)
    G4 = GraphGenerator.gnp_random_connected_graph(30,.5)
    nx.draw(G1, with_labels = True)
    plt.savefig("Graph1.png")

    nx.draw(G2, with_labels = True)
    plt.savefig("Graph2.png")

    nx.draw(G3, with_labels = True)
    plt.savefig("Graph3.png")

    nx.draw(G4, with_labels = True)
    plt.savefig("Graph4.png")
    # G = nx.karate_club_graph()

    start_time1 = time.time()
    LouvainCommunity1 = LouvainCommunityDetection.louvain_communities(G1)
    print("--- %.15f execution time in seconds ---" % (time.time() - start_time1))
    print(LouvainCommunity1)

    start_time11 = time.time()
    CliquePercolationCommunity1 = list(CliquePercolation.k_clique_communities(G1, 2))
    print("--- %.15f execution time in seconds ---" %(time.time() - start_time11))
    print(CliquePercolationCommunity1)

    start_time111 = time.time()
    GNCommunity1 = list(GN.girvan_newman(G1))
    print("--- %.15f execution time in seconds ---" %(time.time() - start_time111))
    print(GNCommunity1)

    print("================================Test-1 Over =====================================")


    start_time2 = time.time()
    LouvainCommunity2 = LouvainCommunityDetection.louvain_communities(G2)
    print("--- %.15f execution time in seconds ---" % (time.time() - start_time2))
    print(LouvainCommunity2)

    start_time22 = time.time()
    CliquePercolationCommunity2 = list(CliquePercolation.k_clique_communities(G2, 5))
    print("--- %.15f execution time in seconds ---"  %(time.time() - start_time22))
    print(CliquePercolationCommunity2)

    start_time222 = time.time()
    GNCommunity2 = list(GN.girvan_newman(G2))
    print("--- %.15f execution time in seconds ---" %(time.time() - start_time222))
    print(GNCommunity2)

    print("================================Test-2 Over =====================================")


    start_time3 = time.time()
    LouvainCommunity3 = LouvainCommunityDetection.louvain_communities(G3)
    print("--- %.15f execution time in seconds ---" % (time.time() - start_time3))
    print(LouvainCommunity3)

    start_time33 = time.time()
    CliquePercolationCommunity3 = list(CliquePercolation.k_clique_communities(G3, 6))
    print("--- %.15f execution time in seconds ---" %(time.time() - start_time33))
    print(CliquePercolationCommunity3)

    start_time333 = time.time()
    GNCommunity3 = list(GN.girvan_newman(G3))
    print("--- %.15f execution time in seconds ---" %(time.time() - start_time333))
    print(GNCommunity3)

    print("================================Test-3 Over =====================================")


    start_time4 = time.time()
    LouvainCommunity4 = LouvainCommunityDetection.louvain_communities(G4)
    print("--- %.15f execution time in seconds ---" % (time.time() - start_time4))
    print(LouvainCommunity4)

    start_time44 = time.time()
    CliquePercolationCommunity4 = list(CliquePercolation.k_clique_communities(G4, 6))
    print("--- %.15f execution time in seconds ---" %(time.time() - start_time44))
    print(CliquePercolationCommunity4)

    start_time444 = time.time()
    GNCommunity4 = list(GN.girvan_newman(G4))
    print("--- %.15f execution time in seconds ---" %(time.time() - start_time444))
    print(GNCommunity4)
    print("================================Test-4 Over =====================================")
    #TODO: Color Community Nodes