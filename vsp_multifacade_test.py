import openvsp_config
openvsp_config.LOAD_MULTI_FACADE = True

import openvsp
import degen_geom as dg

# VSP file containing single
vsp_file = "rect_wing.vsp3"

# Create a private vsp server instance
vsp_model = openvsp.vsp_servers.start_vsp_instance("openaerostruct")

# This is how you would access an already created instance in another location in the code
# vsp_model = openvsp.get_instance("openaerostruct")

# Read in file
vsp_model.ReadVSPFile(vsp_file)

# Create a degengeom set that will have our VLM surfaces in it
vsp_model.SetAnalysisInputDefaults("DegenGeom")
vsp_model.SetIntAnalysisInput("DegenGeom", "WriteCSVFlag", [0], 0)
vsp_model.SetIntAnalysisInput("DegenGeom", "WriteMFileFlag", [0], 0)

# Export all degengeoms to a list
degen_results_id = vsp_model.ExecAnalysis("DegenGeom")

# Get all of the degen geom results managers ids
degen_ids = vsp_model.GetStringResults(degen_results_id, "Degen_DegenGeoms")

# Create a list of all degen surfaces
degens = []
# loop over all degen objects
for degen_id in degen_ids:
    res = vsp_model.parse_results_object(degen_id)
    degen_obj = dg.DegenGeom(res)

    # Create a degengeom object for the cambersurface
    plate_ids = vsp_model.GetStringResults(degen_id, "plates")
    for plate_id in plate_ids:
        res = vsp_model.parse_results_object(plate_id)
        degen_obj.plates.append(dg.DegenPlate(res))

    degens.append(degen_obj)