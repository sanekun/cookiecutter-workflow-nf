import sys
import subprocess as sh


# import subprocess

try:
    # initialise git
    sh.run(["git", "init"], check=True)
    sh.run(["git", "checkout", "-b", "main"], check=True)

    # create repository
    sh.run(['git', 'remote', 'add', 'origin', 'https://github.com/{{ cookiecutter.archetype_org}}/{{ cookiecutter.archetype_id }}.git'], check=True)
    
except subprocess.CalledProcessError as err:
    print('Error:', err)

sys.exit(0)
