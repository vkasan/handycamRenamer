# ----------------------------------------------------------------------------------------------------
# !!! Don't forget to back up your files as there is always a chance that something could go wrong !!!
# ----------------------------------------------------------------------------------------------------

# Print details of renaming (ignored and renamed files)
debug = False

# Location of where your video files are stored
directory = '.'

# List of file extensions to consider when renaming (upper/lower-case, doesn't matter)
allowed_extensions = ['.mts']

# Length of filenames (without extension) to consider renaming
# For example: "00069.MTS" has length = 5
# Set length = 0 to rename all files in the directory (matching the allowed_extensions of course)
allowed_length = 5

# The template for renaming the files
# Available wildcards:
# date = when the video was recorded (YYYY-MM-DD HH-MM-SS)
# original = original filename without the extension
# ext = original file extension (for example ".MTS")
# ext_lower = original file extension but lowercase
new_filename_format = '{date}{ext}'

# Datetime format
# Codes are available at:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
new_filename_date_format = '%Y-%m-%d %H-%M-%S'
