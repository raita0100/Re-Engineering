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
      type-of-file:</br>
      - **d** => for directory</br>
      - **f** => for link files</br>
      - **\-** => for others</br>
    next 9 bits are divided into 3-groups of 3-each</br>
       <ol>
        <li>Owner</li>
       <li>Group</li>
       <li>Others</li>
       </ol>
       </br>
    permissions are:
       - read (r) (4)
       - write (w) (2)
       - execute (x) (1)

    - Setting owner
    ```sh
    $ chown [option] <selecting user/group> <path/to/file>
    ```
    options may be -> -R</br>
    setting group or user as -> :group

    - giving permissions to Others
    ```sh
    $ chmod [option] <users><add/remove>
    $ chmod -R 777 <path/to/file> -> set rwx to ugo
    $ chmod 744 <path/to/file> -> set rwxrr to ugo
    $ chmod g+rw <path/to/file>
    ```
    | Users | explainations |
    |-------|---------------|
    | a | all |
    | g | group |
    | o | other |
    | u | user |

    - linking the file (inode number)
    ```sh
    $ ln -l <source_path> <link_path>
    ```
    to avoid duplication one file can named with symbolic links to access at different positions.

  * Connecting to Other computers
    ---
    > (Secure SHell) (SSH) -> To connect to remote computer</br> (Secure CoPy) (SCP) -> to copy files from or to remote computer.

    ```sh
    $ ssh user@remote_computer_address
    ```
    then it will ask for a password.</br>

    To copy files:
    ```sh
    $ scp <source_path> user@host:<destination_path>
    ```
    - environment
      ---
      --> bash is a program here we can write sub program to run.</br>
      --> Also we can define variables to.</br>
      To Define a variables
      ```sh
      $ export variable=value
      ```
      this is now a environent variable.</br>
      To view the variables vale use ***echo***.
      ```sh
      $ echo $variable
      ```
      To view all the Environment variables:
      ```sh
      $ env
      ```
      **Saving Environment variable (.bashrc)**
      > Environment variables are stored in ~/.bash_profile or ~/.bashrc file

      To make your own environment variables</br>
      <ul>
        <li>open ~/.bashrc file</li>
        <li>write your variable as export variable=value</li>
        <li>close file</li>
        <li>source ~/.bashrc</li>
        <li>now we can use variable as $variable</li>
      </ul>

      * Adding the data to path
        ---
        ```sh
        $ export PATH=$PATH:<path/to/file/to/add/to/path>
        ```
        this will add new_apth to path list.</br>
        $PATH -> previous path value</br>
        : separation to new path.

    * Nick naming command (alias)
      ---
      To make large commands small we can alias them.</br>
      ex: if i need to list content of folder with different colores for directories and files.</br>
      in mac-t command is : ls -G </br>
      in linux command is : ls --color </br>
      we cann alias them using ***alias***
      ```sh
      $ alias ls 'ls -G'
      ```
      > if commands are more we can store them in a separate file like ~/.bash_aliases</br>
      and add to ~/.bashrc to compile  source ~/.bash_aliases

    * Scripting with bash
      ---
      bash scripts ends with .sh and all commands valid in terminal are valid in bash script. </br>
      simple progtram to explore directories
      ```sh
      $ vi explore.sh
      ```
      use # for comments write script</br>
      to run ***./explore.sh***
