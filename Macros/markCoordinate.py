# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
import re
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

failCount = 0

def getCoordinate(message='Input 3D coordinate'):
    global failCount
    try:
        inputString = input(message)
        coordString = inputString.strip(' ()')
    except:
        return None
    try:
        coords = [float(v) for v in re.split(',|\s|\t', coordString)]
        return coords
    except:
        failCount += 1
        if failCount < 3:
            return getCoordinate(message='Could not read. Try again')
        else:
            return [0,0,0]


coordinate = getCoordinate()

if coordinate:
    # create a new 'Sphere'
    sphere1 = Sphere(registrationName='Sphere1')
    
    # find source
    setupfoam = FindSource('setup.foam')
    
    # Properties modified on sphere1
    sphere1.Center = coordinate
    sphere1.Radius = 0.2
    
    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    
    # show data in view
    sphere1Display = Show(sphere1, renderView1, 'GeometryRepresentation')
    
    # trace defaults for the display properties.
    sphere1Display.Representation = 'Surface'
    sphere1Display.ColorArrayName = [None, '']
    sphere1Display.SelectTCoordArray = 'None'
    sphere1Display.SelectNormalArray = 'Normals'
    sphere1Display.SelectTangentArray = 'None'
    sphere1Display.OSPRayScaleArray = 'Normals'
    sphere1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    sphere1Display.SelectOrientationVectors = 'None'
    sphere1Display.ScaleFactor = 0.04000015258789063
    sphere1Display.SelectScaleArray = 'None'
    sphere1Display.GlyphType = 'Arrow'
    sphere1Display.GlyphTableIndexArray = 'None'
    sphere1Display.GaussianRadius = 0.002000007629394531
    sphere1Display.SetScaleArray = ['POINTS', 'Normals']
    sphere1Display.ScaleTransferFunction = 'PiecewiseFunction'
    sphere1Display.OpacityArray = ['POINTS', 'Normals']
    sphere1Display.OpacityTransferFunction = 'PiecewiseFunction'
    sphere1Display.DataAxesGrid = 'GridAxesRepresentation'
    sphere1Display.PolarAxes = 'PolarAxesRepresentation'

