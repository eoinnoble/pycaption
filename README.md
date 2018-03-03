# Pycaption
Testing the speed at which [Pycaption](http://pycaption.readthedocs.io/en/stable/) converts SRT to DFXP. Source files should be kept in the `input` folder and the script will save files to `output` if you tell it to.

Run `python convert_srt_to_dfxp.py [iterations] [output flag]`, where `[iterations]` is an `int` of the number of iterations you want to test, and `[output flag]` is `True` if you want the script to save its output, and `False` by default. **Note:** the script skips hidden files (those whose filenames begin with `.`).