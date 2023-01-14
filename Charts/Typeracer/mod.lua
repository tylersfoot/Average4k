function create()
    -- https://kadedev.github.io/Avg4KModDocs/
    -- https://stackoverflow.com/questions/20423406/lua-convert-string-to-table
    -- https://wiki.libsdl.org/SDL2/SDLKeycodeLookup

    -- init variables
    bpm = 120
    str = "this game is amazing i love average four kay" -- string to be typed
    currentIndex = 0 -- current character
    score = 0 -- total characters correct
    keys = 0 -- total characters typed
    over = false -- is the game over
    start = false -- has the first key been pressed
    check = false -- checks if it did the update loop
    converted = {} -- array to hold characters

    -- converts str to SDL keycode using reference array and puts each character in the `t` array
    reference = {a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7, h = 8, i = 9, j = 10,
        k = 11, l = 12, m = 13, n = 14, o = 15, p = 16, q = 17, r = 18, s = 19, t = 20, u = 21,
        v = 22, w = 23, x = 24, y = 25, z = 26, [" "]= 27}

    -- array with the characters, unconverted; used for making sprites
    characters = {}
    for i = 1, #str do
        characters[i] = str:sub(i, i)
    end

    -- create a sprite for each of the character
    for i = 1, #str do
        createSprite(characters[i], i, i*30, 0) -- change "i*30" to the spacing of the characters when i find out the img size
    end

    -- array with the converted keycodes to check in key_pressed() event
    for i = 1, #str do
        keycode = reference[str:sub(i, i):lower()]
        if keycode then
            converted[i] = keycode
        end
    end

    -- move the receptors offscreen
    activateMod("amovey", 0, 0, "outCubic", -100000)

end

function key_pressed(key)
    -- starts timer on first key press
    if start == false then
        time_start = getTime()
        start = true
    end
    -- checks if the array is not empty and the character pressed matches the current character in the array
    if currentIndex < #converted then
        if key == converted[currentIndex] then
            -- do something, like print a message
            consolePrint("Key pressed matches array value")
            score = score + 1
            -- remove the current element from the table
            table.remove(converted, currentIndex)
        end
        keys = keys + 1
        currentIndex = currentIndex + 1
    else
        over = true
        -- handle the case when the table is empty, aka the sentence has been typed
        accuracy = (score/keys) * 100
        consolePrint("Your accuracy was: " .. accuracy .. "%")


    end
end

function update(beat)
    -- if the game is over and it hasn't calculated time yet, calculate the time it took to type the sentence
    if over then
        if check == false then
            time_end = getTime()
            time = (time_end - time_start) * 1000
            consolePrint("Elapsed time: " .. time .. " seconds")
            check = true
        end
    end
end