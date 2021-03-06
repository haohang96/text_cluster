import pdb
import numpy as np
from sklearn.cluster import AgglomerativeClustering


def embed_sentence(sentence_list):
    pass



def clus_data(data, n_clusters, affinity, linkage, dis_thre):
    model = AgglomerativeClustering(n_clusters=n_clusters, affinity=affinity, linkage=linkage, distance_threshold=dis_thre)
    clus_res = model.fit(data)

    return clus_res

if __name__ == "__main__":
    data = np.random.randn(100, 128)
    clus_res = clus_data(data, n_clusters=None, affinity='euclidean', linkage='ward', dis_thre=0.6)
    pdb.set_trace()
