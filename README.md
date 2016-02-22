# git money

Turns issues and pull requests on GitHub into money. Get paid for submitting
pull requests associated with any kind of issue relating to things such as code,
graphics, content and more. Whatever an issue can be created for, git money can
be used so people get paid for handling them.

## Requirements
- 21 Bitcoin Computer [https://21.co/buy](https://21.co/buy)
- GitHub Repository [https://github.com/](https://github.com/)

## How it works
1. From the command line on a 21 Bitcoin Computer, run `gitmoney ISSUE DESCRIPTION` with the issue title and the description of the issue that you would like to post to GitHub.
2. Assuming that no errors were encountered, your issue should now appear in your GitHub repository.
3. Post links to your issue on the Internet (Reddit, Twitter, other social media).
4. Review pull requests resolving the issue as they come in.
5. Merge the pull request that best resolves the issue to unlock the bounty.

## Installation instructions
1. Install the git-money repository on your 21 Bitcoin Computer as you would with any GitHub repository.
2. In the git-money folder that you just installed on your 21 Bitcoin Computer, run `sudo pip3 install --editable .` to install the gitmoney CLI functionality.
3. In order to access the GitHub API, you must also create a Personal Access Token by clicking **[here](https://github.com/settings/tokens)**.
4. This Personal Access Token should then be added to the repos.json file, which you can see **[here](https://github.com/davemc84/git-money/blob/master/config/repos.json)**. As with any API token, this should neither be shared nor stored in a public repository.

## Questions? Comments?

Please join [slack.21.co](https://slack.21.co/) or open an issue.
