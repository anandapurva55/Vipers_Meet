import cx_Freeze
import os


executables = [cx_Freeze.Executable("snake.py")]



cx_Freeze.setup(name = "Vipers Meet",



                options = {

                 "build_exe" : {

                "packages" :["pygame"],

                     "include_files" : ["apple.png","snake1.jpg"]
                               }
                           },

                 description = "Vipers Meet is a very nice game",


                 executables = executables




)
