import numpy as np

def get_angles(h_params, v_params):
    a_st, a_end, step_a = h_params.get('start',0), h_params.get('end', 360), h_params.get('step', 10)
    b_st, b_end, step_b = v_params.get('start',0), v_params.get('end', 360), v_params.get('step', 10)
    
    step_a = (a_end - a_st) // step_a
    step_b = (b_end - b_st) // step_b
    
    horz_angles = np.linspace(a_st, a_end, step_a)
    vert_angles = np.linspace(b_st, b_end, step_b)
    horz_angles = [np.deg2rad(i) for i in horz_angles]
    vert_angles = [np.deg2rad(i) for i in vert_angles]
    
    return horz_angles, vert_angles

def rotate_points(points, a, b):
    my = np.array([[np.cos(b),0,np.sin(b)],[0,1,0],[-np.sin(b),0,np.cos(b)]])
    mz = np.array([[np.cos(a), -np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1]])
    return np.matmul(np.matmul(points,my),mz)

def generate_2d_dist(n):
    return 10*np.random.random((n,2))-.5#np.array([0,0])#


def get_shots(h_params, v_params, n=1000, debug=False):
    horz_angles, vert_angles = get_angles(h_params, v_params)
    
    if debug:
        print('Rays generator: h, v, total:',len(horz_angles), len(vert_angles),len(horz_angles)* len(vert_angles))
    
    rays, points, indxs = [],[],[]
    data = np.zeros((n,3)) 
            
    for ah in horz_angles:
        for av in vert_angles:
            x,y,z = np.cos(av)*np.sin(ah),np.cos(av)*np.cos(ah), np.sin(av)
            ray = -np.array([x,y,z]) * 1e5
            rays.append(ray)
            
            data[:,:2] = generate_2d_dist(n)
            data2 = rotate_points(data, ah, av)
            points.append(data2 - ray)
            
            indxs.append([ah,av])
    
    return np.array(indxs), np.array(rays), np.array(points).astype(np.float32)

def combine_rp(rays, p):
    #p:[v*h, N, 3], rays:[v*h, 3], returns [v*h*N*2,3] 2 for pair: ray.dir, ray.point
    p = np.expand_dims(p,2)
    p = np.repeat(p, 2, axis=2)
    p[:,:,0] = np.repeat(rays.reshape(rays.shape[0], 1, 3), p.shape[1], axis=1)
    return p.reshape((-1,3))

def intersect_batch(polys, shots_batch, lock=None, debug=False):
    if debug:
        print('Int count:{} m'.format(polys.shape[0]*shots_batch.shape[0]/1e6))
    
    from lti import fact as intersection
    results = intersection(polys,shots_batch)
    return results 

def convert_results(results, indxs, shots_batch, debug=False):
    num_rays = shots_batch.shape[0]//2
    num_shots = num_rays // indxs.shape[0]
    
    ids = results[:,1].astype(np.int)
    uni_ray = ids // n1#(ids - ids%(n1)) // (n1)
    poly_ids = ids%n1
    
    conv_results = []
    ur = np.unique(uni_ray)
    print(uni_ray.shape)
    
    for ray in ur :
        ray_ang = indxs[ray //n2]
        #print(ray, ray_ang)
        
        #ray_ang = indxs[ray]
        idxs = np.argwhere(uni_ray == ray)
        #print(idxs)
        
        ray_polys = poly_ids[idxs]
        ha, va = np.rad2deg(ray_ang[0]),np.rad2deg(ray_ang[1])
        conv_results.append([ha,va,ray_polys])
    
        if debug:
            print("ray# {0}: {1:.0f},{2:.0f} :".format(ray,ha,va),';'.join([str(i) for i in ray_polys]))
        
    return conv_results


