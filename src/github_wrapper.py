import os

from github import Github

from src.week_operations import WeekOperations


REPO = "draios/automation"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]


class GithubWrapper:
    def __init__(self):
        self.repo = Github(GITHUB_TOKEN).get_repo(REPO)

    def get_prs_merged_between_latest_weeks(self, number_of_weeks):
        prs = []
        for pr in self.repo.get_pulls(state="closed", sort="created", direction="desc", base="staging"):
            merged_at = pr.merged_at
            if merged_at is None:
                continue

            if WeekOperations.is_date_before_latest_weeks(merged_at, number_of_weeks):
                break

            if WeekOperations.is_date_between_latest_weeks(merged_at, number_of_weeks):
                prs.append(pr)

        return prs
