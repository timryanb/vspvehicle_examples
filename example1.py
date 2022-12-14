import openvsp as vsp

"""
This is a simple script to show how to use the VSPVehicle class.
This class is a light wrapper of the openvsp API that allows users to 
interact with multiple independent vehicle instances in the same Python script.
"""

# Create first vehicle instance
veh1 = vsp.VSPVehicle()
# Create first vehicle instance
veh2 = vsp.VSPVehicle()
# Add a wing to vehicle instance 1
veh1.AddGeom("WING")
# Get the current geoms loaded in each vehicle
geoms1 = veh1.FindGeoms()
geoms2 = veh2.FindGeoms()
# Print number of geoms, veh1 should have 1, veh2 should have zero
print(f"Number of geoms currently in veh1: {len(geoms1)}")
print(f"Number of geoms currently in veh2: {len(geoms2)}")
# Read in 777 model to veh2 instance
veh2.ReadVSPFile("Boeing_777-9x_ref.vsp3")
# Update geoms list
geoms1 = veh1.FindGeoms()
geoms2 = veh2.FindGeoms()
# Print number of geoms, veh1 should still have 1, veh2 should now have 15
print(f"Number of geoms currently in veh1: {len(geoms1)}")
print(f"Number of geoms currently in veh2: {len(geoms2)}")
# Write out some files from each instance
veh1.WriteVSPFile("Wing.vsp3")
veh2.ExportFile("B777.p3d", vsp.SET_ALL, vsp.EXPORT_PLOT3D)
# Delete all geoms in veh2
veh2.ClearVSPModel()
# Update geoms list
geoms1 = veh1.FindGeoms()
geoms2 = veh2.FindGeoms()
# Print number of geoms, veh1 should still have 1, veh2 now have 0 again
print(f"Number of geoms currently in veh1: {len(geoms1)}")
print(f"Number of geoms currently in veh2: {len(geoms2)}")
