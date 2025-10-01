#!/bin/env bash

#SBATCH --job-name=LOPE_NER     
#SBATCH --partition=shared-gpu
#SBATCH --time=04:00:00
#SBATCH --mem=48GB
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:1,VramPerGpu:48G    
#SBATCH --output=LOPE_NER-%j.out
#SBATCH --error=LOPE_NER-%j.err

module load Python/3.9.6

source /home/users/b/betti/LOPE_ENV/bin/activate

/home/users/b/betti/LOPE_ENV/bin/python /home/users/b/betti/MappingLope/LOPE_NER/NER_TEST_FULL.py
