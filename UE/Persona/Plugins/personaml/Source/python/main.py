from operator import truediv
import unreal
import subprocess
import sys
import importlib
import time
import os
import json



def reimport_texture():
    import_task = unreal.AssetImportTask()
    import_task.automated = True
    import_task.destination_name =''
    import_task.destination_path = '/personaml/MLImported'
    import_task.filename = 'D:/Persona/FBX/baked_diffuse.png'
    import_task.replace_existing = True
    import_task.save = True
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])

def reimport_mesh(fbx_path):
    import_task = unreal.AssetImportTask()   
    import_task.destination_name = ''   
    import_task.destination_path = '/personaml/MLImported/'
    import_task.filename = fbx_path   
    import_task.replace_existing = True   
    import_task.automated = False
    import_task.save = True  
    import_task.factory = unreal.ReimportFbxAnimSequenceFactory() 
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])

def reimport_animation(fbx_path):   
    import_task = unreal.AssetImportTask()   
    import_task.destination_name = 'wrappedHead_v001_Anim'   
    import_task.destination_path = '/personaml/MLImported/'
    import_task.filename = fbx_path   
    import_task.replace_existing = True   
    import_task.automated = False
    import_task.save = True  
    import_task.factory = unreal.ReimportFbxAnimSequenceFactory() 
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])

def not_unreal_actions():
    topologypath = 'D:\\Persona\\Maya\\input\\baked_new_topology.obj'
    
    if os.path.exists(topologypath):
        os.remove(topologypath)
    
    os.system("start /wait cmd /c py D:\\Persona\\UE\\Persona\\Plugins\\personaml\\Source\\python\\mainexternal.py")

fbxFilePath = 'D:/Persona/FBX/wrappedHead_v001.fbx'


not_unreal_actions()

reimport_texture()

reimport_mesh(fbxFilePath)

reimport_animation(fbxFilePath)


f = open(r'D:/Persona/Maya/Input/ML_Head/body_shape_classifier/ML_Head.json')
jsoned_body = json.load(f)

body_type = jsoned_body["body_shape"]


def body_changing(x):
    actor = unreal.GameplayStatics.get_all_actors_with_tag(unreal.EditorLevelLibrary.get_editor_world(), 'Human')
    if x == 'female_M': 
        actor[0].call_method("Activate_F_M")
    elif x == 'female_L': 
        actor[0].call_method("Activate_F_L")
    elif x == 'male_L': 
        actor[0].call_method("Activate_M_L")
    elif x == 'male_M': 
        actor[0].call_method("Activate_M_M")
    else:
        return 0

# body_changing(body_type)

