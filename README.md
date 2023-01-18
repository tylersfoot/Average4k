# Average4k Notes - Update b12 - 1/14/23

This is a collection of notes and observations about Average4k that I've observed.
Some things in here may go into more detail than the official documentation, but some things will also be missing.
Feel free to let me know if you have any questions, corrections, or suggestions by contacting me, preferrably on Discord: tylersfoot#8888.

## Information/Links
- [Community GitHub Wiki](https://github.com/WizardMantis441/a4k-docs/wiki)
- [Kade's Documentation](https://kadedev.github.io/Avg4KModDocs/#/)
- [Official Lua Documentation](https://www.lua.org/manual)
- [Average4k Community Fandom](https://average4k.fandom.com/wiki/Average4k_Wiki)
- [Wishlist the game on Steam](https://store.steampowered.com/app/1828580/Average4k)
- [Development Trello Page](https://trello.com/b/2CVDM9k9/average4k-trello)
- [Average4k Discord Server](https://discord.gg/p65upz2NNJ)

# Modcharting/Song Packs
### Song Pack Directory
- Below is an example of a song pack directory.
```
└── pack name/
    ├── banner.png
    ├── pack.meta
    ├── song1/
    │   └── ...
    ├── song2/
    │   └── ...
    └── song3/
        └── ...
```
- `pack.meta` is a small file that contains information about the pack:
  - `banner` - The path of the banner image for your pack.
    - Any other size will be scaled to fit. For example, a square image will be vertically squished.
    - version b13 or higher:
      - The "recommended" size is 300x75. By default, all packs DO show as 300x75, so no stretching will occur.
      - However, if the user has enough packs to have a scrollbar, the banners will be squashed to 275x75.
      - Since there is nothing you can do about this at the moment, I recommend making your banner 300x75.
      - Unlike earlier, there is no need to make the banner transparent as it will no longer cut off any pixels on the right.
    - version b12 or lower:
      - The "recommended" size is 275x75. However, in my testing, I found that the best possible banner size is: 300x73
        - Using this, the banner's y-axis will NOT be streched or cut off at all.
        - For the x-axis, make the banner's content only 275px wide with 25px of transparency on the right.
        - Basically, banner content: 275x73 | transparent border: 25x73 on the right side.
        - Note that no matter the size, there will be a miniscule amount of horizontal stretching (2px).
  - `packName` - The name of the song pack. This will show up in the workshop.
  - `showName` - Determines whether the `packName` will be shown on top of the banner. Should be `false` if your banner has the name on it.
- Example below:
```meta
banner: banner.png
packName: Super Awesome Pack v1.0
showName: true
```

### Modchart Directory
- Below is an example of a basic directory for a modchart.
```
└── song/
    ├── song.sm
    ├── song.wav
    ├── bg.png 
    └── mod/
        ├── mod.lua
        ├── spritesheet.png
        └── spritesheet.xml
```

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

# Skinning (will revamp in b13)
- Skins visually change different aspects of the game, most notably the notes/receptors and the menu.
- Below is a basic tutorial on how to create a skin in Average4k.
### Getting Started
- To create a skin, navigate to the Average4k folder from steam (Average4k->Settings->Manage->Browse local files), then go to `assets\noteskin`. In here is where all of the skins (including the default ones) are located.
- From here, make a copy of one of the default skins, and rename it to whatever you like. You can now change all of the note images and edit the `config.skin` file, explained below.
- Here is an example directory of my personal skin folder:
```
└── tylersfoot skin v1.2/
    ├── config.skin
    ├── hold.png
    ├── holdend.png
    ├── idfk.png
    ├── lit.png
    ├── out.png
    ├── receptor.png
    └── menu/
        ├── Gameplay/
        │   ├── crown.png
        │   ├── leftBorder.png
        │   ├── leftGraid.png
        │   ├── rightGraid.png
        │   ├── underway.png
        │   └── underwayBorder.png
        ├── Menu/
        │   ├── avg4k.png
        │   ├── bg.png
        │   ├── border.png
        │   ├── close.png
        │   ├── darkmodebg.png
        │   ├── genericAvatar.png
        │   ├── majorerroricon.png
        │   ├── minorerroricon.png
        │   ├── roundedbutton_ok.png
        │   ├── TheWhitePixel.png
        │   ├── Container/
        │   │   ├── dropdownarrow.png
        │   │   └── scroll_arrow.png
        │   └── MainMenu/
        │       ├── Multi/
        │       │   ├── carat.png
        │       │   ├── checkbox.png
        │       │   ├── filtercontainer.png
        │       │   ├── lobbycontainer.png
        │       │   ├── lobbysearch.png
        │       │   ├── maincontainer.png
        │       │   ├── sortby_dropdown.png
        │       │   └── sortbycontainer.png
        │       ├── Settings/
        │       │   ├── dropdown.png
        │       │   ├── dropdownItem.png
        │       │   ├── endOfDropdown.png
        │       │   ├── maincontainer.png
        │       │   ├── previewicon.png
        │       │   ├── searchcontainer.png
        │       │   ├── settingssearch.png
        │       │   ├── toggle.png
        │       │   ├── toggle_bg.png
        │       │   └── typeinputcontainer.png
        │       └── Solo/
        │           ├── diffSelectArrow.png
        │           ├── leftcontainer.png
        │           ├── maincontainer.png
        │           ├── maincontainer_solo.png
        │           ├── packscontainer.png
        │           ├── packsearchbar.png
        │           ├── songcontainer.png
        │           ├── wheelContainer.png
        │           └── wheelTop.png
        ├── Music/
        │   ├── MenuTheme.meta
        │   └── MenuTheme.wav
        └── Start/
            ├── KadeDevTeam.png
            └── MiscLogo.png
```
### `config.skin` File:

This file holds some configuration options to change when creating your skin.

`rotate` (true/false) - Rotates the sprite's orientation depending on it's direction; Useful for arrow skins.

`shrink` (true/false) - Shrinks the receptors depending on if they are being held or not.

`bounce` (true/false) - Makes the combo and judgement text bounce when a note is played.

`disableQuant` (true/false) - Disables the note color quantization. If set to true, specify the image file to use for each lane. An example is shown below, where the directions specify the notes and the text following it specifies the image file name, without the extension.
```
left: image1
down: image2
up: image2
right: image1
```

### Skinning the menu:

The final option in `config.skin` is `path`.

When set to `path: default` , the skin will take the default menu elements from the base game. In order to change the menu elements, follow the steps below:

1. In the `assets` folder, copy the entire `skinDefaults` folder.
2. Paste the folder in your custom skin folder, and rename it to whatever you want (I'll use `skinAssets` for the sake of this tutorial)
3. In `config.skin`, change the path to the name of the folder (`path: skinAssets`)
4. Skin the menu! All changes made to the images in this folder will apply to your game when your skin is selected.


# Update Changelog

### b11 - 06/12/2022
Features:
- Added a leaderboard
- Added support for importing .osz, .qp, and stepamia pack folders
- Added drag and drop support for importing songs

Fixes:
- Minor fixes

### b11.1 - 08/24/2022
Features:
- Added wine support (technically you can play on a steamdeck now)
- Added new multiplayer menu

Fixes:
- Minor fixes 

### b11.2.2 - 09/06/2022
Features:
- Added StealthOpacity, StealthWhite, StealthReceptorOpacity to modchart docs
- Added a "create lobby" button and textbox as a temporary way to create custom lobbies

Fixes:
- Multiplayer leaderboard no longer breaks when someone leaves midgame
- Multiplayer now tells the host more detailed information on who has the chart
- Multiplayer now tells the new host they're the host midgame if the old one leaves
- Chat now resets every time you join a lobby
- Fixed a memory leak when removing a song's audio from the games memory
- Fixed being able to toggle options from the select song screen
- Fixed a bug when refreshing the pack list, it would still act like there is a scroll bar even though there isn't
- Fixed a bug where you could only open the leaderboard once for a song.
- Fixed a bug where when selecting a multiplayer lobby, the game would sometimes break, and you'd have to go to settings and back to the multiplayer tab to fix it
- Properly orientated the download percentage
- removed herobrine

### b12 - 10/02/2022
Features:
- Added .ssc support
- Added lua error reporting
- Added 64th quantized notes
- Added song position bar 
- Added a new bar skin

Fixes:
- scrolling on the wheel now lets you go up to the bottom

Miscellaneous:
- Removed support uploading individual songs to the Workshop; you can now only upload packs

### b13 - WIP
Features:
- Added a "More Info" panel to the song selection screen. Accessible by using "tab", replacing the leaderboard with a better one
- Added "linear" as an easing option in "activateMod" functions
- Added 4 new Steam Achievements
- Added a new folder into the skin directory called "judgements" which now allow you to customize the judgement and combo counter texts
- Added the "soundPath" property to skins to allow you to set a custom sound path (like changing menu elements). Currently, the sounds are "hitSound.wav" and "beatTick.wav"
- Added back the "Resolution" setting and fixed resolutions, so they actually work correctly instead of breaking the game
- Added "config.scrollSpeed" which returns the current user scrollspeed
- Added "config.displayWidth" and "config.displayHeight" which returns the current resolution set by the user (note: the gameplay field is stretched from 1280x720 to fill up every other resolution)
- Added mines
- Added fakes
- Added `setModProperty`, `getModProperty`, `getSpriteMod`, `setAutoEnd`, and `setAutoEnd` to lua api
- Added `key_pressed`, `key_released`, and `editor_scroll` to the lua api

Fixes:
- Fixed multiple issues with leaderboards, including separate diffs for leaderboards, submitting completely different charts under a leaderboard, and some other misc issues.
- "activateMod" functions now also complete instantly if their length is 0
- Hitsounds now stack
- Editor no longer crashes that much (including the mod editor)
- Editor is no longer a lag mess (as much as before)
- Fixed a bug where a 0 offset chart would result in a bpm segment being found as a bpm of 120 (not having the correct bpm meant the notes were not correct)
- Fixed an issue where closing the game would hang (it no longer does this)
- Fixed an issue where hold notes would prematurely end before they should have
- Fixed pack banner scaling/sizing

Miscellaneous:
- Implemented a new EULA (preview can be found here: https://store.steampowered.com/eula/1828580_eula_0 (and no we aren't collecting your data lmao)
- Changed the "How" achievement icon
- More Info now shows average nps, and max nps.
- More Info allows you to select a leaderboard score to show a hit graph of that score
- Overhauled the logging system
- Made "activateMod" functions no longer start on the "0"th beat if the game doesn't load on it. (Basically, it now starts as soon as it is done loading if set on the 0th beat)
- You can now leave a lobby while playing in game if you are not the host