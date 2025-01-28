# ----------------------------------------------------------------------------------------------------
# !!! Don't forget to back up your files as there is always a chance that something could go wrong !!!
# ----------------------------------------------------------------------------------------------------

import time

from renamer import rename
import config

start_time = time.time()

rename_stats = rename(debug=config.debug,
                      directory=config.directory,
                      allowed_extensions=config.allowed_extensions,
                      allowed_length=config.allowed_length,
                      new_filename_format=config.new_filename_format,
                      new_filename_date_format=config.new_filename_date_format)

print(f'Done in {round(time.time() - start_time, 4)} seconds!\n'
      f'*  Successfully renamed {rename_stats[0]} file(s)\n'
      f'*  Skipped {rename_stats[1]} file(s)')
