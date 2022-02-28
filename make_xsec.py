import json

xs = {
    "WW_TuneCP5_13TeV-pythia8": 75.82,
    "WZ_TuneCP5_13TeV-pythia8": 27.6,
    "ZZ_TuneCP5_13TeV-pythia8": 12.14,
    "QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 248600000.,
    "QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 27990000.,
    "QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 9999999.,#FIXME
    "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 322600.,# huge weights
    "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 29980.,
    "QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8": 29980.,
    "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 6334.,
    "QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8": 6334.,
    "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 1088.,
    "QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8": 1088.,
    "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 99.11,
    "QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8": 99.11,
    "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8": 20.23,
    "QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8": 20.23,
    "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8": 6225.42,
    "DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8": 161.1,
    "DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8": 48.58,
    "DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8": 5.678,
    "DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8": 1.738,
    "DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8": 0.8077,
    "DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8": 0.1514,
    "DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8": 0.003435,
    "DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8": 89.39,
    "DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8": 3.43,
    "DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8": 0.464,
    "DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8": 0.0436,
    "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8": 52940.,
    "WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8": 999999.,#FIXME
    "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8": 1343,
    "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8": 359.6,
    "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8": 48.85,
    "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8": 12.05,
    "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8": 5.501,
    "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8": 1.329,
    "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8": 0.03216,
    "WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 315.6,
    "WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 68.57,
    "WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8": 34.9,
    "ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 145.4,
    "ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 34.0,
    "ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8": 18.67,
    "ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8": 11.24,
    "ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-madgraph-pythia8": 11.24,
    "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8": 3.74,
    "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8": 3.74,
    "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 26.2278,
    "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8": 26.2278,
    "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 44.07048,
    "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8": 44.07048,
    "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 35.6,
    "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8": 35.6,
    "ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8": 35.6,
    "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8": 35.6,
    "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8": 88.29,
    "TTToHadronic_TuneCP5_13TeV-powheg-pythia8": 377.96,
    "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8": 365.34,
    "GluGluHToTauTau_M125_13TeV_powheg_pythia8": 48.58*0.0627,
    "VBFHToTauTau_M125_13TeV_powheg_pythia8":3.782*0.0627,
    "WminusHToTauTau_M125_13TeV_powheg_pythia8":0.5328*0.0627,
    "WplusHToTauTau_M125_13TeV_powheg_pythia8":0.8400*0.0627,
    "ZHToTauTau_M125_13TeV_powheg_pythia8":0.7612*0.0627,
    "ggZH_HToTauTau_ZToLL_M125_13TeV_powheg_pythia8":0.1227*0.0627*3*0.033658,
    "ggZH_HToTauTau_ZToNuNu_M125_13TeV_powheg_pythia8":0.1227*0.0627*0.2000,
    "ggZH_HToTauTau_ZToQQ_M125_13TeV_powheg_pythia8":0.1227*0.0627*0.6991,
    "ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8":0.5269*0.0627,
    "GluGluHToTauTau": 0.8045*0.0627, #from lhe (x BR)
    "GluGluHToWWToLNuQQ_M125_NNPDF31_TuneCP5_PSweights_13TeV_powheg_JHUGen710_pythia8":48.58*0.2137*2.*0.676*0.108,
    "GluGluHToWWToLNuQQ_M125_TuneCP5_PSweight_13TeV-powheg2-jhugen727-pythia8":48.58*0.2137*2.*0.676*0.108,
    "Spin0ToTauTau_2j_scalar_g1_HT300_M10_nodmx_v0_TuneCP5_MLM": 9.85e-02,
    "Spin0ToTauTau_2j_scalar_g1_HT300_M30_nodmx_v0_TuneCP5_MLM": 1.78e-02,
    "Spin0ToTauTau_2j_scalar_g1_HT300_M50_nodmx_v0_TuneCP5_MLM": 1.61e-02,
    "Spin0ToTauTau_2j_scalar_g1_HT300_M125_nodmx_v0_TuneCP5_MLM": 1.28e-02,
    "Spin0ToTauTau_2j_scalar_g1_HT300_M300_nodmx_v0_TuneCP5_MLM": 8.34e-03,

    "QCD_HT500to700": 30330.0,
    "QCD_HT700to1000": 6412.0,
    "QCD_HT1000to1500": 1118.0,
    "QCD_HT1500to2000": 108.5,
    "QCD_HT2000toInf": 21.94,
    "QCD_Pt_120to170": 407400.0,
    "QCD_Pt_170to300": 103500.0,
    "QCD_Pt_300to470": 6833.0,
    "QCD_Pt_470to600": 549.5,
    "QCD_Pt_600to800": 0,
    "QCD_Pt_800to1000": 26.22,
    "QCD_Pt_1000to1400": 7.475,
    "QCD_Pt_1400to1800": 0.6482,
    "QCD_Pt_1800to2400": 0.08742,
    "QCD_Pt_2400to3200": 0.005237,
    "QCD_Pt_3200toInf": 0.0001353,
    "TTTo2L2Nu": 77.10979749999998,
    "TTToHadronic": 303.8527975,
    "TTToSemiLeptonic": 306.137405,
    "ST_s-channel_4f_leptonDecays": 1.188915,
    "ST_t-channel_antitop_4f_InclusiveDecays": 67.93,
    "ST_t-channel_antitop_5f_InclusiveDecays": 71.74,
    "ST_t-channel_top_4f_InclusiveDecays": 113.4,
    "ST_t-channel_top_5f_InclusiveDecays": 119.7,
    "ST_tW_antitop_5f_inclusiveDecays": 32.51,
    "ST_tW_antitop_5f_NoFullyHadronicDecays": 10.890849999999999,
    "ST_tW_top_5f_inclusiveDecays": 32.45,
    "ST_tW_top_5f_NoFullyHadronicDecays": 10.87075,
    "WJetsToQQ_HT-400to600": 277.0,
    "WJetsToQQ_HT-600to800": 59.06,
    "WJetsToQQ_HT-800toInf": 28.75,
    "WJetsToLNu_HT-70To100": 1270.0,
    "WJetsToLNu_HT-100To200": 1252.0,
    "WJetsToLNu_HT-200To400": 336.5,
    "WJetsToLNu_HT-400To600": 45.12,
    "WJetsToLNu_HT-600To800": 10.99,
    "WJetsToLNu_HT-800To1200": 4.938,
    "WJetsToLNu_HT-1200To2500": 1.155,
    "WJetsToLNu_HT-2500ToInf": 0.02625,
    "ZJetsToQQ_HT-400to600": 114.5,
    "ZJetsToQQ_HT-600to800": 25.41,
    "ZJetsToQQ_HT-800toInf": 12.91,
    "DYJetsToLL_HT-70to100": 139.9,
    "DYJetsToLL_HT-100to200": 140.1,
    "DYJetsToLL_HT-200to400": 38.35,
    "DYJetsToLL_HT-400to600": 5.217,
    "DYJetsToLL_HT-600to800": 1.267,
    "DYJetsToLL_HT-800to1200": 0.5682,
    "DYJetsToLL_HT-1200to2500": 0.1332,
    "DYJetsToLL_HT-2500toInf": 0.002978,
    "DYJetsToLL_Pt-100to250": 94.78,
    "DYJetsToLL_Pt-250to400": 3.629,
    "DYJetsToLL_Pt-400to650": 0.4980,
    "DYJetsToLL_Pt-650toInf": 0.1143,
    "EWKZ_ZToQQ": 0,
    "EWKZ_ZToLL": 6.207,
    "EWKZ_ZtoNuNu": 10.65,
    "EWKWminus_WToQQ": 0,
    "EWKWplus_WToQQ": 0,
    "EWKWminus_WToLNu": 32.08,
    "EWKWplus_WToLNu": 39.09,
    "WW": 75.83,
    "WZ": 27.56,
    "ZZ": 12.14,
    "GluGluHToBB_MINLO": 0,
    "VBFHToBB": 2.2498257,
    "WminusH_HToBB_WToQQ": 0,
    "WplusH_HToBB_WToQQ": 0,
    "WminusH_HToBB_WToLNu": 0,
    "WplusH_HToBB_WToLNu": 0,
    "ZH_HToBB_ZToQQ": 0,
    "ZH_HToBB_ZToLL": 0,
    "ZH_HToBB_ZToNuNu": 0,
    "ggZH_HToBB_ZToNuNu": 0,
    "ggZH_HToBB_ZToQQ": 0,
    "ggZH_HToBB_ZToLL": 0,
    "ttHToBB": 0.29120516999999996
}
zkeys = []
for d in xs.keys():
    if "DYJetsToLL_Pt" in d:
       zkeys.append(d)
for z in zkeys:
    xs[z+"_Zee"] = xs[z]
    xs[z+"_Zmm"] = xs[z]
    xs[z+"_Zem"] = xs[z]
    xs[z+"_Ztt"] = xs[z]

with open('fileset/xsecs.json', 'w') as outfile:
    json.dump(xs, outfile, indent=4)
