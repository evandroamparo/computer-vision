import sys
from describe import describe
from translate import translate

try:
    image_path = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <image path or URL>")

description = describe(image_path)
print(translate(description[0]))

# ####################################

