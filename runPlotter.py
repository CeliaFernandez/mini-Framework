import ROOT as r
from ROOT import gROOT

from interface.Element import Element
from interface.Canvas import Canvas

import os


WORKPATH = os.path.abspath('./') + '/'


def makePlot(name, listOfElements, nbin, xmin, xmax, xlabel, ylog = False, normed = False, overflow = True):

    hlist = []
    ymax = 0.0

    for element in listOfElements:
        _h = element.getTH1F(nbin, xmin, xmax, overflow)
        if normed: _h.Scale(1.0/_h.Integral())
        _h.SetLineWidth(2)
        _h.SetLineColor(element.getColor())
        hlist.append(_h)
        if _h.GetMaximum() > ymax: ymax = _h.GetMaximum()

       
    plot = Canvas('hist_'+name, 'png', 0.6, 0.6, 0.9, 0.9, 1)

    for i,_h in enumerate(hlist):

        if ylog:_h.SetMaximum(10.0*ymax)
        else:_h.SetMaximum(1.3*ymax)

        if i == 0: 
            _h.GetXaxis().SetTitle(xlabel)
            _h.GetYaxis().SetTitle("Events / "+ str((xmax-xmin)/nbin))
            plot.addHisto(_h, 'HIST', listOfElements[i].getLabel(), 'l', _h.GetLineColor(), 1, i)
        else: plot.addHisto(_h, 'HIST, SAME', listOfElements[i].getLabel(), 'l', _h.GetLineColor(), 1, i)
   

    plot.save(1, 0, ylog, '', '', outputDir = 'plots/')




if __name__=="__main__":

    gROOT.ProcessLine('.L ' + WORKPATH + 'include/tdrstyle.C')
    gROOT.SetBatch(1)
    r.setTDRStyle()

    file1 = "/afs/cern.ch/work/f/fernance/private/Long_Lived_Analysis/CMSSW_9_4_4/src/MyAnalysis/IFCALongLivedAnalysis/output.root"

    sample1 = []
    sample1.append(Element(file1, "Events", "EEBase_trackIxy", r.kAzure, "output"))

    makePlot("prueba", sample1, 40, 0.0, 20.0, "dxy (cm)", normed = True)

 
