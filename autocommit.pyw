# -*- coding: utf-8 -*-
"""
Created on Tues June  3 13:08:39 2020

@author: elmokulc
"""

# commande line to  convert to ex  : pyinstaller.exe --onefile --console --icon=icon.ico zotero_launcher.py
import subprocess
import os
import datetime

repository = os.getcwd()

# Pull data
print("#PULL")
git_command_pull = ['git', 'pull', 'origin', 'master']
git_query = subprocess.Popen(git_command_pull, cwd=repository,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(git_out_txt0, error) = git_query.communicate()
git_out_txt0 = git_out_txt0.decode("utf-8")

# Saving if any chagements
print("#SAVING on Git repository")
now = datetime.datetime.now()
git_command_status = ['git', 'status']
git_command_add = ['git', 'add', '.']
git_command_commit = ['git', 'commit', '-m',
                      'commit of {0}'.format(now.strftime("%B %d, %Y, %H:%M:%S"))]
git_command_push = ['git', 'push', 'origin', 'master']


if git_query.poll() == 0:
    git_query = subprocess.Popen(git_command_status, cwd=repository,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (git_out_txt0, error) = git_query.communicate()
    git_out_txt0 = git_out_txt0.decode("utf-8")

# Git add
if git_query.poll() == 0:
    git_query = subprocess.Popen(git_command_add, cwd=repository,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (git_out_txt, error) = git_query.communicate()
    git_out_txt = git_out_txt.decode("utf-8")

    git_query = subprocess.Popen(git_command_status, cwd=repository,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (git_out_txt, error) = git_query.communicate()
    git_out_txt = git_out_txt.decode("utf-8")


# Git commit
print("Commit name {0}".format(now.strftime("%B %d, %Y, %H:%M:%S")))
if git_query.poll() == 0:
    git_query = subprocess.Popen(git_command_commit, cwd=repository,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (git_out_txt, error) = git_query.communicate()
    git_out_txt = git_out_txt.decode("utf-8")

    git_query = subprocess.Popen(git_command_status, cwd=repository,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (git_out_txt, error) = git_query.communicate()
    git_out_txt = git_out_txt.decode("utf-8")


# Git push
print("#PUSHING...")
if git_query.poll() == 0:
    git_query = subprocess.Popen(git_command_push, cwd=repository,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (git_out_txt2, error2) = git_query.communicate()
    git_out_txt2 = git_out_txt2.decode("utf-8")
    error2 = error2.decode("utf-8")
    git_query = subprocess.Popen(git_command_status, cwd=repository,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (git_out_txt, error) = git_query.communicate()
    git_out_txt = git_out_txt.decode("utf-8")

print("#CLOSING")