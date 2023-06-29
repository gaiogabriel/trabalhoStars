import cx_Freeze
executables= [
    cx_Freeze.Executable(script= "main.py", icon= "space.ico")
]
cx_Freeze.setup(
    name= "Space Marker",
    options= {
        "build_exe":{
            "packages": ["pygame"],
            "include_files":["fundo.jpg",
                             "audio.mp3"
                
                            ]
        }
    } , executables= executables
)