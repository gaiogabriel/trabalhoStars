import cx_Freeze
executables= [
    cx_Freeze.Executable(script= "main.py", icon= "space.ico")
]
cx_Freeze.setup(
    Name= "SpaceMarker",
    options= {
        "build.exe":{
            "packages": ["pygame"],
            "include_files":[
                "audio.mp3",
                "fundo.jpg"
                
            ]
        }
    } , executables= executables
)