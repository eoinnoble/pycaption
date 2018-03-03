# -*- coding: utf-8 -*-

import io
import os
import sys
import time

from pycaption import DFXPWriter, SRTReader


INPUT_DIRECTORY = "input"
OUTPUT_DIRECTORY = "output"


def convert_srt_to_dfxp(times, generate_output=False):

    all_time = 0
    counter = 0
    input_file_count = len(os.listdir(INPUT_DIRECTORY))
    skipped_files = 0

    for input_file in os.listdir(INPUT_DIRECTORY):

        if input_file.startswith('.'):  # Skip hidden files and SRT master file
            skipped_files += 1
            continue

        filename = '{}/{}'.format(INPUT_DIRECTORY, input_file)

        with io.open(filename, 'r', encoding='utf-8') as fh:
            try:
                srt_data = fh.read()
            except UnicodeDecodeError:
                print("Problem with {}".format(filename))
                raise

        total_file_time = 0

        for _ in range(times):
            t0 = time.time()
            dfxp_data = DFXPWriter().write(SRTReader().read(srt_data))
            t1 = time.time()
            time_taken = t1 - t0
            total_file_time += time_taken

            if generate_output and "{}.xml".format(counter) not in os.listdir(OUTPUT_DIRECTORY):
                with open("{}/{}.xml".format(OUTPUT_DIRECTORY, counter), "w") as new_dfxp_file:
                    new_dfxp_file.write(dfxp_data)

        all_time += total_file_time
        counter += 1
        sys.stdout.write("\r{}/{} files completed.".format(counter, input_file_count))

    print("\nConverting {} files took an average of {} seconds over {} iterations.\n{} files were skipped".format(
        counter,
        all_time / times,
        times,
        skipped_files
    ))


if __name__ == '__main__':
    try:
        iterations = int(sys.argv[1])
    except (IndexError, ValueError):
        iterations = None

    try:
        output_flag = bool(sys.argv[2])
    except IndexError:
        output_flag = False

    if type(iterations) is int:
        print("Converting SRT from folder '{}' into DFXP {} time{}.".format(
            INPUT_DIRECTORY,
            iterations,
            "s" if iterations > 1 else ""
        ))
        if output_flag is True:
            print("Saving converted files in folder '{}'.".format(OUTPUT_DIRECTORY))
        else:
            print("Converted files will not be saved (pass `True` as second argument to save output).")

        convert_srt_to_dfxp(iterations, output_flag)
    else:
        print("Please provide an integer for the number of iterations you want to test.")
