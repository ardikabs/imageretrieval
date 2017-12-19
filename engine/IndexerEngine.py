
from lib.pyimagesearch.colordescriptor import ColorDescriptor
import os
import glob
import json
import cv2
import numpy as np

# PATH_DATASET = "static/dataset/"
# PATH_RESULT = 'static/result/'
# cd = ColorDescriptor((8,12,3))
# result = {}
# output = open(PATH_RESULT+'training.json','w')

# for image in os.listdir(PATH_DATASET):

#     imgId = image[0:image.rfind('.')]
#     img = cv2.imread(PATH_DATASET + image)

#     features = cd.describe(img)
#     features = [f for f in features]

#     result[imgId]=[]
#     result[imgId].append({
#         "region_1":features[0].tolist(),
#         "region_2":features[1].tolist(),
#         "region_3":features[2].tolist(),
#         "region_4":features[3].tolist()
#     })

# output.write(json.dumps(result))
# output.close()

class IndexerEngine:
    def __init__(self,datasetPath,resultPath):
        self.cd = ColorDescriptor
        self.datasetPath = datasetPath # datasetpath should be look like this path/to/static/dataset/*.png
        self.resultPath = resultPath
        
    
    def indexer(self):
        result = {}
        output = open(self.resultPath,'w') # resultpath should be look like this path/to/static/result/training.json
        for image in os.listdir(self.datasetPath):
            imgId = image[0:image.rfind('.')]
            img = cv2.imread(self.datasetPath + image)

            features = cd.describe(img)
            features = [f for f in features]

            result[imgId]=[]
            result[imgId].append({
                "region_1":features[0].tolist(),
                "region_2":features[1].tolist(),
                "region_3":features[2].tolist(),
                "region_4":features[3].tolist()
            })
        output.write(json.dumps(result))
        output.close()

        return json.dumps(result)
