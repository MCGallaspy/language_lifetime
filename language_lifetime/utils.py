"""
A module of useful functions for implementing the process described in README.md.

You *can* run this from the command line, but it's behavior depends on my whim (and whatever I'm debugging) so don't
rely on it.
"""
import os
import requests
import subprocess
import sys

# Github username and password for making authenticated requests
GHUNAME = os.environ["GHUNAME"]
GHPASSWD = os.environ["GHPASSWD"]


def github_get(*args, **kwargs):
    """
    Make an authenticated request to github.
    :return: A request object.
    """
    kwargs.update({
        "auth": (GHUNAME, GHPASSWD)
    })
    return requests.get(*args, **kwargs)


def analyze_tree(repo_path):
    """
    :param repo_path: A string. The path to a repo to analyze.
    :return: A dict, with language-bytes key-value pairs.
    """
    proc = subprocess.Popen("bundle exec linguist", shell=True, cwd=repo_path, stdout=subprocess.PIPE,
                            universal_newlines=True)
    out, err = proc.communicate()
    langs = dict()
    for line in out.splitlines():
        pct, lang = line.split()
        langs[lang] = pct
    return langs


if __name__ == "__main__":
    print(analyze_tree(sys.argv[1]))
