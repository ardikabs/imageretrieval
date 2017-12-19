
from lib.pyimagesearch.colordescriptor import ColorDescriptor
from lib.pyimagesearch.searcher import Searcher
import cv2
import json
import os
import numpy as np
import urllib


class SearchEngine:
    def __init__(self,sourcePath):
        self.cd = ColorDescriptor((8,12,3))
        self.sourcePath = sourcePath
    

    def searchQuery(self,query):
        img = cv2.imread(query)
        features = self.cd.describe(img)
        searcher = Searcher(self.sourcePath)
        results = searcher.search(features)

        return results