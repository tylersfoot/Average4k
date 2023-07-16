# THIS PYTHON FILE IS FOR ME TO TEST STUF FOR AVERAGE4K

import moviepy.editor as mp
from PIL import Image
import os
import cv2
import numpy as np
import math
import shutil
Image.MAX_IMAGE_PIXELS = 10000000000000

doneVideo = True
doneFramesGenerate = True
doneFramesGroup1 = True
doneFinalImage = True

# ---------------------------------------------------------------- #
# '''

# load the video file
clip = mp.VideoFileClip("./data/badapple-original.mp4")

# make some variables
targetfps, targetheight = 60, 240
targetwidth = int(targetheight / 0.75)
calchorizframes = math.floor(32768 / targetwidth)
calcvertframes = math.floor(32768 / targetheight)
calcframes = calchorizframes * calcvertframes

# print some information
print(f'Original video frames: {clip.reader.nframes}')
print(f'Target fps: {targetfps}, width: {targetwidth}, height: {targetheight}')
print(
    f'Calculated max horizontal frames: {calchorizframes}, max vertical frames: {calcvertframes}, max total frames: {calcframes}')

if not doneVideo:
    # resize the video
    clip_resized = clip.set_fps(targetfps)
    clip_resized = clip_resized.resize(height=targetheight)

    # save the resized video and verify the fps
    clip_resized.write_videofile(f'./data/badapple-{targetheight}p-{targetfps}fps.mp4', fps=targetfps)
    clip_resized.close()
clip_verify = mp.VideoFileClip(f'./data/badapple-{targetheight}p-{targetfps}fps.mp4')
actualframes = clip_verify.reader.nframes
print(f'New video fps: {clip_verify.reader.nframes}, max fps: {calcframes}')

# close the clips
clip.close()
clip_verify.close()

# '''
# ---------------------------------------------------------------- #
# '''

print('Starting part 2...')
# load the video file
clip = mp.VideoFileClip(f'./data/badapple-{targetheight}p-{targetfps}fps.mp4')

if not doneFramesGenerate:
    # delete old frames and make new directory to store frames
    try:
        shutil.rmtree('./data/frames')
        os.makedirs('./data/frames')
    except:
        pass

    # iterate through all frames and save as image
    for i, frame in enumerate(clip.iter_frames()):
        image = mp.ImageClip(frame).save_frame('./data/frames/frame-{}.png'.format(i))
        print(f'\rStored frame {i}, {round((i / actualframes * 100), 2)}% Done', end='')
    print('\n')

# close the clip
clip.close()
print('Finished, closed clip')

# '''
# ---------------------------------------------------------------- #
# '''

print('Starting part 3...')
try:
    os.remove("./data/frames/temp.png")
except:
    pass
temp = cv2.imread('./data/frames/frame-0.png')
cv2.imwrite('./data/frames/temp.png', temp)
print('Rewrote temp.png')

if not doneFramesGroup1:
    # store the images in a list
    group_size = calchorizframes
    imgs = []
    for i in range(1, actualframes):
        imgs += [cv2.imread(f'./data/frames/frame-{i}.png')]
        print(
            f'\rAdded img {i} to list, {round((i/actualframes)*100, 2)}% Done', end='')
    print(f'Number of images: {len(imgs)}')

    # split the images into chunks
    imgs_chunk = []
    for i in range(0, len(imgs), group_size):
        imgs_chunk += [imgs[i:i + group_size]]
    print('Split images into chunks')

    # concatenate the resulting images and save each group
    for i in range(len(imgs_chunk)):
        temp = np.concatenate(imgs_chunk[i], axis=1)
        cv2.imwrite(f'./data/frames/group-{i + 1}.png', temp)
        print(f'\rConcatenated and saved group {i + 1} with width {temp.shape[1]}px, {round((i / len(imgs_chunk) * 100), 2)}% Done', end='')
    print('\n')

# '''
# ---------------------------------------------------------------- #
# '''
if not doneFinalImage:
    print('Removing images')
    for i in range(0, 200):
        try:
            os.remove(f'./data/frames/process-{i}.png')
            os.remove(f'./data/frames/finalimage.png')
            os.remove(f'./data/frames/temp.png')
        except:
            pass
    print('Removed images')

    # add black to last group to make it the same size
    img = Image.open('./data/frames/group-129.png') # open the image file
    img_array = np.array(img) # convert the image to a numpy array
    width, height = img_array.shape[1], img_array.shape[0] # get the width and height of the image
    black_section = np.zeros((height, 3520, 3), dtype=np.uint8) # create a black section with the desired size (32640 - 29120)
    result = np.hstack((img_array, black_section)) # stack the image and the black section horizontally
    result_img = Image.fromarray(result) # convert the result back to an image
    result_img.save('./data/frames/group-129.png') # save the result


    # concatenate all groups
    final_image = cv2.imread('./data/frames/group-1.png')
    for i in range(1, 130):
        group_image = cv2.imread(f'./data/frames/group-{i}.png')
        final_image = np.concatenate((final_image, group_image), axis=0)
        # cv2.imwrite(f'./data/frames/process-{i + 1}.png', final_image1)
        print(f'\rConcatenated and saved group {i} with width {final_image.shape[1]}px, {round((i/129) * 100, 2)}% Done', end='')
    print('\n')

    # save the final image
    cv2.imwrite(f'./data/frames/finalimage.png', final_image)
    print('Saved final image')
# '''

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

# '''
frames = 13147
frame_height = 240
frame_width = 320
image_name = "BA.png"
frame_name = "BA"
# xml_directory = 'C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/bad apple/bad apple/mod/BA.xml'
frames = frames-13100
for x in range(1, 130):
    lines = [f'<TextureAtlas imagePath="group-{x}">\n']
    xml_directory = f'C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/bad apple/bad apple/mod/BA{x}.xml'
    for i in range(1, 103):
        xx = (i - 1) * frame_width
        print(f'i{i} | group{x} | x{xx}')
        lines.append(f'    <SubTexture name="{frame_name}{str(i).zfill(4)}" x="{xx}" y="0" width="{frame_width}" height="{frame_height}"/>\n')
    lines.append('</TextureAtlas>')
    with open(xml_directory, 'w') as f:
        f.writelines(lines)
print(f'Finished writing to {xml_directory}')

'''
img = Image.open('C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/bad apple/bad apple/mod/finalimage.png') # open the image file
print(1)
img_array = np.array(img) # convert the image to a numpy array
print(2)
cropped_img = img_array[:5000, :] # crop the image to 10000x10000 px by slicing the numpy array
print(3)
cropped_img = Image.fromarray(cropped_img) # convert the cropped numpy array back to an image
print(4)
cropped_img.save('C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/bad apple/bad apple/mod/BA.png') # save the cropped image
print(5)
'''

'''
# trims n pixels from the left and right of the image
try:
    os.remove("C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/bad apple/bad apple/mod/BA.png")
    print('removed img')
except:
    pass
img = cv2.imread('./data/BA.png')
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
'''
