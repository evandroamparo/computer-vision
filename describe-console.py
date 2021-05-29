from describe import describe
import sys
# from describe import describe
# from translate import translate
from image_describer import describe_image

try:
    image_path = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <image path or URL>")

# description = describe(image_path)
# print(translate(description[0]))

print (describe_image(image_path))

# ####################################

