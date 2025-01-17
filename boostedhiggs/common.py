import numpy as np
import awkward
from uproot_methods import TLorentzVectorArray

#dataset_ordering = ['JetHT','SingleElectron','SingleMuon','MET','Tau']
dataset_ordering = {
  '2017':['SingleMuon','SingleElectron','MET','JetHT','Tau'],
  '2018':['SingleMuon','EGamma','MET','JetHT','Tau']
}

pd_to_trig = {
  '2017':{
    'PFHT800':"JetHT",
    'PFHT900':"JetHT",
    'AK8PFJet360_TrimMass30':"JetHT",
    'AK8PFHT700_TrimR0p1PT0p03Mass50':"JetHT",
    'PFHT650_WideJetMJJ950DEtaJJ1p5':"JetHT",
    'PFHT650_WideJetMJJ900DEtaJJ1p5':"JetHT",
    'PFJet450':"JetHT",
    'PFHT1050':"JetHT",
    'AK8PFJet400_TrimMass30':"JetHT",
    'AK8PFJet420_TrimMass30':"JetHT",
    'AK8PFHT800_TrimMass50':"JetHT",
    'PFJet500':"JetHT",
    'AK8PFJet500':"JetHT",
    'Ele50_CaloIdVT_GsfTrkIdT_PFJet165':"SingleElectron",
    'Ele115_CaloIdVT_GsfTrkIdT':"SingleElectron",
    "Ele15_IsoVVVL_PFHT600":"SingleElectron",
    "Ele35_WPTight_Gsf":"SingleElectron",
    "Ele15_IsoVVVL_PFHT450_PFMET50":"SingleElectron",
    'IsoMu27':"SingleMuon",
    'Mu50':"SingleMuon",
    'Mu55':"SingleMuon",
    "Mu15_IsoVVVL_PFHT600":"SingleMuon",
    "Mu15_IsoVVVL_PFHT450_PFMET50":"SingleMuon",
    'PFMETNoMu120_PFMHTNoMu120_IDTight':"MET",
    'PFMETNoMu110_PFMHTNoMu110_IDTight':"MET",
    'DoubleMediumChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTau40_Trk1_eta2p1_Reg':"Tau",
    'MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1':"Tau",
    'MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_1pr':"Tau",
    'DoubleMediumChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Reg':"Tau",
    'MediumChargedIsoPFTau200HighPtRelaxedIso_Trk50_eta2p1':"Tau",
    'MediumChargedIsoPFTau220HighPtRelaxedIso_Trk50_eta2p1':"Tau",
  },
  '2018':{
    'PFHT800':"JetHT",
    'PFHT900':"JetHT",
    'AK8PFJet360_TrimMass30':"JetHT",
    'AK8PFHT700_TrimR0p1PT0p03Mass50':"JetHT",
    'PFHT650_WideJetMJJ950DEtaJJ1p5':"JetHT",
    'PFHT650_WideJetMJJ900DEtaJJ1p5':"JetHT",
    'PFJet450':"JetHT",
    'PFHT1050':"JetHT",
    'AK8PFJet400_TrimMass30':"JetHT",
    'AK8PFJet420_TrimMass30':"JetHT",
    'AK8PFHT800_TrimMass50':"JetHT",
    'PFJet500':"JetHT",
    'AK8PFJet500':"JetHT",
    'Ele50_CaloIdVT_GsfTrkIdT_PFJet165':"EGamma",
    'Ele115_CaloIdVT_GsfTrkIdT':"EGamma",
    "Ele15_IsoVVVL_PFHT600":"EGamma",
    "Ele35_WPTight_Gsf":"EGamma",
    "Ele15_IsoVVVL_PFHT450_PFMET50":"EGamma",
    'IsoMu27':"SingleMuon",
    'Mu50':"SingleMuon",
    'Mu55':"SingleMuon",
    "Mu15_IsoVVVL_PFHT600":"SingleMuon",
    "Mu15_IsoVVVL_PFHT450_PFMET50":"SingleMuon",
    'PFMETNoMu120_PFMHTNoMu120_IDTight':"MET",
    'PFMETNoMu110_PFMHTNoMu110_IDTight':"MET",
    'DoubleMediumChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTau40_Trk1_eta2p1_Reg':"Tau",
    'MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1':"Tau",
    'MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_1pr':"Tau",
    'DoubleMediumChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg':"Tau",
    'DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Reg':"Tau",
    'MediumChargedIsoPFTau200HighPtRelaxedIso_Trk50_eta2p1':"Tau",
    'MediumChargedIsoPFTau220HighPtRelaxedIso_Trk50_eta2p1':"Tau",
  },
}

def isOverlap(events,dataset,triggers,year):
    trig_to_pd = {}
    for p in dataset_ordering[year]:
        trig_to_pd[p] = []
    for t in triggers:
        if t not in trig_to_pd[pd_to_trig[year][t]]:
            trig_to_pd[pd_to_trig[year][t]].append(t)
    overlap = np.ones(events.size, dtype='bool')
    for p in dataset_ordering[year]:
        if dataset.startswith(p):
            pass_pd = np.zeros(events.size, dtype='bool')
            for t in trig_to_pd[p]:
                try:
                    pass_pd = pass_pd | events.HLT[t]
                except:
                    pass
            overlap = overlap & pass_pd
            break
        else:
            for t in trig_to_pd[p]:
                try:
                    overlap = overlap & np.logical_not(events.HLT[t])
                except:
                    pass
    return overlap


def getParticles(events,lo_id=22,hi_id=25,flags=['fromHardProcess', 'isLastCopy']):
    absid = np.abs(events.GenPart.pdgId)
    return events.GenPart[
        # no gluons
        (absid >= lo_id)
        & (absid <= hi_id)
        & events.GenPart.hasFlags(flags)
    ]

def getBosons(events):
    return getParticles(events)

def match(left, right, metric, maximum=np.inf):
    '''Matching utility

    For each item in ``left``, find closest item in ``right``, using function ``metric``.
    The function must accept two broadcast-compatible arrays and return a numeric array.
    If maximum is specified, mask matched elements where metric was greater than it.
    '''
    lr = left.cross(right, nested=True)
    mval = metric(lr.i0, lr.i1)
    idx = mval.argmin()
    if maximum < np.inf:
        matched = lr.i1[idx[mval[idx] < maximum]]
        return matched.copy(content=matched.content.pad(1)).flatten(axis=1)
    else:
        return lr.i1[idx]


def matchedBosonFlavor(candidates, bosons, maxdR=0.8):
    matched = match(candidates, bosons, lambda a, b: a.delta_r(b), maxdR)
    childid = abs(matched.children.pdgId)
    genflavor = (childid == 5).any() * 3 + (childid == 4).any() * 2 + (childid < 4).all() * 1
    return genflavor.fillna(0)

def matchedBosonFlavorLep(candidates, bosons, maxdR=0.8):
    matched = match(candidates, bosons, lambda a, b: a.delta_r(b), maxdR)
    childid = abs(matched.children.pdgId)
    genflavor = (childid == 13).any() * 3 + (childid == 11).any() * 2 + (childid == 15).any() * 1 + ((childid != 15) & (childid != 13) & (childid != 11)).all() * 0
    return genflavor.fillna(0)


def getHTauTauDecayInfo(events,mod=False):
    #print('genvistau pt')
    #print(events.GenVisTau.pt)
    #print('genvistau parent id')
    #print(events.GenVisTau.parent.pdgId)
    #print('genvistau id')
    #print(events.GenVisTau.parent.children.pdgId)
    #genvistau_higgs = events.GenVisTau[events.GenVisTau.parent.pdgId==25]
    genvistau_higgs = events.GenVisTau
    ngenvistau_higgs = (genvistau_higgs.pt.fillna(0.)>0.).sum()
    el_taus = getParticles(events,11,11,['isDirectTauDecayProduct'])
    mu_taus = getParticles(events,13,13,['isDirectTauDecayProduct'])
    nel_taus = (el_taus.pt.fillna(0.)>0.).sum()
    nmu_taus = (mu_taus.pt.fillna(0.)>0.).sum()
    tau_pt = awkward.concatenate([genvistau_higgs.pt, el_taus.pt, mu_taus.pt], axis=1).pad(2, clip=True)
    tau_eta = awkward.concatenate([genvistau_higgs.eta, el_taus.eta, mu_taus.eta], axis=1).pad(2, clip=True)
    tau_phi = awkward.concatenate([genvistau_higgs.phi, el_taus.phi, mu_taus.phi], axis=1).pad(2, clip=True)
    tau_mass = awkward.concatenate([genvistau_higgs.mass, el_taus.mass, mu_taus.mass], axis=1).pad(2, clip=True)
    tau_p4 = TLorentzVectorArray.from_ptetaphim(tau_pt.fillna(0),tau_eta.fillna(0),tau_phi.fillna(0),tau_mass.fillna(0))
    tau_pair = tau_p4.cross(tau_p4)
    tau_pair_dr = tau_pair.i0.delta_r(tau_pair.i1)
    genvistau1_decay = genvistau_higgs[:,0:1].status.pad(1,clip=True).fillna(15).flatten()
    genvistau2_decay = genvistau_higgs[:,1:2].status.pad(1,clip=True).fillna(15).flatten()
    genHTauTauDecay = np.zeros_like(ngenvistau_higgs)
    genHadTau1Decay = np.zeros_like(ngenvistau_higgs)
    genHadTau2Decay = np.zeros_like(ngenvistau_higgs)
    genHTauTauDecay = np.zeros_like(ngenvistau_higgs) + 1*np.array((ngenvistau_higgs==2) & (nel_taus==0) & (nmu_taus==0)).astype(int) + 2*np.array((ngenvistau_higgs==1) & (nel_taus==1) & (nmu_taus==0)).astype(int) + 3*np.array((ngenvistau_higgs==1) & (nel_taus==0) & (nmu_taus==1)).astype(int) + 4*np.array((ngenvistau_higgs==0) & (nel_taus==1) & (nmu_taus==1)).astype(int) + 5*np.array((ngenvistau_higgs==0) & (nel_taus==2) & (nmu_taus==0)).astype(int) + 6*np.array((ngenvistau_higgs==0) & (nel_taus==0) & (nmu_taus==2)).astype(int)
    if mod:
        genHTauTauDecay = genHTauTauDecay * np.array(((tau_pair_dr<0.8) & (tau_pair_dr>0.)).any() & (tau_pt[:,:2]>25.).all()).astype(float)
    else:
        genHTauTauDecay = genHTauTauDecay * (2*np.array(((tau_pair_dr<0.8) & (tau_pair_dr>0.)).any() & (tau_pt[:,:2]>25.).all()).astype(float)-1)
    genHadTau1Decay = np.zeros_like(genvistau1_decay) + 1*np.array((genvistau1_decay==0)).astype(int) + 2*np.array((genvistau1_decay==1)  | (genvistau1_decay==2)).astype(int) + 3*np.array((genvistau1_decay==10) | (genvistau1_decay==11)).astype(int)
    genHadTau2Decay = np.zeros_like(genvistau2_decay) + 1*np.array((genvistau2_decay==0)).astype(int) + 2*np.array((genvistau2_decay==1)  | (genvistau2_decay==2)).astype(int) + 3*np.array((genvistau2_decay==10) | (genvistau2_decay==11)).astype(int)
    return genHTauTauDecay, genHadTau1Decay, genHadTau2Decay

