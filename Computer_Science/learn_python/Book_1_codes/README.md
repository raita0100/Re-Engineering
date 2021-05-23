## 1. Getting Starter

  - Shell Commands
    * path and pwd (Present working directory)
     ---
      ```sh
      $ pwd
      /Users/vinodpatil/Downloads/Learning/Re-Engineering/Computer_Science/learn_python/Book_1_codes
      ```
      this will give us the **Relative path.**</br>

      | Syntax | Meaning|
      |--------|--------|
      | / | root directory |
      |  ~  | home directory |
      |  .  | current directory |
      |  ..  | parent directory |
      | ../../| Parent to Parent directory |

      ```sh
      ~myfiles/:$
      ```
      ##### This is abbreviated path.

    * ls (Listing the content).
     ---
      ```sh
      $ ls
      README.md	test.py
      ```
      ```sh
      $ ls .
      README.md	test.py
      ```
      ```sh
      $ ls ..
      Book_1_codes	Books		README.md
      ```
      ```sh
      $ ls ../../
      learn_python
      ```

    * cd (Chnage directory).
     ---

     ```sh
     $ cd [optional path]
     ```
     default **cd** take to home directory

   * File (Working with files)
     ---

     - head
      ```sh
      $ head <./path/to/file>
      ```
      prints first 10 Lines of file

      - tail
      ```sh
      $ tail <./path/to/file>
      ```
      prints the last 10 lines of file

      - touch
      ```sh
      $ touch <filename.txt>
      ```
      for creating the file
      > * spaces can be used in namings with escape charecter *(\)* ex: touch my\ file.txt => (my file.txt)

      - cat and (> -> Redirection)
      ```sh
      $ cat [pth/to/file]
      ```
      This will print content of files
      ```sh
      $ cat <source/file> > <target/file>
      ```
      This will copy cotent of source file to target file
      ```sh
      $ cat > <target/file>
      ```
      This will overwrite whatever you type in terminal to taget file</br>
      To terminate hit ctrl+d

      - Text Editores
        + nano (more basic)
        + vim (moderrmn linux)
        + emacs (normal)
      ```sh
      $ nano <filename>
      $ vi <fileneme>
      $ emacs <filename>
      ```
      Choose any one to fire with editor in terminal

      - cp Copying the files
      ```sh
      $ cp [-opt] <source path> <destination path>
      ```
      </br>
      copy from source to destination</br></br>

      optional arguements:
      | options | function|
      |---------|---------|
      | -v | print verbose |
      | -i | To prompt the conformation |
      | -u | Not to overwrite at destination |
      | -p | Reserve the permission of ownership |
      | -r | to copy subdirectories |
      | -rt | To copy only the files and subdirectories but not the source directory, use the -T option: |
      | man cp | For more opti

     - mv Moving the files
     ```sh
     $ mv <source/path> <destination/path>
     ```
     move files from source to destination

     - mkdir (Make directory)
      ```sh
      $ mkdir <file/path/for/creation>
      ```
     create a file in specified location</br>

     - rm Remove files or delete files
      ```sh
      $ rm [-opt] <file/to/remove>
      ```
      | option | explaination |
      |--------|--------------|
      | -r | all subdirectories</br> with asking permission for each|
      | -rf | force delete</br>No permission asked |

    * Flags and wildcards
      ---
    > -r is a flag or switch</br>
    > "*" is a wildcard for 0 or more.</br>

    * Getting help
      ---
      ```sh
      $ man ls
      ```
      man (manual) used for online refarance manual pf a Commands.<br>
      ### <u>*man*</u> uses <u>*less*</u> viewer for viewing the files.</br>

      > ### *less is modeled over more.*

    - Search for a command and feature
      ```sh
      $ apropos "text editor"
      ```
      this will list all the man pages which have text editor in them
      ex: above outputs
      ```sh
      $ apropos "text editor"
      ed(1), red(1)            - text editor
      vim(1)                   - Vi IMproved, a programmer's text editor
      ```
      </br>

    * Combining Utilities with redirection and pipes (>, >> , |)
      ---

      | option | description |
      |--------|-------------|
      | > | output of left overwrite to right file|
      | >> | append to right |
      | \| | pipe or chain (cobine commands)|

    * Permission and Shearing
      ---
      To see permissions:
      ```sh
      $ ls -l
      -rw-r--r-- type ownername groupownerbelong size mont day hour:minute Name-of-file
      ```
    first bit in 10 bits: -rw-r--r--
      type-of-file:
      - **d** => for directory
      - **f** => for link files
      - **\-** => for others</br>
    next 9 bits are divided into 3-groups of 3-each
       1. Owner
       2. Group
       3. Others
       </br>
    permissions are:
       - read (r) (1)
       - write (w) (2)
       - execute (x) (4)
