#!/bin/zsh
# Shellscript for TU BS AC/OC Cluster
echo $SLURMD_NODENAME

mkdir -p /scratch/$USER/job_$SLURM_JOB_ID/ || exit 1
cd /scratch/$USER/job_$SLURM_JOB_ID/ || exit 1


file=${SLURM_JOB_NAME:r}
echo $file
cp  $SLURM_SUBMIT_DIR/$file   /scratch/$USER/job_$SLURM_JOB_ID/ || exit 1

#Module laden
module load openmpi/4.1.1
module load orca/5.0.0

#Programm ausführen
$ORCA_PATH/orca $file

#Alles zurückkopieren
cp -r * $SLURM_SUBMIT_DIR || exit 1

#Wenn kopieren ok, dann alles löschen
rm -rf /scratch/$USER/job_$SLURM_JOB_ID
