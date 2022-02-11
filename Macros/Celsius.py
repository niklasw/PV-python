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
calculator2 = Calculator(Input=setupfoam)

# Properties modified on calculator1
calculator1.ResultArrayName = 'C'
calculator1.Function = 'T-273.15'
RenameSource('Celsius', calculator1)

calculator2.ResultArrayName = 'cC'
calculator2.AttributeType = 'Cell Data'
calculator2.Function = 'T-273.15'
RenameSource('CelsiusC', calculator2)


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1507, 789]

# get layout
layout1 = GetLayout()

# show data in view
calculator1Display = Show(calculator2, renderView1, 'GeometryRepresentation')

