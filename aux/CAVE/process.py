import glob
from pathlib import Path

import cv2
import numpy as np
import scipy.io

DATASET_PATH = 'data/GT/CAVE'

for hs_path in glob.iglob(f'{DATASET_PATH}/*/'):
    name = Path(hs_path).stem
    hsi = None
    # read all PNGs correspnding to different spectra to form the HS cube
    for img_path in glob.iglob(f'{hs_path}/*.png'):
        img = np.asarray(cv2.imread(img_path, cv2.IMREAD_GRAYSCALE))
        img = np.expand_dims(img, axis=2) 
        hsi = img if  hsi is None else np.concatenate((hsi, img), axis=2)
    # read BMP with the RGB image
    msi_path = glob.glob(f'{hs_path}/*.bmp')[0]
    msi = np.asarray(cv2.cvtColor(cv2.imread(msi_path), cv2.COLOR_BGR2RGB))
    # save both together as MAT file
    scipy.io.savemat(f'{DATASET_PATH}/{name}.mat', {"hsi": hsi, "msi": msi})