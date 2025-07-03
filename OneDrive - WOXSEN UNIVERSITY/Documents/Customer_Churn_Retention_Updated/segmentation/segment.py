from sklearn.cluster import KMeans

def segment_customers(data, n_segments=4):
    kmeans = KMeans(n_clusters=n_segments)
    data['Segment'] = kmeans.fit_predict(data[['Tenure', 'MonthlySpend']])
    return data
