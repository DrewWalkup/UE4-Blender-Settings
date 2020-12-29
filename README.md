## READ ME - UE4_Blender_Settings

This script was configured to help those familiar with UE4 and Maya to adapt to Blender more effectivly.

**Goals:**

1. 3D Viewport navigation (only) similar to Unreal Editor / Maya
2. Export settings for Unreal Engine

Default Blender shortcuts have been left mostly unaltered as this would hinder long-term use of the software as well as learning from tutorials.


## Implementation

**Blender 3D Viewport navigation - Pan, Orbit, and Zoom**

Unreal Editor / Maya - pan, orbit, and zoom viewport controls:
- **Alt + LMB + Drag** - Tumbles the viewport around a single pivot or point of interest.
- **Alt + RMB + Drag** - Dollies (zooms) the camera toward and away from a single pivot or point of interest.
- **Alt + MMB + Drag** - Tracks the camera left, right, up, and down in the direction of mouse movement.


**Game-style (WASD) navigation (already default in Blender, called "Walk Mode")**

Menu: View ‣ Navigation ‣ Walk Navigation
Hotkey: **Shift-F**

**Usage**
This navigation mode behaves similar to the first person navigation system available in most 3d world games nowadays. It works with a combination of keyboard keys **(WASD)** and mouse movement. By default the navigation is in the ‘free’ mode, with no gravity influence. You can toggle between gravity and free mode during the navigation **(Tab)**.

**Shortcuts**
- Move the camera forward/backward **(W / S)**.
- Strafe left/right **(A / D)**.
- Move down and up **(Q / E)** - only in ‘free’ mode.
- Alternate between ‘free’ and ‘gravity’ modes **(Tab)**.
- Change the movement speed: **WheelUp** to increase the movement speed. **WheelDown** to decrease the movement speed.


**Conflicting shortcuts that have been replaced**

**Loop Select**

Mode: Edit Mode

Original hotkey: **Alt-RMB**

New hotkey: **Alt-RMB(double-click)**

**Linear Weight Gradient**
Mode: Weight Paint
Original hotkey: **Alt-LMB**
New hotkey: **Alt-Shift-LMB**

**Radial Weight Gradient**
Mode: Weight Paint
Original hotkey: **Alt-Ctrl-LMB**
New hotkey: **Alt-Shift-Ctrl-LMB**

**Select Object Menu**
Mode: Object Mode
Original hotkey: **Alt-LMB**
New hotkey: **Alt-LMB(double-click)**


**Important setting in Unreal Engine**

Please note that this script assumes that you have Maya-style "Invert Middle Mouse Pan" option enabled in your Unreal Editor.
Most 3D applications use this type of navigation (or at least have it as an option). You can enable it in Unreal Editor by going to Edit -> Editor Preferences -> Viewports and then clicking "Invert Middle Mouse Pan" checkbox.

![UE4 Invert Middle Mouse Pan](/images/ue4_invert_mm_pan.png)


## Blender Installation

1. Reset all settings to default (optional):

![Blender Load Factory Settings](/images/blender_load_factory.png)

2. Switch from the *Outliner* to Text Editor, then click the "New" button:
*Important: The 3d Viewport must remain open if you want to implement world grid & clip plane adjustment*

![Blender Load Text Editor](/images/blender_text_editor.png)

3. Paste the code from UE4_blender_settings.py into the editor window and click "Run Script":

![Blender Run Script](/images/blender_run_script.png)

4. Switch from Text Editor back to Outliner:

5. Save everything in default startup file (optional)

![Blender Save Default Startup](/images/blender_save_default.png)

Enjoy!


## Credits

Unreal-friendly configuration for Blender

Version: 0.5
Last updated: December 22, 2020
Original Author: @mission (UE Forums)
Update to Blender 2.91: @dnwalkup (UE Forums)
