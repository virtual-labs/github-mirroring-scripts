import os
import sys

path = '/root/' + sys.argv[1] + '/'
os.system('mkdir -p ' + path)
with open('list_of_repos.txt', 'r') as repos_to_clone:
	cmd = ''
	for line in repos_to_clone:
		line = line.strip()
		repo_name = line.split('/')[-1].split('.git')[0]
		if os.path.exists(os.path.join(path, repo_name)) == False:
			cmd = 'git clone %s %s%s' % (line, path, repo_name)
		else:
			os.system('git --git-dir=%s%s%s %s' % (path, repo_name, '/.git', 'reset --hard HEAD')
			cmd = 'git --git-dir=%s%s%s %s' % (path, repo_name, '/.git', 'pull')
		os.system(cmd)
os.system('rm list_of_repos.txt')
