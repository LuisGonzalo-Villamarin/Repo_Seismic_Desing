import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#########################################################################################################################################
#########################################################################################################################################
###################################### Simple CLASS for SDOF system in free vibration ####################################################
#########################################################################################################################################
#########################################################################################################################################

class Simple_free_motion():
    def __init__(self, xo, xvo, w, to, dt, tf):
        self.xo = xo
        self.xvo = xvo
        self.w = w
        self.to = to
        self.dt = dt
        self.tf = tf
    
    def sim_free_sdof_nodamp(self):
        xo = self.xo
        xvo = self.xvo
        w = self.w
        to = self.to
        dt = self.dt
        tf = self.tf

        x = []
        ti = []

        for t in np.arange(to,tf, dt):
            x.append(xo * np.cos(w*t) + xvo / w * np.sin(w*t))
            ti.append(t)
        
        x_df = pd.DataFrame(x, columns= ['Amplitude'])
        ti_df = pd.DataFrame(ti, columns= ['Time'])
        resul = pd.concat([ti_df, x_df], axis=1, ignore_index=False)
        
        return x, ti, resul