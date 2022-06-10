# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:21:27 2022

@author: makow
"""

from predict import *

to_parse = '--model-location esm1v_t33_650M_UR90S_1 esm1v_t33_650M_UR90S_2 esm1v_t33_650M_UR90S_3 esm1v_t33_650M_UR90S_4 esm1v_t33_650M_UR90S_5\
    --sequence QVQLVQSGAEVKKPGASVKVSCKASGYTFTDYYMHWVRQAPGQGLEWMGRVNPNGRGTTYNQKFEGRVTMTTDTSTSTAYMELRSLRSDDTAVYYCARSNLLDDWGQGTTVTVSS \
    --dms-input ./data/emi_igg.csv\
    --mutation-col mutant\
    --dms-output ./data/emi_igg_labeled.csv\
    --offset-idx 32\
    --scoring-strategy masked-marginals'

parser = create_parser()
args = parser.parse_args(to_parse.split())
main(args)
