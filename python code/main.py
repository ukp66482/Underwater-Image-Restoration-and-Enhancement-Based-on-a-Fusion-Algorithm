import numpy as np
import cv2
import os

for filename in os.listdir("./UIEB_dataset/input"):
    if filename.endswith(('.png', '.jpg')):
        img_path = os.path.join("./UIEB_dataset/input", filename)
        output_png_path = os.path.join("./result", filename)
        img = cv2.imread(img_path)

    b_origin, g_origin, r_origin = cv2.split(img)
    b_origin = b_origin.astype(float)
    g_origin = g_origin.astype(float)
    r_origin = r_origin.astype(float)

    #Color_Correction
    m_B = np.mean(b_origin)
    m_G = np.mean(g_origin)
    m_R = np.mean(r_origin)
    m_ave = (m_B + m_G + m_R) / 3
    d_B = m_ave - m_B
    d_G = m_ave - m_G
    d_R = m_ave - m_R
    b_new = b_origin + d_B
    g_new = g_origin + d_G
    r_new = r_origin + d_R

    #Finish
    processed_image = cv2.merge([b_new, g_new, r_new])
    cv2.imwrite(output_png_path, processed_image)
    print("Save")