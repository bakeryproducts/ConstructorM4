import numpy as np
from utils import get_angles

class Intersection_analysis:
    def __init__(self, inters, ang_data, comp_data):
        self.data = inters
        self.n_angles, self.a_angles, self.b_angles = ang_data
        self.comps = comp_data
        
    def sort(self, ar):
        #ar==self.data
        self.data_sorted = ar[np.lexsort((ar[:, 0], ar[:, 1]))]

    def pair_id_comp(self, idxs):
        true_inds, id_by_comp = self.restore_comp_ind(idxs, self.comps)
        self.id_face = np.concatenate([true_inds.reshape((-1,1)), id_by_comp.reshape((-1,1))], axis=1)

    def pair_id_angle(self, idxs):
        hs,vs = get_angles(self.a_angles, self.b_angles)
        angs = np.array([(a,b) for b in vs for a in hs ])
        self.id_ang = angs[idxs//self.n_angles]

    def create_log(self):
        idxs = self.data[:,1].astype(np.int)
        self.pair_id_angle(idxs)
        self.pair_id_comp(idxs)
        t = np.concatenate([self.data, self.id_ang, self.id_face], axis=1)
        np.save('test.npy', t)

    def restore_comp_ind(self, i, comp_ls):
        """ given index in results and lengths of all components,
         returns index of face inside component and component id 
        
        Arguments:
            i index
            comp_ls [] list of comps lengths
        
        Returns:
            ls = np.array([112,542,1000,23])
            inds = np.array([0,111,112,653,654])
            restore_comp_ind(inds, ls) # (array([  0, 111, 112, 541, 654]), array([0, 0, 1, 1, 2]))
        """
        ct = np.cumsum(comp_ls)
        idx_comp = (ct<=i.reshape((-1,1))).sum(axis=1)
        true_ind = i - ct[idx_comp-1] #if idx > 1 else i
        true_ind[true_ind<=0] = i[true_ind<=0]
        return true_ind, idx_comp
    
    
        
    