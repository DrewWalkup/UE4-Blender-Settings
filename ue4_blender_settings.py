##################################################################################################
# Unreal-friendly configuration for Blender
#
# Version: 0.5
# Last updated: December 22, 2020
# Forums thread:
# https://forums.unrealengine.com/development-discussion/content-creation/77422-let-s-make-ue-friendly-config-for-blender-maya-navigation
# Original Author: @mission
# Update to Blender 2.91: @dnwalkup
##################################################################################################

import bpy; 

def kmi_props_setattr(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except AttributeError:
        print("Warning: property '%s' not found in keymap item '%s'" %
              (attr, kmi_props.__class__.__name__))
    except Exception as e:
        print("Warning: %r" % e)

x = bpy.context.preferences
wm = bpy.context.window_manager
kc = wm.keyconfigs.user

################################
# Optional, non-default settings
################################

x.inputs.use_auto_perspective = True                               # v0.5 edit: updated for Blender 2.91 - enable: Auto Perspective (auto orthographic views)
x.system.use_region_overlap = True                                 # enable: Region Overlap (makes Tool Shelf transparent)

bpy.data.scenes["Scene"].render.engine = 'CYCLES'            # switch to Cycles Render
bpy.data.scenes["Scene"].cycles.device = 'GPU'               # use GPU for rendering
bpy.context.scene.cycles.preview_samples = 4                 # v0.5 edit: 32 is default for Cycles viewport, customize as you like

bpy.ops.preferences.addon_enable(module="space_view3d_pie_menus")    # v0.5 edit: revised for Blender 2.91 enable addon: "3d Viewport Pie Menus"
bpy.ops.preferences.addon_enable(module="mesh_looptools")            # enable addon: "Mesh: LoopTools"
bpy.ops.preferences.addon_enable(module="fspy_blender")              # v0.5 edit: enable addon: "fSpy"
bpy.ops.preferences.addon_enable(module="node_wrangler")             # v0.5 edit: enable addon: "Node Wrangler"

#################################
# Unreal Editor / Maya navigation
#################################

km = kc.keymaps['3D View']                  # Map 3D View

kmi = km.keymap_items.new('view3d.rotate', 'LEFTMOUSE', 'PRESS', alt=True)
kmi = km.keymap_items.new('view3d.move', 'MIDDLEMOUSE', 'PRESS', alt=True)
kmi = km.keymap_items.new('view3d.dolly', 'RIGHTMOUSE', 'PRESS', alt=True)

x.inputs.invert_mouse_zoom = True
x.inputs.invert_zoom_wheel = False
x.inputs.invert_mouse_zoom = False          # v0.5 edit: maya preference, default is True
x.inputs.view_rotate_method = 'TURNTABLE'
x.inputs.view_zoom_axis = 'HORIZONTAL'      # v0.5 edit: maya preference, default is 'VERTICAL' 

# x.keymap.select_mouse = 'LEFT'            This is depreciated, see https://blender.stackexchange.com/a/184435 

#####################
# UE4 export settings
#####################

bpy.data.scenes["Scene"].unit_settings.system = 'METRIC'
bpy.data.scenes["Scene"].unit_settings.scale_length = 0.01              # v0.5 edit: proper UE4 length settings
bpy.data.scenes["Scene"].unit_settings.length_unit = 'CENTIMETERS'      # v0.5 edit: proper UE4 unit settings
bpy.context.scene.render.fps = 23.98                                    # v0.5 edit: 24 FPS. Cinematicism.
bpy.context.scene.render.fps_base = 1                                   # Framerate base

########################################################
# Fix for ALT+RIGHTMOUSE (zoom) conflict in Edit Mode
# Loop Select by double-clicking instead of single-click
########################################################

km = kc.keymaps['Mesh']             # Map Mesh

kmi = km.keymap_items.remove(km.keymap_items['mesh.loop_select'])
kmi = km.keymap_items.new('mesh.loop_select', 'LEFTMOUSE', 'DOUBLE_CLICK', alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', False)
kmi = km.keymap_items.new('mesh.loop_select', 'LEFTMOUSE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', True)

###################################################################
# Fix for ALT+LEFTMOUSE (rotate) conflict in Weight Paint.
# Apply linear and radial gradients by holding additional SHIFT key
###################################################################

km = kc.keymaps['Weight Paint']             # Map Weight Paint

kmi = km.keymap_items.remove(km.keymap_items['paint.weight_gradient'])
kmi = km.keymap_items.new('paint.weight_gradient', 'LEFTMOUSE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'type', 'LINEAR')
kmi = km.keymap_items.new('paint.weight_gradient', 'LEFTMOUSE', 'PRESS', shift=True, ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'type', 'RADIAL')

############################################################################################
# Fix for ALT+LEFTMOUSE (rotate) conflict in 3D View (Select Object Menu randomly appearing)
# Activate Select Object Menu by pressing ALT+DOUBLE_CLICK instead
############################################################################################

km = kc.keymaps.new('3D View', space_type='VIEW_3D', region_type='WINDOW', modal=False)             # Map 3D View

for val in km.keymap_items:
    if val.idname == 'view3d.select':
        kmi = km.keymap_items.remove(km.keymap_items['view3d.select'])

kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'PRESS')
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', False)
kmi_props_setattr(kmi.properties, 'center', False)
kmi_props_setattr(kmi.properties, 'enumerate', False)
kmi_props_setattr(kmi.properties, 'object', False)
kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'PRESS', shift=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', True)
kmi_props_setattr(kmi.properties, 'center', False)
kmi_props_setattr(kmi.properties, 'enumerate', False)
kmi_props_setattr(kmi.properties, 'object', False)
kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'PRESS', ctrl=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', False)
kmi_props_setattr(kmi.properties, 'center', True)
kmi_props_setattr(kmi.properties, 'enumerate', False)
kmi_props_setattr(kmi.properties, 'object', True)
kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'DOUBLE_CLICK', alt=True)             # non-default
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', False)
kmi_props_setattr(kmi.properties, 'center', False)
kmi_props_setattr(kmi.properties, 'enumerate', True)
kmi_props_setattr(kmi.properties, 'object', False)
kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi_props_setattr(kmi.properties, 'extend', True)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', True)
kmi_props_setattr(kmi.properties, 'center', True)
kmi_props_setattr(kmi.properties, 'enumerate', False)
kmi_props_setattr(kmi.properties, 'object', False)
kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'PRESS', ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', False)
kmi_props_setattr(kmi.properties, 'center', True)
kmi_props_setattr(kmi.properties, 'enumerate', True)
kmi_props_setattr(kmi.properties, 'object', False)
kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'PRESS', shift=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', True)
kmi_props_setattr(kmi.properties, 'center', False)
kmi_props_setattr(kmi.properties, 'enumerate', True)
kmi_props_setattr(kmi.properties, 'object', False)
kmi = km.keymap_items.new('view3d.select', 'LEFTMOUSE', 'PRESS', shift=True, ctrl=True, alt=True)
kmi_props_setattr(kmi.properties, 'extend', False)
kmi_props_setattr(kmi.properties, 'deselect', False)
kmi_props_setattr(kmi.properties, 'toggle', True)
kmi_props_setattr(kmi.properties, 'center', True)
kmi_props_setattr(kmi.properties, 'enumerate', True)
kmi_props_setattr(kmi.properties, 'object', False)

###############
# save settings
###############
bpy.ops.wm.save_userpref()

######################################################
# v0.5 edit: workaround for context sensitive settings
######################################################

for window in bpy.context.window_manager.windows:
    screen = window.screen

    for area in screen.areas:
        if area.type == 'VIEW_3D':
            override = {'window': window, 'screen': screen, 'area': area}
            bpy.ops.screen.screen_full_area(override)                       # 3D Viewport screen/context override
            bpy.context.space_data.overlay.grid_scale = 0.01                # adjust grid scale to accommodate UE4 length adjustment 
            bpy.context.space_data.clip_end = 50000                         # adjust far camera clip plane
            bpy.ops.screen.back_to_previous()
            break