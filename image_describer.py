from describe import describe
from translate import translate

def describe_image(image_path):
    try:
        description = describe(image_path)
        translation = translate(description[0])
        return (translation , description[1])
    except:
        return "Não consegui decifrar"


# ####################################

