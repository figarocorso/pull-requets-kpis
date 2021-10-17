import os

from github import Github

REPO = "draios/automation"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

def main():
    repo = Github(GITHUB_TOKEN).get_repo(REPO)
    for pr in repo.get_pulls(state="closed", sort="created", direction="desc", base="staging"):
        print(pr)
        break

if __name__ == "__main__":
    main()
