# pillow_examples.py

# Pillow is used for image processing in Python
# Pillow is the modern version of PIL (Python Imaging Library)

# install:
# pip install Pillow


from PIL import Image, ImageFilter, ImageOps, ImageDraw


# ==========================================================
# OPEN IMAGE
# ==========================================================

# Image.open(path)
# opens image from given path

img = Image.open("photo.jpg")

# show image using system image viewer

img.show()


print("\n--------------------\n")


# ==========================================================
# IMAGE INFORMATION
# ==========================================================

# size returns:
# (width, height)

print(img.size)

# format returns image format

print(img.format)

# mode returns color mode

print(img.mode)

# common modes:
#
# RGB  -> red green blue
# RGBA -> RGB + transparency
# L    -> grayscale


print("\n--------------------\n")


# ==========================================================
# RESIZE IMAGE
# ==========================================================

# resize((width, height))
# creates resized copy of image

resized = img.resize((300, 300))

# save resized image

resized.save("resized.jpg")


print("\n--------------------\n")


# ==========================================================
# CROP IMAGE
# ==========================================================

# crop((left, top, right, bottom))

# left   -> starting x position
# top    -> starting y position
# right  -> ending x position
# bottom -> ending y position

cropped = img.crop((100, 100, 400, 400))

cropped.save("cropped.jpg")


print("\n--------------------\n")


# ==========================================================
# ROTATE IMAGE
# ==========================================================

# rotate(angle)
# rotates image in degrees

rotated = img.rotate(90)

rotated.save("rotated.jpg")


print("\n--------------------\n")


# ==========================================================
# CONVERT IMAGE MODE
# ==========================================================

# convert("L")
# converts image to grayscale

gray = img.convert("L")

gray.save("gray.jpg")


# convert("RGB")
# converts image to RGB mode

rgb = img.convert("RGB")

rgb.save("rgb.jpg")


print("\n--------------------\n")


# ==========================================================
# FLIP IMAGE
# ==========================================================

# mirror() flips horizontally

mirror = ImageOps.mirror(img)

mirror.save("mirror.jpg")


# flip() flips vertically

flip = ImageOps.flip(img)

flip.save("flip.jpg")


print("\n--------------------\n")


# ==========================================================
# THUMBNAIL
# ==========================================================

# thumbnail() resizes image while keeping aspect ratio

thumbnail_img = img.copy()

thumbnail_img.thumbnail((200, 200))

thumbnail_img.save("thumbnail.jpg")


print("\n--------------------\n")


# ==========================================================
# APPLY FILTERS
# ==========================================================

# filter() applies image effects

# blur filter

blur = img.filter(ImageFilter.BLUR)

blur.save("blur.jpg")


# sharpen filter

sharp = img.filter(ImageFilter.SHARPEN)

sharp.save("sharp.jpg")


# detail enhancement

detail = img.filter(ImageFilter.DETAIL)

detail.save("detail.jpg")


print("\n--------------------\n")


# ==========================================================
# DRAW TEXT ON IMAGE
# ==========================================================

# copy image so original image remains unchanged

draw_img = img.copy()

# ImageDraw.Draw(image)
# creates drawing object

draw = ImageDraw.Draw(draw_img)

# text((x, y), text, fill=color)

draw.text(
    (50, 50),
    "Hello Pillow",
    fill="white"
)

draw_img.save("text_image.jpg")


print("\n--------------------\n")


# ==========================================================
# CREATE NEW IMAGE
# ==========================================================

# Image.new(mode, size, color)

new_img = Image.new(
    "RGB",
    (500, 500),
    color="blue"
)

new_img.save("blue.jpg")


print("\n--------------------\n")


# ==========================================================
# FORMAT CONVERSION
# ==========================================================

# save with different extension
# automatically converts format

img.save("converted.png")


print("\n--------------------\n")


# ==========================================================
# COPY IMAGE
# ==========================================================

# copy() creates duplicate image object

copy_img = img.copy()

copy_img.save("copy.jpg")


print("\n--------------------\n")


# ==========================================================
# IMAGE WIDTH AND HEIGHT
# ==========================================================

width, height = img.size

print(width)

print(height)


print("\n--------------------\n")


# ==========================================================
# PRACTICAL EXAMPLE
# ==========================================================

# create profile thumbnail

profile = Image.open("photo.jpg")

profile.thumbnail((150, 150))

profile.save("profile_thumbnail.jpg")


print("Profile thumbnail created")


print("\n--------------------\n")


# ==========================================================
# PRACTICAL EXAMPLE
# ==========================================================

# add watermark text

watermark_img = img.copy()

draw = ImageDraw.Draw(watermark_img)

draw.text(
    (20, 20),
    "My Watermark",
    fill="white"
)

watermark_img.save("watermark.jpg")


print("Watermark added")


print("\n--------------------\n")


# ==========================================================
# SUMMARY
# ==========================================================

# Image.open(path)
# opens image
#
# img.show()
# displays image
#
# img.size
# returns (width, height)
#
# img.resize()
# resizes image
#
# img.crop()
# crops image
#
# img.rotate()
# rotates image
#
# img.convert()
# changes image mode
#
# ImageOps.mirror()
# horizontal flip
#
# ImageOps.flip()
# vertical flip
#
# img.thumbnail()
# creates thumbnail
#
# img.filter()
# applies filters
#
# ImageDraw.Draw()
# draw text/shapes
#
# Image.new()
# creates new image
#
# img.save()
# saves image

print("done")