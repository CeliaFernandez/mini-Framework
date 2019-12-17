import ROOT as r
from ROOT import gROOT

from interface.Distribution import Distribution
from interface.Recipe import Recipe
from interface.Canvas import Canvas

import os, optparse


################################################################################
#### ---------------------------------------------------------------------- ####
#### -------------------------- GLOBAL VARIABLES -------------------------- ####               
#### ---------------------------------------------------------------------- ####
################################################################################

WORKPATH = os.path.abspath('./') + '/'



###############################################################################
#### --------------------------------------------------------------------- ####
#### ----------------------------- FUNCTIONS ----------------------------- ####                        
#### --------------------------------------------------------------------- ####
###############################################################################

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

      
    ymin = 0.9 - len(hlist)*0.04
    plot = Canvas(name, 'png', 0.5, ymin, 0.9, 0.9, 1)

    for i,_h in enumerate(hlist):

        if ylog:_h.SetMaximum(10.0*ymax)
        else:_h.SetMaximum(1.3*ymax)

        if i == 0: 
            _h.GetXaxis().SetTitle(xlabel)
            _h.GetYaxis().SetTitle("Events / "+ str((xmax-xmin)/nbin))
            plot.addHisto(_h, 'HIST', listOfElements[i].getLabel(), 'l', _h.GetLineColor(), 1, i)
        else: plot.addHisto(_h, 'HIST, SAME', listOfElements[i].getLabel(), 'l', _h.GetLineColor(), 1, i)
   

    plot.save(1, 0, ylog, '', '', outputDir = 'plots/')




###############################################################################
#### --------------------------------------------------------------------- ####
#### ----------------------------- MAIN CODE ----------------------------- ####               
#### --------------------------------------------------------------------- ####
###############################################################################


if __name__=="__main__":


    #######################
    ###  Parser object  ###
    #######################

    parser = optparse.OptionParser(usage='usage: %prog [opts] FilenameWithSamples', version='%prog 1.0')
    parser.add_option('-c', '--config', action='store', type=str, dest='config', default='config.py', help='Python file with main() function definition. Default: \'config.py\'')
    (opts, args) = parser.parse_args()

    #######################
    ###  Set TDR style  ###
    #######################

    gROOT.ProcessLine('.L ' + WORKPATH + 'include/tdrstyle.C')
    gROOT.SetBatch(1)
    r.setTDRStyle()


    ###################################
    ###  Config load and execution  ###
    ###################################

    handle = open(opts.config, 'r')
    exec(handle)
    handle.close()


    for plot in histogramRecipes.keys():

        recipe = histogramRecipes[plot]
        distributions, xlabel, bins, isLog = recipe.getAttributes()
        makePlot(plot, distributions, bins[0], bins[1], bins[2], xlabel, ylog = isLog, normed = True)

 
