from __future__ import print_function, division
import gzip
import json
import os

import uproot
import matplotlib.pyplot as plt
import mplhep as hep
plt.style.use(hep.styles.ROOT)
import numpy as np

from coffea import hist
from coffea.util import load

import pickle
import gzip
import math

import argparse

import pickle


#cfile = load('../condor/Feb17_NN/hists_sum_SingleMuon.coffea')
#cfile = load('../condor/Jun10_NN/hists_sum_WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8.coffea')
#cfile = load('./htt_test_spin0.coffea')
#cfile = load('./outfiles/2017_test_0--1.hist')
with open("./outfiles/2017_test_0--1.hist", 'rb') as f:
    cfile = pickle.load(f)
#cfile = load('../condor/Mar17_NN/hists_sum_WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8.coffea')
#cfile = load('../condor/Mar17_NN/hists_sum_WJetsToQQ_HT800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8.coffea')
#cfile = load('../condor/Mar17_NN/hists_sum_ZJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8.coffea')
#cfile = load('../condor/Mar17_NN/hists_sum_ZJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8.coffea')
#cfile = load('../condor/Mar17_NN/hists_sum_ZJetsToQQ_HT800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8.coffea')
#cfile = load('htt_nntest.coffea')
print(cfile)
hists_mapped = cfile

h = hists_mapped['met_nn_kin'].integrate('region','hadhad_signal_met').integrate('nn_disc',slice(0.95,None))
#print(h.axis('met_pt').edges())
#print(h.integrate('met_pt',slice(50.,None),'over').sum('h_pt').values())
#print('hadhad',h.sum(*[ax for ax in h.axes() if ax.name not in ['massreg']]).values())
#print('hadhad',h.integrate('massreg',slice(100.,110.)).values())
#h = hists_mapped['jet_nn_kin'].integrate('region','hadhad_met_signal').integrate('nn_disc',slice(0.95,None))
#print('hadhad_met',h.sum(*[ax for ax in h.axes() if ax.name not in ['massreg']]).values())
#h = hists_mapped['jet_nn_kin'].integrate('region','hadmu_signal').integrate('nn_disc',slice(0.95,None))
#print('hadmu',h.sum(*[ax for ax in h.axes() if ax.name not in ['massreg']]).values())
#h = hists_mapped['jet_nn_kin'].integrate('region','hadel_signal').integrate('nn_disc',slice(0.95,None))
#print('hadel',h.sum(*[ax for ax in h.axes() if ax.name not in ['massreg']]).values())

#compiled = load('../boostedhiggs/data/corrections.coffea')
#print(compiled)
#print(compiled['2017_pileupweight_dataset'])
#print([x for x in compiled['2017_pileupweight_dataset']])
#print([compiled['2017_pileupweight_dataset'][x]([10.,20.,30.,40.,50.,60.,70.,80.]) for x in compiled['2017_pileupweight_dataset']])
#print(compiled['2017_pileupweight']([10.,20.,30.,40.,50.,60.,70.,80.]))