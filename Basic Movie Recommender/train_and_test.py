import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# getting the data
data = fetch_movielens(min_rating = 3.0)

# training model
model = LightFM(loss='warp')
model.fit(data['train'])

#testing model
total_users, total_features = data['train'].shape
ids = [500, 60, 101]
for id in ids:
	# movie already liked by user
	known_positives = data['item_labels'][data['train'].tocsr()[id].indices]
	prediction = model.predict(id, np.arange(total_features))

	#ranking them
	top_items = data['item_labels'][np.argsort(-prediction)]

	#print out the results
	print "User"+ str(id)
	print "     Known positives:"
	for x in known_positives[:3]:
		print "        %s" % x 

	print "     Recommended:"
	for x in top_items[:3]:
		print("        %s" % x)	