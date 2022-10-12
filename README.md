# CMS-VR-Event-Display-Stuff
1) obj_mod is a python script that takes obj line files (in our case the particle track obj's we got from iSpy) and redefines them as a surface, allowing it to be rendered in Unity. Gonna work on it more so that it looks better when loaded in blender.
    track__.obj and modified_track__.obj are examples of how the script works
    
2) obj_mod_multi_track.py is the same as obj_mod.py, except that it works for obj files that define multiple different lines in one file. Tracks_V3 is the publicly available track obj file from iSpy's "Hto4l_120-130GeV.ig: Events/Run_201191/Event_1357605031" event dataset, and you can probably guess what modified_Tracks_V3 is.
