#### import the simple module from the paraview
from paraview.simple import *
from pathlib import Path
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
setupfoam = OpenFOAMReader(FileName='setup.foam')
setupfoam.MeshRegions = ['internalMesh']
setupfoam.MeshRegions.SelectAll()
setupfoam.CellArrays.SelectAll()



# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on setupfoam
setupfoam.CaseType = 'Decomposed Case'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1436, 756]


objFile = Path('geometry/building.obj')

#objFiles = Path('.').glob('constant/triSurface/building*.obj')
#
#if objFiles:
#    objFile = sorted(objFiles)[-1]

if objFile.exists():
    building5obj = WavefrontOBJReader( registrationName='building.obj', FileName=objFile.as_posix())
    building5objDisplay = Show(building5obj, renderView1, 'GeometryRepresentation')
    building5objDisplay.SetRepresentationType('Feature Edges')



# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# show data in view
setupfoamDisplay = Show(setupfoam, renderView1)
# trace defaults for the display properties.
setupfoamDisplay.ColorArrayName = ['POINTS', 'p']
setupfoamDisplay.LookupTable = pLUT

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
setupfoamDisplay.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(Input=setupfoam)

# Properties modified on extractBlock1
extractBlock1.Selectors = ['//boundary']

# show data in view
extractBlock1Display = Show(extractBlock1, renderView1)
# trace defaults for the display properties.
extractBlock1Display.ColorArrayName = ['POINTS', 'p']
extractBlock1Display.LookupTable = pLUT

# hide data in view
Hide(setupfoam, renderView1)

# show color bar/color legend
extractBlock1Display.SetScalarBarVisibility(renderView1, True)

#
extractBlock1Display.BackfaceRepresentation = 'Cull Frontface'

# set scalar coloring
ColorBy(extractBlock1Display, ('CELLS', 'T'))

# rescale color and/or opacity maps used to include current data range
extractBlock1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
extractBlock1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')

animationScene1.GoToLast()

#### saving camera placements for all active views

# current camera placement for renderView1

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
