'''
Implementation of CART algorithm of Decision Tree
'''

class DecisionTreeClassifier:
    def __init__(self, max_tree_depth = float('inf'), min_leaf_node_sz = -float('inf') ):
        self.max_tree_depth = max_tree_depth
        self.min_leaf_node_sz = min_leaf_node_sz
        
    # Helper function - to know the net gini index of a split
    # Returns GINI Index for a particular split - Weighted average of left and right group
    def gini_index(self, groups):
        gini = 0
        total_len = sum( [len(group) for group in groups] )
        for group in groups:
            population_sz = len(group)*1.0
            labels = [item[-1] for item in group]
            temp = [(labels.count(item)/population_sz)**2 for item in list(set(labels))]
            sub_gini = 1-sum(temp)
            gini += sub_gini*( len(group)*1.0/total_len ) 
        
        return gini
    
    # Helper function
    # Divides input dataset into 2 parts based on input threshold
    def test_split(self, dataset, index, threshold):
        left, right = [], []
        for row in dataset: 
            if row[0][index]<=threshold:
                left.append(row)
            else:
                right.append(row)
        return (left,right)        
    
    # Helper Function
    # Returns the most common/frequent class in the input 'group'
    def to_terminal(self, group):
        labels = [row[1] for row in group]
        return max(labels, key=labels.count)
    
    # Helper Function
    # Checks if a node is terminal node based on certain criterians
    def is_terminal(self, node, left, right, depth):
        # Criterion 1:
        if node['Gini']==0:
            node['left'] = self.to_terminal(left)
            node['right'] = self.to_terminal(right) 
            return True
        
        # Criterion 2:
        if not left or not right:
            node['left'] = node['right'] = self.to_terminal(left+right)
            return True
            
        # Criterion 3:
        if len(left)<=self.min_leaf_node_sz:
            node['left'] = self.to_terminal(left)
        if len(right)<=self.min_leaf_node_sz:
            node['right'] = self.to_terminal(right)
            return True
        
        # Criterion 4:
        if depth>=self.max_tree_depth:
            node['left'] = node['right'] = self.to_terminal(right+left)
            return True
        
        return False
    
    # Helper function
    # Recursivly calls get_best_split() untill the node is found to be terminal
    def split_it_recursive(self, split_node, depth):
        left, right = split_node['Groups']
        del split_node['Groups']           # since not useful during prediction + high space occupant 
        
        if self.is_terminal(split_node, left, right, depth):
            return 

        split_node['left'] = self.get_best_split(left)
        self.split_it_recursive(split_node['left'],depth+1)
        split_node['right'] = self.get_best_split(right)
        self.split_it_recursive(split_node['right'],depth+1)
    
    # Helper function 
    # Returns best split possible for dataset in argument
    def get_best_split(self, dataset):        
        best_index, best_threshold, best_gini = None, None, 1  
        for feature_index in range(len(dataset[0][0])):
            for row in dataset:
                groups = self.test_split(dataset, feature_index, row[0][feature_index] )
                gini = self.gini_index(groups)
                if gini<best_gini:
                    best_index, best_threshold, best_gini, best_groups =  feature_index, row[0][feature_index], gini, groups
        return {'Index':best_index, 'Threshold':best_threshold, 'Groups': best_groups, 'Gini':best_gini}
    
    # Main Function
    # Returns the root element of the Decision Tree formed after training
    def fit(self, x_train, ytrain):
        self.x_train = x_train 
        self.y_train = y_train
        self.dataset = zip(x_train, y_train)
        
        self.root = self.get_best_split(self.dataset)
        self.split_it_recursive(self.root, depth=1)
        
        return self.root
        
    # Helper Function
    # Returns y_pred for input x_test (row)
    def prediction(self, node, x_test_row):
        if type(node)==int:        #i.e if leaf node
            return node
        index = node['Index']
        threshold = node['Threshold']
        if x_test_row[index]<=threshold:
            return self.prediction(node['left'], x_test_row)
        else:
            return self.prediction(node['right'], x_test_row)

    # Main Function
    # Returns y_pred for input x_test (list)
    def predict(self, x_test):
        return [self.prediction(self.root, row) for row in x_test]

x_train = [[3],
           [5],
           [4],
           [1],
           [7],

           [45],
           [33],
           [100],
           [26],
           [70] ]        #Though this is simple dataset(for demo), but the model works as fine for complex dataset 

y_train = [0,0,0,0,0,1,1,1,1,1]
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)


x_test = [[6],
          [120],
          [35]]
print 'y_pred:',clf.predict(x_test)
'''
Output= y_pred: [0, 1, 1]
'''
