import random

flowers = [
    "🌸", "🌼", "🌻", "🌺", "🌷", "🌹"
]

# Generate a bunch of random flowers
for _ in range(10):  # Number of flowers
    print("  " * random.randint(0, 10) + random.choice(flowers))  # Random positioning

print("\nEnjoy your digital flower garden! 🌿🌺")

