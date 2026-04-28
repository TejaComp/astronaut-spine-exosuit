import opensim as osim

model = osim.Model(r"C:\SpineSimulation\Models\gait2392_simbody.osim")
model.initSystem()

muscle_set = model.getMuscles()
print(f"\nTotal muscles: {muscle_set.getSize()}")
print("\nAll muscle names:")
print("-" * 30)

for i in range(muscle_set.getSize()):
    print(muscle_set.get(i).getName())