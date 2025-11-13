## Instructions

1. Roll up an instance for the client
2. Open the code editor and look for the file `mdoq/post_roll_up_actions`.
  If this file doesn't exist you need to add it, you can do this by running the following from SSH
  `cd ~/htdocs && wget https://raw.githubusercontent.com/MDOQ-UK/Templates/main/post_roll_up_actions -O mdoq/post_roll_up_actions && chmod a+x mdoq/post_roll_up_actions`
3. Once `mdoq/post_roll_up_actions` exists you need to open the file in the code editor
  You need to look for the lines that have:
  ```
  "$ARGUMENT_STEP_FINAL-$ARGUMENT_COMPARISON_AHEAD")
            set -xe
            # do something
            ;;
        "$ARGUMENT_STEP_FINAL-$ARGUMENT_COMPARISON_IDENTICAL")
            set -xe
            # do something
            ;;
        "$ARGUMENT_STEP_FINAL-$ARGUMENT_COMPARISON_BEHIND")
            set -xe
            # do something
            ;;
  ```
  There may be content in there instead of "# do something", if so do not delete.
  You then need to add the following for each, right before the `;;`
  ```
  curl -s https://raw.githubusercontent.com/zero1limited/gitignore/master/updater.php | php
  curl -s https://raw.githubusercontent.com/MDOQ-UK/Templates/main/gitignore/updater.php | php
  ```
  So that this part of the file looks like:
  ```
  "$ARGUMENT_STEP_FINAL-$ARGUMENT_COMPARISON_AHEAD")
            set -xe
            curl -s https://raw.githubusercontent.com/zero1limited/gitignore/master/updater.php | php
            curl -s https://raw.githubusercontent.com/MDOQ-UK/Templates/main/gitignore/updater.php | php
            ;;
   "$ARGUMENT_STEP_FINAL-$ARGUMENT_COMPARISON_IDENTICAL")
            set -xe
            curl -s https://raw.githubusercontent.com/zero1limited/gitignore/master/updater.php | php
            curl -s https://raw.githubusercontent.com/MDOQ-UK/Templates/main/gitignore/updater.php | php
            ;;
   "$ARGUMENT_STEP_FINAL-$ARGUMENT_COMPARISON_BEHIND")
            set -xe
            curl -s https://raw.githubusercontent.com/zero1limited/gitignore/master/updater.php | php
            curl -s https://raw.githubusercontent.com/MDOQ-UK/Templates/main/gitignore/updater.php | php
            ;;
  ```
  **If unsure please just ask Adam to confirm** (when the instance is ready)
4. Commit this file to git
5. Recreate the instance
6. Test the instance
7. Check if the file `.gitignore` can be added to git, if so commit it.
8. Ask Adam to validate the work.
9. Use the "I'm Done" process to merge this file into master.
> This work does not need to be released.
{.is-warning}
