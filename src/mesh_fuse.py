import argparse, os
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--colmap_dense', default='data/colmap_workspace/dense')
    parser.add_argument('--out_mesh', default='data/meshes/scene.obj')
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.out_mesh), exist_ok=True)
    print('Placeholder: aquí ejecutarías herramientas de meshing (Poisson, OpenMVS, etc.)')
    open(args.out_mesh,'w').write('# OBJ placeholder\n')
    print('Malla placeholder escrita en', args.out_mesh)
