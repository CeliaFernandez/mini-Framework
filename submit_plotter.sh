

###################
# FLAG definition #
###################

# Request the Bourne Shell
#$ -S /bin/bash

# Change to the current working directory before starting the job
#$ -cwd

# Change the job name to "hello_world"

#$ -N Untame_de_ 

# Resource request. We request 1MB of memory, and 60 seconds of wall
# clock time, that more than is enough for the test.
# -l mem_free=2G
# -l h_rt=4:0:00

# We are using the "l.tests" project for the examples
#$ -P l.gaes


#################
# Actual script #
#################

pushd /gpfs/users/fernanc/CMSSW_9_4_4/src/
eval `scramv1 runtime -sh`
pushd
python /gpfs/users/fernanc/CMSSW_9_4_4/src/MyAnalysis/mini-Framework/runPlotter.py  
