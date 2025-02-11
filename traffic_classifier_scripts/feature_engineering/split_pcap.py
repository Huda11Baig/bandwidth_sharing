import os
import subprocess


def split_pcap_files(input_directory, output_directory, splitcap_path="SplitCap.exe", enable="mono",
                     parallel_sessions=1018, filter_string=None):
    """
    Split all pcap files in the specified path and its subdirectories into the specified folder

    :param input_directory: Input directory path containing pcap files
    :param output_directory: Output directory path, where the split files will be stored
    :param splitcap_path: Path to the SplitCap executable
    :param enable: Environment for the executable
    :param parallel_sessions: Number of parallel sessions to keep in memory at the same time
    :param filter_string: String used to filter files, only files with this string in the file name will be split
    """
    # Make sure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".pcap") and (filter_string is None or filter_string in filename):
            input_file_path = os.path.join(input_directory, filename)
            # Create a separate output directory for each pcap file
            file_output_directory = os.path.join(output_directory, filename)
            if not os.path.exists(file_output_directory):
                os.makedirs(file_output_directory)
            # Build SplitCap command
            command = [enable, splitcap_path, "-r", input_file_path, "-o", file_output_directory, "-p", str(parallel_sessions)]
            # Execute command
            subprocess.run(command)


if __name__ == "__main__":
    output_dir = "/path/to/output/dir/"
    input_dir = "/path/to/input/dir/"
    filter_str = "iproyal"
    split_pcap_files(input_dir, output_dir, filter_string=filter_str)


