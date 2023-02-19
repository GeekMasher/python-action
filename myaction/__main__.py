
import argparse

parser = argparse.ArgumentParser(__name__)

parser_github = parser.add_argument_group("github")
parser_github.add_argument("-gt", "--github-token")
parser_github.add_argument("-gr", "--github-repository")

if __name__ == "__main__":
    arguments = parser.parse_args()

    print(f" >> {arguments.github_repository}")

