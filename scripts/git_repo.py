"""
git functionalities
"""

import os
import logging
from subprocess import check_call

git_repo = os.getenv('GIT_REPO')

logging.basicConfig(level=logging.DEBUG)

GIT_YML_PATH = '/opt/docker-compose-projects-git/'

def git_pull():
    """
    perform git pull
    """
    if git_repo:
        logging.info('Updating Git project repository')
        check_call(['git', '-C', GIT_YML_PATH, 'pull', '--no-rebase', 'origin'])
    else:
        logging.info('will not execute git pull: not a git repository')

if git_repo:
    if os.path.isdir(os.path.join(GIT_YML_PATH, '.git')):
        git_pull()
    else:
        logging.info('Cloning Git project repository')
        check_call(['git', 'clone', '--', git_repo, GIT_YML_PATH])
