# folder-automation

Automating the process of sorting files in a user's folder on Windows by file type.

This script iterates through the files in a user's folder on Windows and places each file in its appropriate folder, it can sort by categories or by extensions. There's a config file that contains the categories.

## Prerequisites

This script requires Python to be installed for it to run. To install Python, click [here](https://www.python.org/downloads/).

## Usage

From a terminal, navigate into the project directory.

```
$ cd downloads-folder-automation
```

From here, you have two options:

1. Run via the GUI, with both options and a popup with the target directory:

   ```
   $ python folder_sorter.py
   ```

2. Run via the command line, here you specify the method and folder to be sorted, with Download's Path as the default one (best for automation):

   ```
   $ python folder_sorter.py sort_c
   $ python folder_sorter.py sort_c "<path>"
   $ python folder_sorter.py sort_e "<path>"
   ```

To have the script run automatically, configure it in Windows Task Scheduler according to [this tutorial](https://datatofish.com/python-script-windows-scheduler/).

# Contributing

Please read [HOW_TO_CONTRIBUTE.md](https://github.com/eric-mahasi/downloads-folder-automation/blob/main/HOW_TO_CONTRIBUTE) for details on submitting pull requests.

# License

This project is licensed under the MIT license - see the [LICENCE.md](https://github.com/eric-mahasi/downloads-folder-automation/blob/main/LICENSE)
for details.

# Acknowledgement

I drew a lot of inspiration for this script from Nitish Sharma's [medium article.](https://medium.com/swlh/automation-python-organizing-files-5d2b6b933402)
Many thanks to the following people who helped me optimize my code:

- Dara Dadachanji on [GitHub](https://github.com/DaraDadachanji).
- knestleknox on [reddit](https://www.reddit.com/r/Python/comments/ptzo3u/comment/he0y4ng/?utm_source=share&utm_medium=web2x&context=3).
- c00lnerd314 on [reddit](https://www.reddit.com/r/Python/comments/ptzo3u/comment/he0d945/?utm_source=share&utm_medium=web2x&context=3).
