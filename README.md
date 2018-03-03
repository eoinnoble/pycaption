# Pycaption
Testing the speed at which [Pycaption](http://pycaption.readthedocs.io/en/stable/) converts SRT to DFXP. Source files should be kept in the `input` folder and the script will save files to `output` if you tell it to.

Run `python convert_srt_to_dfxp.py [iterations] [output flag]`, where `[iterations]` is a positive integer representing the number of iterations you want to test, and `[output flag]` is `True` if you want the script to save its output, and `False` by default. **Note:** the script skips hidden files (those whose filenames begin with `.`).

Should return something like the following in the command line:
```
Converting SRT from folder 'input' into DFXP 100 times.
Saving converted files in folder 'output'.
1609/1611 files completed.
Converting 1609 files took an average of 49.94203472137451 seconds over 100 iterations.
2 files were skipped.
```