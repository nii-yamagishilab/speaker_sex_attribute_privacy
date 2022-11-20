#!/bin/bash
# ==============================================================================
# Copyright (c) 2022, Yamagishi Laboratory, National Institute of Informatics
# Author: Xiaoxiao Miao (xiaoxiaomiao@nii.ac.jp)
# All rights reserved.
# ==============================================================================

source env.sh

echo -e "${RED}Try pre-trained model${NC}"

model_typed=demo


for dset in libri_dev_{enrolls,trials_m,trials_f} libri_test_{enrolls,trials_m,trials_f}; do
	python adapted_from_facebookresearch/inference.py --input_test_file scp/vpc/$dset.lst \
		--xv_glob global_sex_neutral_xvect/globalavg_neutralsex.xvector \
		--checkpoint_file pretrained_models_anon_xv/HiFi-GAN/$model_type \
		--output_dir pretrained_models_anon_xv/output/${model_type}/sexanon/${dset}

	echo "$dset DONE" 

done
echo -e "${RED}Please check generated waveforms from pre-trained model in ./pretrained_models/output"
 
