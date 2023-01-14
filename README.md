# Average4k Notes

This is a collection of notes and observations about Average4k that I've observed.
Some things in here may go into more detail than the official documentation, but some things will also be missing.
Feel free to let me know if you have any questions, corrections, or suggestions by contacting me, preferrably on Discord: tylersfoot#8888.

## Sprites:

- Sprites can be still images or animated with a `.xml` file, shown in the next section.
- Lua code snippet for loading a sprite in `mod.lua`:

```lua
function create()
    -- path: path to the sprite relative to the mod.lua folder, without the extension
    -- name: name of the sprite
    -- x, y: position of the sprite; 0, 0 is the top left corner of the screen
    -- the sprite position is based on the top left corner of the sprite aswell
	createSprite("path", "name", 0, 0)
end
```

- You can use `setSpriteProperty` to change different aspects of the sprite:

| Property     | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| `loop`       | true/false, sets whether to loop the animation or not                     |
| `fps`        | Frames per second to fun the animation at                                 |
| `anim`       | Sets the current animation name to play                                   |
| `sparrow`    | A path to load the spritesheet, relative to mod.lua, without extension    |
| `animFinish` | Calls a funtion when the animation is finished, only when `loop` is false |
| `rageMin`    | The minimum frame to play                                                 |
| `rageMax`    | The maximum frame to play                                                 |
| `anchor`     | Anchors this sprite to another sprite                                     |

- Lua code snippet for loading an animated sprite in `mod.lua`:

```lua
function create()
	createSprite("path", "name", 0, 0) -- loads sprite
	setSpriteProperty("name", "sparrow", "BA") -- loads animation spritesheet
	setSpriteProperty("name", "loop", "true") -- loop animation
	setSpriteProperty("name", "fps", "60") -- run at 60fps
	setSpriteProperty("name", "anim", "anim1") -- play the 'anim1' animation
	setSpriteProperty("name", "animFinish", "func_name") -- calls 'func_name' when the animation is finished 
end
```

- Regarding animations, not including the image or having an incorrect directory to the image results in a black image displayed.
- Images wider than 32768px cannot be loaded - this has the same result as above, a black image displayed.
- Interestingly, both of the above scenarios still result in an animation being played; it just results in each frame being black.

### `.xml` Files:

- XML Files are used to define animation frames for sprites.
- `.xml` file format template:

```xml
<TextureAtlas imagePath="name.png">
    <SubTexture name="name0001" x="0" y="0" width="640" height="480"/>
    <SubTexture name="name0002" x="640" y="0" width="640" height="480"/>
    ...
</TextureAtlas>
```

- `name` must have a 4-digit number after it; it should be counting up from 1, including zeroes to fill the 4 digits, like so: 0001, 0002.. 0998, 0999
- Each parameter must have quotation marks (" ") surrounding the values, like `x="640"`
- Python code that I used to generate an XML file:

```py
# This code snippet writes a .xml file for an image assuming a consistent frame size, and that the frames are joined horizontally in the image
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
```
