from beach import Beach
from wave import Wave
from sand import Sand

beach = Beach("Kuta Beach", "Indonesia")
wave = Wave(2, 28)
sand = Sand("white", "fine")

print(beach)
print(beach.describe())
print(wave.splash())
print(sand.feel())
