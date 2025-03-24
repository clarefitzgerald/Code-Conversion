## This program was made using ChatGPT prompts. I will not take credit for it, but this saved me probably a couple days worth of Ctrl+F and replace all.
# Mass variable renaming for Studio 5000 L5K files
## Purpose:
### Migrating antiquated RsLogix 500 code to Studio 5000 takes forever because of the switch from direct addressing to tag-based addressing. If you want code that is readable in the future, you might want to consider changing your variable names to something meaningful (instead of "B3[0].5" or something). 
## How to Use:
### In Studio 5000, "save as" an L5K file. 
### Export all tag names and comments from Studio 5000 and edit the file to make your new tags. 
### Create an Excel file with the left column as the old names (including the bit referenced) and the right column as the new names. 
### Export the file as a CSV. Change the variable that holds the CSV file name to match the one you created. 
### In a code editor such as VS Code, change the variable names that hold the file name to match yours. If you are referencing a file in a different directory, use the os.chdir. 
### Make sure you have a python interpreter installed and then run your code. 
