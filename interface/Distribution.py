import ROOT as r
from ROOT import TFile, TH1F
import copy

class Distribution:

    def __init__(self, fpath, tname, varexp, color, label, cut = ""):

        self.fpath = fpath
        self.tname = tname
        self.varexp = varexp
        self.color = color
        self.label = label
        self.cut = cut


    def getTH1F(self, nbin, xmin, xmax, overflow = True):

        _f = TFile(self.fpath)
        _t = _f.Get(self.tname)
        bw = (xmax - xmin)/nbin

        if overflow:
            _h = TH1F("aux_h", "", nbin + 1, xmin, xmax + bw)
        else:
            _h = TH1F("aux_h", "", nbin, xmin, xmax)

        _h.Sumw2()
        _t.Project(_h.GetName(), self.varexp, self.cut, "")

        if overflow:
            _h.SetBinContent(_h.GetNbinsX(), _h.GetBinContent(_h.GetNbinsX()) + _h.GetBinContent(_h.GetNbinsX() + 1))

        return copy.deepcopy(_h)


    def getColor(self):

        return self.color

    def getLabel(self):

        return self.label
