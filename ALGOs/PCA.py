
class PCA:
    def __init__(self, features_raw, n_components=None, feature_rescale=False):
        self.n_components = n_components
        self.features_raw = features_raw
        self.feature_rescale = feature_rescale


    def transpose(self, matrix):
        return zip(*matrix)

    
    # Min,Max feature normalisation
    def scale_features(self, features_raw):
        features_raw_tranpose = self.transpose(features_raw)
        
        ans = []
        for all_feature_a_values in features_raw_tranpose:
            mini = min(all_feature_a_values)*1.0
            maxi = max(all_feature_a_values)*1.0

            all_feature_a_values_scaled = [(value-mini)/(maxi-mini) for value in all_feature_a_values]
            ans.append(all_feature_a_values_scaled)

        return self.transpose(ans)


    # Mean,std-dev normalisation 
    def scale_features_2(self, feature_raw):
        features_raw_tranpose = self.transpose(self.features_raw)
        
        ans = []
        for all_feature_a_values in features_raw_tranpose:
            mean = self.mean(all_feature_a_values)*1.0
            std  = self.std(all_feature_a_values)*1.0

            all_feature_a_values_scaled = [(value-mean)/std for value in all_feature_a_values]
            ans.append(all_feature_a_values_scaled)

        return self.transpose(ans)

    
    # Returns mean of input vector    
    def std(self, vec):
        import math
        mean = self.mean(vec)
        return math.sqrt( sum((x - mean)**2 for x in vec) / len(vec) )

        
    # Returns mean of input vector    
    def mean(self, vec):
        return sum(vec)*1.0/len(vec)


    # Returns covariance matrix for the 2 input vectors
    def get_convariance(self, x1, x2):
        n = len(x1)
        x1_mean = self.mean(x1)
        x2_mean = self.mean(x2)
        ans = 0.0
        for i in range(len(x1)):
            ans += (x1[i]-x1_mean)*(x2[i]-x2_mean)

        return ans/(n-1) 


    # Returns covariance matrix for the raw feature vectors
    def get_convariance_matrix(self, features_scaled):
        n_features = len(features_scaled[0])

        ans = [[0]*n_features]*n_features
        features_scaled_tranpose = self.transpose(features_scaled)
        for i in range(n_features):
            for j in range(i+1):
                ans[i][j] = self.get_convariance(features_scaled_tranpose[i], features_scaled_tranpose[j])        
        return ans


    # Returns eigenvalue,eigenvectors for the input matrix    
    def get_eigenvectors_vs_eigenvalues(self, matrix):
        import numpy as np   # Didnt wanted to use a library but here its unavoidable 
        eig_val_np,eig_vec_np = np.linalg.eig(matrix)
        eig_vec_np = eig_vec_np.T
        eig_vals = [float(val) for val in eig_val_np]
        eig_vecs = [list(x) for x in eig_vec_np]
        
        ans = zip( eig_vecs,eig_vals ) 
        ans.sort(key = lambda a: a[1], reverse = True ) # sort by eigenvalues
        
        return ans


    # Selects and returns top eigenvecs,eigenvals from all eigenvecs,eigenvals
    def select_best(self, eigenvectors_vs_eigenvalues):
        if self.n_components:
            return eigenvectors_vs_eigenvalues[:self.n_components]

        # Criterion: Top Eigenvalues-Eigenvector that Captures 85% of total variance
        variance_captured = 0
        ans = []
        eigenvalues_sum = sum([x[1] for x in eigenvectors_vs_eigenvalues])*1.0

        step = 0
        while(variance_captured<0.85):
            eig_pair = eigenvectors_vs_eigenvalues[step]
            variance_captured += eig_pair[1]/eigenvalues_sum
            step += 1

        return eigenvectors_vs_eigenvalues[:step]


    def mul(self, a, b):
        return sum(ai*bi for ai,bi in zip(a,b))
        
    # Returns feature_new = feature_old * eigenvectors
    def transform_features(self, features_scaled, eigenvectors_vs_eigenvalues):
        ans = []
        for features_observation_1 in features_scaled:
            transformed_feature_observation_1 = [self.mul(features_observation_1, eigenvector) for eigenvector,eigenvalue in eigenvectors_vs_eigenvalues] #element-wise multiplication
            ans.append(transformed_feature_observation_1)

        return ans
    
    # Main function
    def transform(self):
        if self.feature_rescale:
            features_scaled = self.scale_features(self.features_raw) #Note: sklearn.decomposition.PCA.fit_transform() donot do feature re-scaling
        else:
            features_scaled = self.features_raw

        cov = self.get_convariance_matrix(features_scaled)

        eigenvectors_vs_eigenvalues = self.get_eigenvectors_vs_eigenvalues(cov)

        eigenvectors_vs_eigenvalues = self.select_best(eigenvectors_vs_eigenvalues)

        features_transformed = self.transform_features(features_scaled, eigenvectors_vs_eigenvalues)

        return features_transformed


X_raw = [[1, 2],
         [3, 4],
         [5, 6]
         ]
X_transformed = PCA(X_raw, n_components=2).transform()

print X_transformed
'''
Output: [[2.1213203435596424, 0.7071067811865475],
        [4.949747468305832, 0.7071067811865475],
        [7.778174593052022, 0.7071067811865475]]
'''


