# persona

## Large Files Absent on repo:
 - Directory [UE/Persona/Plugins/personaml/Content/Textures](https://drive.google.com/file/d/1_7xDpZPoq3oN0zRXgpBRslntzgqzSq2Y/view?usp=sharing).
 - Binary [Maya/Karen_M_M_full_rig.mb](https://drive.google.com/file/d/1HlpB_48-OlO0K4lFFPjVR7-VZsRFLbyo/view?usp=sharing).


## Vital points that have to be satysfied for persona app to run:
    - Repo must be placed in D:/Persona dir.
    - Absolute paths to Maya and Houdini in Maya/HBaker_v003.bat (default for Houdini 19.0.622 and maya 2020).
    - Houdini Limited Commercial License.
    - Maya2020 License.
    - Python libraries: tqdm, requests, tk-tools TODO: Find the way to launch venv on start.
    - IP adress have to be whitelisted by appsilon. 


## Problems that have to be solved in priority order, starting with the most important:
    - Maya DNA interpretation node, now character has no animation, because bones have no connection to control rig.
    - Packaging python operations (venv or binary).
    - UE pipeline modification: copying the plugin character into current project.
    - Material correction pipeline modification, procedural color correction.


## To test the plugin:
    - Download missing files and place them properly
    - Go to the UE/Persona/Persona2.uproject
    - Click Persona Button on the top of the editor.
    - Choose concept you want to begin with.
    - Wait with black window that communicates with ml api from appsilon.
    - Houdini launches and do the topology rebake.
    - Maya launches and do the rigging.
    - We got our concept personified in /personaml/MLImported/wrappedHead_001 and linked to BP_Persona in the