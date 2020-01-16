chmod +x /gpfs/users/fernanc/CMSSW_9_4_4/src/MyAnalysis/mini-Framework/submit_plotter.sh
qsub -o /gpfs/users/fernanc/CMSSW_9_4_4/src/MyAnalysis/mini-Framework/logs/plotter.log -e /gpfs/users/fernanc/CMSSW_9_4_4/src/MyAnalysis/mini-Framework/logs/plotter.err /gpfs/users/fernanc/CMSSW_9_4_4/src/MyAnalysis/mini-Framework/submit_plotter.sh
