# THIS PYTHON FILE IS FOR ME TO TEST STUF FOR AVERAGE4K

import moviepy.editor as mp
from PIL import Image
import os
import cv2
import numpy as np

'''
# Load the video file
clip = mp.VideoFileClip("./data/badapple-original.mp4")
# Set the new frame rate
clip_15fps = clip.set_fps(2)
# Resize the video
clip_resized = clip_15fps.resize(height=240)
# Save the new video
clip_resized.write_videofile("./data/badapple-240p2fps.mp4", fps=5)
'''

'''
# Load the video file
clip = mp.VideoFileClip("./data/badapple-480p5fps.mp4")
# Create a directory to save the frames
if not os.path.exists("./data/frames3"):
    os.makedirs("./data/frames3")
# Iterate through all frames
for i, frame in enumerate(clip.iter_frames()):
    # Save the frame as an image file
    image = mp.ImageClip(frame).save_frame("./data/frames3/frame-{}.png".format(i))
'''

'''
try:
    os.remove("./data/frames4/temp.png")
except:
    pass
temp = cv2.imread('./data/frames4/frame-0.png')
cv2.imwrite('./data/frames4/temp.png', temp)

# Split the images into smaller groups
group_size = 100
imgs = [cv2.imread(f'./data/frames4/frame-{i}.png') for i in range(1, 1086)]
print(f'Number of images: {len(imgs)}')

# split the images into chunks
imgs_chunk = [imgs[i:i + group_size] for i in range(0, len(imgs), group_size)]

# Concatenate the resulting images and save each group
for i in range(len(imgs_chunk)):
    temp = np.concatenate(imgs_chunk[i], axis=1)
    cv2.imwrite(f'./data/frames4/group-{i + 1}.png', temp)
    print(f'Concatenated and saved group {i + 1} with width: {temp.shape[1]}')
'''

'''
# Concatenate all groups
final_image = cv2.imread('./data/frames2/group_1.png')
for i in range(2, len(imgs_chunk) + 1):
    print(f'opened group: {i} | ', end='')
    group_image = cv2.imread(f'./data/frames2/group_{i}.png')
    final_image = np.concatenate((final_image, group_image), axis=1)
    cv2.imwrite(f'./data/frames2/process_{i + 1}.png', final_image)
    print(f'width aft:{final_image.shape[1]} | ')

# Save the final image
cv2.imwrite('./data/frames2/temp.png', final_image)
print('done2')
'''



'''
for i in range(1, 11, 2):
    print(i)
    img1 = cv2.imread(f'./data/frames4/group-{i}.png')
    img2 = cv2.imread(f'./data/frames4/group-{i+1}.png')
    img3 = np.concatenate((img1, img2), axis=1)
    cv2.imwrite(f'./data/frames4/h-{i}.png', img3)
'''
# group-11 left over
'''
for i in range(1, 11, 4):
    print(i)
    img1 = cv2.imread(f'./data/frames4/h-{i}.png')
    img2 = cv2.imread(f'./data/frames4/h-{i+2}.png')
    img3 = np.concatenate((img1, img2), axis=1)
    cv2.imwrite(f'./data/frames4/i-{i}.png', img3)
'''
# h-9 left over
'''
for i in range(1, 33, 8):
    print(i)
    img1 = cv2.imread(f'./data/frames4/i-{i}.png')
    img2 = cv2.imread(f'./data/frames4/i-{i+4}.png')
    img3 = np.concatenate((img1, img2), axis=1)
    print(f'width aft:{img3.shape[1]} | ')
    cv2.imwrite(f'./data/frames2/k-{i}.png', img3)
'''

# print(1)
# img1 = cv2.imread(f'./data/frames4/i-1.png')
# img2 = cv2.imread(f'./data/frames4/i-5.png')
# img3 = np.concatenate((img1, img2), axis=1)
# cv2.imwrite(f'./data/frames4/z-1.png', img3)
'''
print(2)
img1 = cv2.imread(f'./data/frames4/z-1.png')
img2 = cv2.imread(f'./data/frames4/h-9.png')
img3 = np.concatenate((img1, img2), axis=1)
cv2.imwrite(f'./data/frames4/z-2.png', img3)
print(3)
img1 = cv2.imread(f'./data/frames4/z-2.png')
img2 = cv2.imread(f'./data/frames4/group-11.png')
img3 = np.concatenate((img1, img2), axis=1)
cv2.imwrite(f'./data/frames4/z-3.png', img3)
print(4)
'''

frames = 51
frame_height = 480
frame_width = 640
image_name = "BA.png"
frame_name = "BA"
xml_directory = 'C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/bad apple/bad apple/mod/BA.xml'
lines = [f'<TextureAtlas imagePath="{image_name}">\n']
for i in range(1, frames+1):
    lines.append(f'    <SubTexture name="{frame_name}{str(i).zfill(4)}" x="{(i-1)*frame_width}" y="0" width="{frame_width}" height="{frame_height}"/>\n')
    print(f'Wrote line {i}', end='\r')
lines.append('</TextureAtlas>')
with open(xml_directory, 'w') as f:
    f.writelines(lines)
print(f'Finished writing to {xml_directory}')

# trims n pixels from the left and right of the image
try:
    os.remove("C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/bad apple/bad apple/mod/BA.png")
    print('removed img')
except:
    pass
img = cv2.imread('BA.png')
print('loaded img')
width = 512000
n = 4480
n2 = (width - n) - (frames*640) - 128
# remove n pixels from the left
img = img[:, n:]
print('cut left')
# remove n2 pixels from the right
img = img[:, :-n2]
print('cut right')
cv2.imwrite('C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/bad apple/bad apple/mod/BA.png', img)
print('saved img')