import os
from datetime import datetime


def rename(debug: bool,
           directory: str,
           allowed_extensions: list[str],
           allowed_length: int,
           new_filename_format: str,
           new_filename_date_format: str) -> tuple[int, int]:
    files_renamed = 0
    files_skipped = 0

    length_ignored = False
    if allowed_length <= 0:
        length_ignored = True

    for filename in os.listdir(directory):
        full_filename = os.path.join(directory, filename)
        part_name, part_ext = os.path.splitext(filename)
        if part_ext.lower() not in allowed_extensions or (len(part_name) != allowed_length and not length_ignored):
            files_skipped += 1
            if debug:
                print(f'[debug] Skipping {filename}')
            continue
        else:
            files_renamed += 1
            ts_mtime = int(os.stat(full_filename).st_mtime)
            ts_ctime = int(os.stat(full_filename).st_ctime)
            ts = min(ts_ctime, ts_mtime)
            date = datetime.utcfromtimestamp(ts).strftime(new_filename_date_format)
            new_filename = new_filename_format.format(date=date,
                                                      original=part_name,
                                                      ext=part_ext,
                                                      ext_lower=part_ext.lower())
            if debug:
                print(f'[debug] Renaming {filename} to {new_filename}')
            os.rename(full_filename, new_filename)

    return files_renamed, files_skipped
