# generated using paraview version 5.8.0-412-ga47aa0a50c
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1455, 863]

from pathlib import Path
filename = Path(input("Enter image file name:"))
image_dir=Path.cwd()/'pictures'
if not image_dir.exists():
    image_dir.mkdir()
if not filename.suffix:
    filename = filename.with_suffix('.png')
image_file = image_dir/filename
print(image_file)

# save screenshot
SaveScreenshot(image_file.as_posix(), renderView1, ImageResolution=[2000, 1200])    
