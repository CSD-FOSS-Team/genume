# Bash protocol

## Available commands

### configure

This commands takes any number of arguments, which are the names of the commands your script requires to run. By default if a command is not available your script terminates execution. This behavior can be changed by specifying the `--nonfatal` optional flag. In this case configure returns a non-zero code and your script will continue execution normally.

### gset

This commands takes any number of optional arguments. The name of each argument is the key and the argument of the argument is the value to set the key to.

### subcat

### value

## Example script

```sh
# Specify required commands.
configure date pwd
# Add description(optional).
gset --description="I am the description!"
# Obligatory hello world.
value --basic test_value Hello World!
# Changing subcategory.
subcat nested
value --advanced adv 'Only for advanced people!'
subcat
# Temporary subcategory.
output=$(date)
value --subcat .date time "Time is ticking: \n ${output}"
# Execute command inside string.
value --advanced dir "Running inside $(pwd)"
```