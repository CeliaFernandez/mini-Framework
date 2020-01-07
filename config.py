from interface.Recipe import Recipe
from interface.Distribution import Distribution

##############################
###  Variable declaration  ###
##############################

RPV = "/gpfs/projects/cms/fernance/DisplacedSUSY_squarkToQuarkChi_MSquark_350_MChi_148_ctau_173mm_TuneCP2_13TeV_80X_19062019-1840/crab_RPV_350-148-173_newTuples/200102_111514/RPV_350_148_173.root"
DY = "/gpfs/projects/cms/fernance/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYJetsToLL_M-50_newNTuples/200102_111608/DY_50.root"

####################
###  Basic cuts  ###
####################
muonChannel = "Flag_HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10 == 1"
electronChannel = "Flag_HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10 == 0 && Flag_HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon25_AND_HE10_R9Id65_Eta2_Mass15 == 1"


###########################
###  Histogram recipes  ###
###########################

histogramRecipes = {}

histogramRecipes["nEEBase"] = Recipe("Number of EE Candidates", [3, 0.0, 3.0])
histogramRecipes["nEEBase"].distributions.append(Distribution(DY, "Events", "nEEBase", r.kRed-7, "DYJetsToLL (M-50)", cut = electronChannel))
histogramRecipes["nEEBase"].distributions.append(Distribution(RPV, "Events", "nEEBase", r.kBlue-7, "RPV(350,148,17.3)", cut = electronChannel))
histogramRecipes["nEEBase"].setLog(True)

histogramRecipes["nMMBase"] = Recipe("Number of MM candidates", [3, 0.0, 3.0])
histogramRecipes["nMMBase"].distributions.append(Distribution(DY, "Events", "nMMBase", r.kRed-7, "DYJetsToLL (M-50)", cut = muonChannel))
histogramRecipes["nMMBase"].distributions.append(Distribution(RPV, "Events", "nMMBase", r.kBlue-7, "RPV(350,148,17.3)", cut = muonChannel))
histogramRecipes["nMMBase"].setLog(True)

histogramRecipes["EEtrackIdx_comparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["EEtrackIdx_comparison"].distributions.append(Distribution(RPV, "Events", "abs(EEBase_trackIxy)", r.kBlue-7, "RPV(350,148,17.3)", cut = electronChannel))
histogramRecipes["EEtrackIdx_comparison"].distributions.append(Distribution(DY, "Events", "abs(EEBase_trackIxy)", r.kRed-7, "DYJetsToLL (M-50)", cut = electronChannel))
histogramRecipes["EEtrackIdx_comparison"].setLog(True)

histogramRecipes["EEtrackDxy_comparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 5.0])
histogramRecipes["EEtrackDxy_comparison"].distributions.append(Distribution(RPV, "Events", "abs(EEBase_trackDxy)", r.kBlue-7, "RPV(350,148,17.3)", cut = electronChannel))
histogramRecipes["EEtrackDxy_comparison"].distributions.append(Distribution(DY, "Events", "abs(EEBase_trackDxy)", r.kRed-7, "DYJetsToLL (M-50)", cut = electronChannel))
histogramRecipes["EEtrackDxy_comparison"].setLog(True)

histogramRecipes["MMtrackIdx_comparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["MMtrackIdx_comparison"].distributions.append(Distribution(RPV, "Events", "abs(MMBase_trackIxy)", r.kBlue-7, "RPV(350,148,17.3)", cut = muonChannel))
histogramRecipes["MMtrackIdx_comparison"].distributions.append(Distribution(DY, "Events", "abs(MMBase_trackIxy)", r.kRed-7, "DYJetsToLL (M-50)", cut = muonChannel))
histogramRecipes["MMtrackIdx_comparison"].setLog(True)

histogramRecipes["MMtrackDxy_comparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 5.0])
histogramRecipes["MMtrackDxy_comparison"].distributions.append(Distribution(RPV, "Events", "abs(MMBase_trackDxy)", r.kBlue-7, "RPV(350,148,17.3)", cut = muonChannel))
histogramRecipes["MMtrackDxy_comparison"].distributions.append(Distribution(DY, "Events", "abs(MMBase_trackDxy)", r.kRed-7, "DYJetsToLL (M-50)", cut = muonChannel))
histogramRecipes["MMtrackDxy_comparison"].setLog(True)

histogramRecipes["ExcludedTracks"] = Recipe("Excluded tracks from PV refitting", [5, 0.0, 5.0])
histogramRecipes["ExcludedTracks"].distributions.append(Distribution(DY, "Events", "RefittedPV_nExcludedTrack", r.kRed-7, "DYJetsToLL (M-50)", cut = "(("+electronChannel+") || ("+muonChannel+")) && RefittedPV_vx != -99"))
histogramRecipes["ExcludedTracks"].distributions.append(Distribution(RPV, "Events", "RefittedPV_nExcludedTrack", r.kBlue-7, "RPV(350,148,17.3)", cut = "EEBase_refittedDxy != -99"))

histogramRecipes["PV_dX"] = Recipe("Refitted PV x - Original PV x", [40, -5.0, 5.0])
histogramRecipes["PV_dX"].distributions.append(Distribution(DY, "Events", "RefittedPV_vx - PV_vx", r.kRed-7, "DYJetsToLL (M-50)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["PV_dX"].distributions.append(Distribution(RPV, "Events", "RefittedPV_vx - PV_vx", r.kBlue-7, "RPV(350,148,17.3)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["PV_dX"].setLog(True)

histogramRecipes["PV_dY"] = Recipe("Refitted PV y - Original PV y", [40, -5.0, 5.0])
histogramRecipes["PV_dY"].distributions.append(Distribution(DY, "Events", "RefittedPV_vy - PV_vy", r.kRed-7, "DYJetsToLL (M-50)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["PV_dY"].distributions.append(Distribution(RPV, "Events", "RefittedPV_vy - PV_vy", r.kBlue-7, "RPV(350,148,17.3)", cut = "EEBase_refittedDxy != -99"))
histogramRecipes["PV_dY"].setLog(True)


### RPV refitting studies:
histogramRecipes["RPVReffiting_EEcomparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["RPVReffiting_EEcomparison"].distributions.append(Distribution(RPV, "Events", "abs(EEBase_trackIxy)", r.kBlue-7, "Original I_{xy}", cut = "EEBase_refittedIxy != -99"))
histogramRecipes["RPVReffiting_EEcomparison"].distributions.append(Distribution(RPV, "Events", "abs(EEBase_refittedIxy)", r.kRed-7, "Refitted I_{xy}", cut = "EEBase_refittedIxy != -99"))
histogramRecipes["RPVReffiting_EEcomparison"].setLog(True)

histogramRecipes["RPVReffiting_MMcomparison"] = Recipe("Minimum track I_{xy}", [40, 0.0, 20.0])
histogramRecipes["RPVReffiting_MMcomparison"].distributions.append(Distribution(RPV, "Events", "abs(MMBase_trackIxy)", r.kBlue-7, "Original I_{xy}", cut = "MMBase_refittedIxy != -99"))
histogramRecipes["RPVReffiting_MMcomparison"].distributions.append(Distribution(RPV, "Events", "abs(MMBase_refittedIxy)", r.kRed-7, "Refitted I_{xy}", cut = "MMBase_refittedIxy != -99"))
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
