import cx_Freeze
# executables = [cx_Freeze.Executable("test1.py",,
#      icon="Icon.ico")]
# cx_Freeze.setup(
# 	name="Town",
# 	options={"build_exe":{"packages":["pygame"]}},
# 	description ="Project",
# 	executables = executables
# 	)

exe = cx_Freeze.Executable(
        script = "Main.py",
        icon = "C:\Users\Martin\Dropbox\Nottingham\sem1\Programming\project_pygame\crousework\picture\icon1.ico",
        # targetName = "Town.exe",

        )
includefiles = ['C:\Users\Martin\Dropbox\Nottingham\sem1\Programming\project_pygame\crousework\picture']

cx_Freeze.setup(
    name = "Town game",
    version = "0.1",
    description = "Converts Binary values to Decimal values",
    author = "Martin",
    options = {'build_exe': {"packages":["pygame"],'include_files':includefiles}},
    executables = [exe]
)