## init.py
## loaded by nuke before menu.py
import nuke

# to add a folder that lives inside '.nuke' folder -> nuke.pluginAddPath('./myFolder')

nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./gizmos/WaveMachine_v1.0')
nuke.pluginAddPath('./gizmos/nuke-vector-matrix')
nuke.pluginAddPath('./pixelfudger3')

# more comfyui setup
nuke.pluginAddPath('./ComfyUINuke')

alexa35Format = '4608 3164 alexa35'
nuke.addFormat(alexa35Format)

nuke.knobDefault('Root.format', 'alexa35')


# Set the path for your shared_nuke_tools directory in this string, between the ''
SHARED_NUKE_TOOLS_PATH = '/Volumes/sandwich-post/assets/comp_tools/shared_nuke_tools/'

nuke.pluginAddPath(SHARED_NUKE_TOOLS_PATH)
