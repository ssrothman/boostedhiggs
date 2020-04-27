import json

xs = {
    "WW_TuneCP5_13TeV-pythia8": 63.21,
    "WZ_TuneCP5_13TeV-pythia8": 10.32,
    "ZZ_TuneCP5_13TeV-pythia8": 22.82,
    "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 1064.,
    "QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 9999999., #FIXME
    "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 121.5,
    "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 25.42,
    "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 366800.,
    "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 29370.,
    "QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 9999999., #FIXME
    "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 6524.,
    "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8": 6077.22,
    "DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8": 161.1,
    "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8": 0.1933,
    "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8": 48.66,
    "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8": 0.003468,
    "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8": 6.968,
    "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8": 1.743,
    "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8": 0.8052,
    "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8": 52850.,
    "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8": 1395.,
    "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8": 1.074,
    "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8": 407.9,
    "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8": 0.008001,
    "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8": 57.48,
    "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8": 12.87,
    "WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8": 1292.,
    "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8": 5.366,
    "WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 34.9,
    "WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 315.6,
    "WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 68.57,
    "ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 18.67,
    "ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 145.4,
    "ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 34.9,
    "ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8": 5., #FIXME
    "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8": 3.74,
    "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 80.95,
    "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 136.02,
    "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 34.91,
    "ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 34.91,
    "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8": 687.1, #FIXME?
    "TTToHadronic_TuneCP5_13TeV-powheg-pythia8": 377.96,
    "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8": 365.34,
    "GluGluHToTauTau": 21.4
}

with open('xsec.json', 'w') as outfile:
    json.dump(xs, outfile, indent=4)