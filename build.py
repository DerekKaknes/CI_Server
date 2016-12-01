import subprocess, os


root_string = 'app/code/'
test_root = 'app.tests.'
changed_files = subprocess.check_output('git diff --name-only HEAD~1', shell=True).strip().split('\n')
for f in changed_files:
    if root_string in f:
        fname = os.path.basename(f).split('.')[0]
        test_name = test_root + 'test_' + fname
        subprocess.check_output('python -m unittest {}'.format(test_name), shell=True)
