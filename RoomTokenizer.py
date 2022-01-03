#!/usr/bin/env python

# Copyright (c) 2017-2022, Austin Carpenter
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 

from gimpfu import *

# import OS stuff for saving the image
import os.path
import os

def export_selection():

   pdb.gimp_message('Started')

   # Gather some data about the image
   mainImage = gimp.image_list()[0]
   mainDrawable = pdb.gimp_image_get_active_drawable(mainImage)

   # Get the filename and remove the extension. We'll use this later to create a new folder to put all our rooms in.
   filename = pdb.gimp_image_get_filename(mainImage)
   filepath = filename[0: filename.rfind('.')] + '_rooms'

   # Begin undo grouping
   # What this means is that if you want to undo afterwards, it will undo the whole script
   # Otherwise it would just undo each individual step
   # Note that undo won't remove the exported room from your file system
   pdb.gimp_image_undo_group_start(mainImage);

   # Cut the selection
   pdb.gimp_edit_cut(mainDrawable)

   # Paste it to a new image
   newImage = pdb.gimp_edit_paste_as_new()

   # Get the drawable, we'll need it for saving later
   newDrawable = pdb.gimp_image_get_active_drawable(newImage)

   # Create a new 'rooms' directory if there already isn't one
   # NOTE: I don't believe this will work on OSX, so you'll have to create it manually beforehand
   if not os.path.isdir(filepath):
      os.mkdir(filepath)

   # Increment the room number based on what's already in the folder, then save it
   # ENHANCE:  This was the first implementation that came to mind, but it will take longer and longer the more rooms are in the folder.
   # It is probably faster to get a list of the files in the folder, sort them, get the last one, parse the last 5 digits out of it and increment them to get the room number.
   # But that will require more error checking and honestly this is far from the bottleneck in this process
   roomNum = 0
   while (roomNum < 65535):
      if os.path.isfile(filepath + os.sep + 'room' + str(roomNum).zfill(5) + '.png'):
         roomNum = roomNum + 1
      else:
         # We've found out what to name our file, so break out
         break;

   # Save the file name with the incremented number
   pdb.file_png_save(newImage, newDrawable, filepath + os.sep + 'room' + str(roomNum).zfill(5) + '.png', '?', 0, 0, 0, 0, 0, 1, 0)

   # Close the new image
   pdb.gimp_image_delete(newImage)

   pdb.gimp_message('Room Token Created')

   # Unselect all
   pdb.gimp_selection_none(mainImage)

   # End the undo grouping
   pdb.gimp_image_undo_group_end(mainImage);

   # End the progress bar
   pdb.gimp_progress_end()

# It's surprisingly hard to find clear, straightforward documentation parameters for the register function.
register(
        "python-fu-export_selection_png",  # This looks like the name it gets in the gimp plugin database
        N_("Creates a new image from the selection"), # This is the tool tip that shows when you hover over the newly created option in the Edit menu.
        "Used for creating individual room tokens for RPGs in Tabletop Simulator", # This is some more info that shows up in the plugin database
        "Austin Carpenter", # Author
        "Austin Carpenter", # Copyright Holder
        "2017-2022", # Copyright year.  This was written and posted to Reddit in 2017 and cleaned up and added to GitHub in 2022
        N_("Export Selection"), # This is the name it gets in the Edit menu.
        "RGBA", # Types of images this script can be run on.  We need an alpha channel for this to work
        [], # Arguments it takes (none)
        [], # Results? (none)
        export_selection, # The name of the function above
        menu = "<Image>/Edit",  # Where in the script lives in the GIMP menu.  If you don't want it in Edit, change this here.  You can create sub-menus too.
        domain=("gimp20-python", gimp.locale_directory)) # I believe this relates to where it lives in the gimp installation

# I believe GIMP will call register() to set it up, and that will map export_selection to this main
main()