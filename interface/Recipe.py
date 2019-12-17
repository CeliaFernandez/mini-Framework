import ROOT as r
from Distribution import Distribution

class Recipe:

    def __init__(self, xlabel, bins):

        self.distributions = []
        self.xlabel = xlabel
        self.bins = bins
        self.log = False

    def addDistribution(self, dist):

        self.distributions.append(dist)

    def setLog(self, log):

        self.log = log

    def getAttributes(self):

        return self.distributions, self.xlabel, self.bins, self.log
