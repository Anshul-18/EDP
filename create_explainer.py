import numpy as np
from lime import lime_tabular
import dill
import joblib
import pickle

# Load your classifier
with open('models/model.pkl', 'rb') as f:
    classifier = pickle.load(f)

# Create features array (replace with actual feature names if different)
features = ['FlowDuration', 'BwdPacketLengthMax', 'BwdPacketLengthMin', 
           'BwdPacketLengthMean', 'BwdPacketLengthStd', 'FlowIATMean', 
           'FlowIATStd', 'FlowIATMax', 'FlowIATMin', 'FwdIATTotal', 
           'FwdIATMean', 'FwdIATStd', 'FwdIATMax', 'FwdIATMin', 
           'BwdIATTotal', 'BwdIATMean', 'BwdIATStd', 'BwdIATMax', 
           'BwdIATMin', 'FwdPSHFlags', 'FwdPackets/s', 'PacketLengthMax',
           'PacketLengthMean', 'PacketLengthStd', 'PacketLengthVariance',
           'FINFlagCount', 'SYNFlagCount', 'PSHFlagCount', 'ACKFlagCount',
           'URGFlagCount', 'AveragePacketSize', 'BwdSegmentSizeAvg',
           'FWDInitWinBytes', 'BwdInitWinBytes', 'ActiveMin', 'IdleMean',
           'IdleStd', 'IdleMax', 'IdleMin']

# Create a new explainer
explainer = lime_tabular.LimeTabularExplainer(
    np.zeros((1,39)),  # Training data
    feature_names=features,
    class_names=['Benign', 'Botnet', 'DDoS', 'DoS', 'FTP-Patator', 'Probe', 'SSH-Patator', 'Web Attack'],
    mode='classification'
)

# Save the new explainer
with open('models/explainer', 'wb') as f:
    dill.dump(explainer, f)

print("New explainer created and saved successfully!") 