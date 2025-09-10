
https://github.com/AmpersandHQ/ampersand-magento2-upgrade-patch-helper
we need a 2 way diff from vendor to theme

https://zero1.teamwork.com/app/tasks/28524640


IMAGINE

If I had a bash script which can check every PHTML file in a Magento theme, 
https://my.mdoq.io/#/filter/client-83/instance/20157

1. create an instance [20157]
2. Declare the theme you are checking [app/design/frontend/z1/hyva]
3. loop through all files in 2 and identify the .phtml files
4. using the 1st folder, search vendor for the registration files to identify the vendor extension folder



All Vendor (LUMA)
```
#!/bin/bash

# Check if arguments are provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <path_to_theme_folder> [excluded_directories...]"
    exit 1
fi

theme_folder="$1"
vendor_dir="/home/magento/htdocs/vendor" # Update this with the actual path to the vendor directory
excluded_directories=("${@:2}")  # Get the list of excluded directories

# Function to extract module name from registration.php
get_module_name() {
    local module_name
    local vendor_file="$1"
    module_name=$(grep -oP "['\"]\K[^'\"]+" "$vendor_file" | head -1)
    echo "$module_name"
}


# Recursive function to find .phtml files in theme folder
find_phtml_files() {
    local current_dir="$1"
    for file in "$current_dir"/*; do
    #echo $file
        if [ -d "$file" ]; then
            # Check if the current directory should be excluded
            should_exclude=0
            for excluded_dir in "${excluded_directories[@]}"; do
                if [ "$file" == "$excluded_dir" ]; then
                    should_exclude=1
                    break
                fi
            done
            if [ $should_exclude -eq 1 ]; then
                continue
            fi
            
            find_phtml_files "$file"
        elif [ "${file: -6}" == ".phtml" ]; then
        #echo "Found $file"
            for registration_file in $(find "${vendor_dir}" -name registration.php); do
                module_name=$(get_module_name "$registration_file")
                #echo "$module_name"
                if [ -n "$module_name" ]; then
                    vendor_file="${registration_file%/*}/view/frontend/templates/${file##*/}"
                    if [ -f "$vendor_file" ]; then
                        echo "Copying $vendor_file to $file"
                        cp "$vendor_file" "$file"
                    fi
                fi
            done
        fi
    done
}

# Start the search
find_phtml_files "$theme_folder"
```



Just Hyva
```
#!/bin/bash

# Check if arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory_1> <directory_2>"
    exit 1
fi

dir1="$1"
dir2="$2"

# Function to recursively find .phtml files in directory 1
find_phtml_files() {
    local current_dir="$1"
    for file in "$current_dir"/*; do
        if [ -d "$file" ]; then
            find_phtml_files "$file"
        elif [ "${file: -6}" == ".phtml" ]; then
            # Extract the relative path of the file
            relative_path="${file#$dir1}"
            # Construct the corresponding file path in directory 2
            dir2_file="${dir2}${relative_path}"
            # Check if the file exists in directory 2
            if [ -f "$dir2_file" ]; then
                # Create the directory structure in directory 1 if it doesn't exist
                mkdir -p "$(dirname "$file")"
                echo "Copying $dir2_file to $file"
                cp "$dir2_file" "$file"
            fi
        fi
    done
}

# Start the search in directory 1
find_phtml_files "$dir1"

```
