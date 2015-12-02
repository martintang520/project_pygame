import cx_Freeze

# using cxfreeze

exe = cx_Freeze.Executable(
        script = "Main.py",
        icon = "picture/icon1.ico",
        # targetName = "Defense of Paris.exe",

        )
includefiles = ['picture','music','sound','map.xml']

cx_Freeze.setup(
    name = "Defense of Paris",
    version = "1.0",
    description = "Converts Binary values to Decimal values",
    author = "Arthas Group",
    options = {'build_exe': {"packages":["pygame"],'include_files':includefiles}},
    executables = [exe]
)