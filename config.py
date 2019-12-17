from interface.Recipe import Recipe
from interface.Distribution import Distribution

##############################
###  Variable declaration  ###
##############################

newRPV = "/gpfs/projects/cms/fernance/DisplacedSUSY_squarkToQuarkChi_MSquark_350_MChi_148_ctau_173mm_TuneCP2_13TeV_80X_19062019-1840/crab_RPV_350-148-173_newTuples/191210_153708/RPV_350-148-173.root"
oldRPV = "/gpfs/projects/cms/fernance/DisplacedSUSY_squarkToQuarkChi_MSquark_350_MChi_148_ctau_173mm_TuneCP2_13TeV_80X_19062019-1840/crab_350-148-173_DisplacedSUSY_NTuple_new/190909_135954/350-148-173_RPV.root"
DY = "/gpfs/projects/cms/fernance/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_newNTuples/191210_153536/DY.root"


###########################
###  Histogram recipes  ###
###########################

histogramRecipes = {}

histogramRecipes["nEEBase"] = Recipe("Number of EE Candidates", [3, 0.0, 3.0])
histogramRecipes["nEEBase"].distributions.append(Distribution(DY, "Events", "nEEBase", r.kRed-7, "DYJetsToLL (M-50)"))
histogramRecipes["nEEBase"].distributions.append(Distribution(newRPV, "Events", "nEEBase", r.kBlue-7, "RPV(350,148,17.3)"))
histogramRecipes["nEEBase"].setLog(True)

histogramRecipes["nMMBase"] = Recipe("Number of MM candidates", [3, 0.0, 3.0])
histogramRecipes["nMMBase"].distributions.append(Distribution(DY, "Events", "nMMBase", r.kRed-7, "DYJetsToLL (M-50)"))
histogramRecipes["nMMBase"].distributions.append(Distribution(newRPV, "Events", "nMMBase", r.kBlue-7, "RPV(350,148,17.3)"))
histogramRecipes["nMMBase"].setLog(True)

histogramRecipes["EEtrackIdx_comparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["EEtrackIdx_comparison"].distributions.append(Distribution(newRPV, "Events", "abs(EEBase_trackIxy)", r.kBlue-7, "RPV(350,148,17.3)"))
histogramRecipes["EEtrackIdx_comparison"].distributions.append(Distribution(DY, "Events", "abs(EEBase_trackIxy)", r.kRed-7, "DYJetsToLL (M-50)"))
histogramRecipes["EEtrackIdx_comparison"].setLog(True)

histogramRecipes["EEtrackDxy_comparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 5.0])
histogramRecipes["EEtrackDxy_comparison"].distributions.append(Distribution(newRPV, "Events", "abs(EEBase_trackDxy)", r.kBlue-7, "RPV(350,148,17.3)"))
histogramRecipes["EEtrackDxy_comparison"].distributions.append(Distribution(DY, "Events", "abs(EEBase_trackDxy)", r.kRed-7, "DYJetsToLL (M-50)"))
histogramRecipes["EEtrackDxy_comparison"].setLog(True)

histogramRecipes["MMtrackIdx_comparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["MMtrackIdx_comparison"].distributions.append(Distribution(newRPV, "Events", "abs(MMBase_trackIxy)", r.kBlue-7, "RPV(350,148,17.3)"))
histogramRecipes["MMtrackIdx_comparison"].distributions.append(Distribution(DY, "Events", "abs(MMBase_trackIxy)", r.kRed-7, "DYJetsToLL (M-50)"))
histogramRecipes["MMtrackIdx_comparison"].setLog(True)

histogramRecipes["MMtrackDxy_comparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 5.0])
histogramRecipes["MMtrackDxy_comparison"].distributions.append(Distribution(newRPV, "Events", "abs(MMBase_trackDxy)", r.kBlue-7, "RPV(350,148,17.3)"))
histogramRecipes["MMtrackDxy_comparison"].distributions.append(Distribution(DY, "Events", "abs(MMBase_trackDxy)", r.kRed-7, "DYJetsToLL (M-50)"))
histogramRecipes["MMtrackDxy_comparison"].setLog(True)

histogramRecipes["ExcludedTracks"] = Recipe("Excluded tracks from PV refitting", [5, 0.0, 5.0])
histogramRecipes["ExcludedTracks"].distributions.append(Distribution(DY, "Events", "RefittedPV_nExcludedTrack", r.kRed-7, "DYJetsToLL (M-50)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["ExcludedTracks"].distributions.append(Distribution(newRPV, "Events", "RefittedPV_nExcludedTrack", r.kBlue-7, "RPV(350,148,17.3)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["ExcludedTracks"].setLog(True)

histogramRecipes["PV_dX"] = Recipe("Refitted PV x - Original PV x", [40, -5.0, 5.0])
histogramRecipes["PV_dX"].distributions.append(Distribution(DY, "Events", "RefittedPV_vx - PV_vx", r.kRed-7, "DYJetsToLL (M-50)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["PV_dX"].distributions.append(Distribution(newRPV, "Events", "RefittedPV_vx - PV_vx", r.kBlue-7, "RPV(350,148,17.3)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["PV_dX"].setLog(True)

histogramRecipes["PV_dY"] = Recipe("Refitted PV y - Original PV y", [40, -5.0, 5.0])
histogramRecipes["PV_dY"].distributions.append(Distribution(DY, "Events", "RefittedPV_vy - PV_vy", r.kRed-7, "DYJetsToLL (M-50)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["PV_dY"].distributions.append(Distribution(newRPV, "Events", "RefittedPV_vy - PV_vy", r.kBlue-7, "RPV(350,148,17.3)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["PV_dY"].setLog(True)


### RPV refitting studies:
histogramRecipes["RPVReffiting_EEcomparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["RPVReffiting_EEcomparison"].distributions.append(Distribution(newRPV, "Events", "abs(EEBase_trackIxy)", r.kBlue-7, "Original I_{xy}", cut = "EEBase_refittedIxy != -99"))
histogramRecipes["RPVReffiting_EEcomparison"].distributions.append(Distribution(newRPV, "Events", "abs(EEBase_refittedIxy)", r.kRed-7, "Refitted I_{xy}", cut = "EEBase_refittedIxy != -99"))
histogramRecipes["RPVReffiting_EEcomparison"].setLog(True)

histogramRecipes["RPVReffiting_MMcomparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["RPVReffiting_MMcomparison"].distributions.append(Distribution(newRPV, "Events", "abs(MMBase_trackIxy)", r.kBlue-7, "Original I_{xy}", cut = "MMBase_refittedIxy != -99"))
histogramRecipes["RPVReffiting_MMcomparison"].distributions.append(Distribution(newRPV, "Events", "abs(MMBase_refittedIxy)", r.kRed-7, "Refitted I_{xy}", cut = "MMBase_refittedIxy != -99"))
histogramRecipes["RPVReffiting_MMcomparison"].setLog(True)

### DY refitting studies:
histogramRecipes["DYReffiting_EEcomparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["DYReffiting_EEcomparison"].distributions.append(Distribution(DY, "Events", "abs(EEBase_trackIxy)", r.kBlue-7, "Original I_{xy}", cut = "EEBase_refittedIxy != -99"))
histogramRecipes["DYReffiting_EEcomparison"].distributions.append(Distribution(DY, "Events", "abs(EEBase_refittedIxy)", r.kRed-7, "Refitted I_{xy}", cut = "EEBase_refittedIxy != -99"))
histogramRecipes["DYReffiting_EEcomparison"].setLog(True)

histogramRecipes["DYReffiting_MMcomparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["DYReffiting_MMcomparison"].distributions.append(Distribution(DY, "Events", "abs(MMBase_trackIxy)", r.kBlue-7, "Original I_{xy}", cut = "MMBase_refittedIxy != -99"))
histogramRecipes["DYReffiting_MMcomparison"].distributions.append(Distribution(DY, "Events", "abs(MMBase_refittedIxy)", r.kRed-7, "Refitted I_{xy}", cut = "MMBase_refittedIxy != -99"))
histogramRecipes["DYReffiting_MMcomparison"].setLog(True)
