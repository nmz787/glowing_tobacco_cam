I bought a Gleaux GMO Tobacco plant, and wanted to automatically take (remote triggered) photos with my dSLR camera, then perform image stacking on them.

My camera was an older Canon EOS Digital Rebel XT (Canon EOS 350D), and I ended up wrapping `subprocess` calls around `gphoto2` to control the shutter speed, snap pics, list the images on the camera memory, download the images, and then stack them.

Generates a timestamped TIFF file when run. Settings for exposure time and number of images are inside `bunchapics.py`

Requires:

`sudo apt-get install gphoto2`

`sudo -H pip install rawpy`

`sudo -H pip install opencv-python`

Usage:
`python bunchapics.py`