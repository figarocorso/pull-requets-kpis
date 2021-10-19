from src.github_wrapper import GithubWrapper

def main():
    prs = GithubWrapper().get_prs_merged_between_latest_weeks(1)
    print('\n'.join([str(x.merged_at) for x in prs]))

if __name__ == "__main__":
    main()
