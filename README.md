# OBJ-Polyline-Converter
1) obj_mod.py is a python script that takes obj line files (in our case the particle track obj's we got from iSpy) and redefines them as a surface, allowing it to be rendered in Unity. Gonna work on it more so that it looks better when loaded in blender.
    track__.obj and modified_track__.obj are examples of how the script works. Tracks_V3 is the publicly available track obj file from iSpy's "Hto4l_120-130GeV.ig:     Events/Run_201191/Event_1357605031" event dataset (multiple lines in one file), and you can probably guess what modified_Tracks_V3 is.

2) obj_quad_mod.py does the same thing, but defines the surfaces as quadrilaterals. Benefits are that it renders better, and the resultant file is much smaller than the resultant file from obj_mod.py (transforming a 3955 sloc source obj file into a 11187 sloc file vs 14915 sloc file). modified_Tracks_V3_quad.obj is an example.
