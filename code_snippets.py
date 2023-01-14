# This code snippet writes a .xml file for an image asusming a consistent frame size, and that the frames are joined horizontally in the image
frames = 51 # number of frames, aka image_width/frame_width
frame_height = 480 # height of each frame, aka the image_height
frame_width = 640 # width of each frame
image_name = "name.png" # name of the image (must be in same directory as .xml file)
frame_name = "frame"
# directory and name of the xml file
xml_directory = 'C:/Program Files (x86)/Steam/steamapps/common/Average4k/assets/charts/test pack/example song/mod/name.xml'
lines = [f'<TextureAtlas imagePath="{image_name}">\n'] # adds the opening line
for i in range(1, frames+1):
    # adds a line for each frame, starting at 1
    # name: the frame_name + the frame number (i), filled in with zeroes to 4 digits
    # x: the starting x position of the frame, which counts up by the frame width, starting at 0 (i-1)
    # y: the starting y position of the frame, which is always 0, as the frame's position is calculated at the bottom left corner
    # width/height: the width and height of the frame, which is always the same
    lines.append(f'    <SubTexture name="{frame_name}{str(i).zfill(4)}" x="{(i-1)*frame_width}" y="0" width="{frame_width}" height="{frame_height}"/>\n')
    print(f'Wrote line {i}', end='\r')
lines.append('</TextureAtlas>') # adds the closing line
with open(xml_directory, 'w') as f:
    f.writelines(lines)
print(f'Finished writing to {xml_directory}')
