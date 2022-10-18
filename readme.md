# Get Random Pokemon Image Script
This python script was written to re-create Nutty's "Who's that Pokemon" ad break but using a different set of apps.
The idea isn't original but hopefully this implementation is.

Thanks to the service provided by [PokeApi](https://pokeapi.co/).

## Python Requirements
1. Python 3.10 (older versions of Python 3 might work?)
2. Install the necessary python dependencies using pip install -r requirements.txt 
    > **Dependencies Installed:**
    > - Pillow
    > - requests
3. Update the cache folder location for the script on line 13 of getPokemonImg.py. *Skipping this step will cause you a headache because the cache folder doesn't exist*
\
**Change this line**
    ```python
    12 ##Image Cache Location (CHANGE THIS FOR YOUR SYSTEM)
    13 scriptDir = f"C:\streaming\scripts\get-pokemon-images"
    ```
## Mix It Up Notes
If you're using MixItUp:
    
    - Be sure you import the commands correctly and setup the other assets you might need.
    - I have included the video files and GIF needed for the background. You will need to point the mix it up command to wherever you pulled/downloaded this repo to.

### I'm offering this with **limited support**. I won't walk you through installing MixItUp or Python. Google has the answers you need for that.
\
If there's something in the code or MIU commands that could be better feel free to let me know. 

### You can find me on these platforms:
> YouTube: https://youtube.com/chrono32123
\
> Twitter: https://twitter.com/chrono32123
\
> Discord: Chrono#8297
\
> Other Platforms: https://beacons.ai/chrono

## Possible Enhancements
- Make a master text file for the national dex numbers
- Find a way to run the script in Mix It Up without needing to define the cache directory. (User Args maybe?)
