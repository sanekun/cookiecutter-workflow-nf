import sys
import subprocess as sh


# import subprocess

try:
    # initialise git
    sh.run(["git", "init"], check=True)
    sh.run(["git", "checkout", "-b", "main"], check=True)

    # create repository
    sh.run(['git', 'remote', 'add', 'origin', '{{ cookiecutter.archetype_git }}'], check=True)
    
except subprocess.CalledProcessError as err:
    print('Error:', err)

sys.exit(0)
