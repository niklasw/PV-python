# generated using paraview version 5.8.0-412-ga47aa0a50c
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
setupfoam = GetActiveSource() #FindSource('setup.foam')

# create a new 'Calculator'
calculator1 = Calculator(Input=setupfoam)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'mag(U)'
calculator1.Function = 'mag(U)'
RenameSource('mag_U', calculator1)

