import cadquery as cq

# Parametry
body_diameter = 24.0
body_length = 85.0
nozzle_diameter = 5.4
nozzle_length = 21.25
trigger_diameter = 3.0
trigger_length = 20.0
mount_hole_distance = 24.0
mount_hole_diameter = 3.2

# Model
body = cq.Workplane("XY").circle(body_diameter / 2).extrude(body_length)
offset = mount_hole_distance / 2
body = body.faces(">Z").workplane().pushPoints([(-offset, 0), (offset, 0)]).hole(mount_hole_diameter)
nozzle = cq.Workplane("XY").workplane(offset=body_length).circle(nozzle_diameter / 2).extrude(nozzle_length)
trigger = cq.Workplane("XZ").workplane(offset=-body_diameter / 2).center(0, 5).circle(trigger_diameter / 2).extrude(trigger_length)
model = body.union(nozzle).union(trigger)

# Eksport
cq.exporters.export(model, 'hpa_engine_model.step')
