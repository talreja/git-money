# git money

# Please support bitcoin and borderless commerce by starring this repository.

## With git money you can let your work speak for itself.

It shouldn’t matter where you are - the United States, Ukraine, an island, India
or anywhere. If your code solves a problem, you should be paid. The quality of
your work should be all that matters when providing a solution to a problem.
With git money, your work is your resume. Nothing else matters.

## Not a coder? Not a problem.

A problem doesn’t have to be technical. People have needs for graphics, text,
video editing, social media assistance and many other things - and they're
willing to pay for it. If you have a skill, there might be money waiting for
you.

## How it works:

### git opportunities

[Browse current bitcoin-payable Issues on GitHub](https://github.com/21hackers/git-money/issues?q=is%3Aissue+is%3Aopen+label%3A%22git+money%22).
All Issues with a payout will contain the green label **git money** along with a
"**Current Bounty:**" when viewed. The current payout for resolving in the issue
is denoted in BTC (Bitcoin) and US Dollars. If you have a question about the
Issue, feel free to comment on it and ask! [New to
git?](https://guides.github.com/activities/hello-world/)

### git work

Once you've found an opportunity, you're halfway home (or wherever it is you're
going!). Go ahead and get to work! All you need to do is clone the repo, create
a branch, commit your changes and submit a pull request. In your pull request
message, [make sure to note that it resolves the
issue](https://github.com/blog/1506-closing-issues-via-pull-requests)  and also include your
bitcoin address. [New to Bitcoin?](https://bitcoin.org/en/bitcoin-for-individuals)

### git money

Once your pull request is merged, you instantly get paid. However you choose to
git money is up to you. Some people look for small issues that add up to larger
sums. Others go straight for the big jobs. Maybe you're middle of the road,
picking and choosing to make extra money on the side. It's completely up to you
how you want to **git money**.

## Interested in running Git Money in your own repository?

### Requirements
- 21 Bitcoin Computer [https://21.co/buy](https://21.co/buy)
- GitHub Repository [https://github.com/](https://github.com/)
- BitGo Express [https://github.com/BitGo/bitgo-express](https://github.com/BitGo/bitgo-express)

### How it works
1. From the command line on a 21 Bitcoin Computer, run `gitmoney ISSUE DESCRIPTION` with the issue title and the description of the issue that you would like to post to GitHub.
2. Assuming that no errors were encountered, your issue should now appear in your GitHub repository.
3. Post links to your issue on the Internet (Reddit, Twitter, other social media).
4. Review pull requests resolving the issue as they come in.
5. Merge the pull request that best resolves the issue to unlock the bounty.

### Installation instructions
1. Install the git-money repository on your 21 Bitcoin Computer as you would with any GitHub repository.
2. In the git-money folder that you just installed on your 21 Bitcoin Computer, run `sudo pip3 install --editable .` to install the gitmoney CLI functionality.
3. In order to access the GitHub API, you must also create a Personal Access Token by clicking **[here](https://github.com/settings/tokens)** and set it as an environment variable as GITHUB_TOKEN.
4. Then create a BitGo access token and set it as an environment variable under ACCESS_TOKEN **[here](https://www.bitgo.com)**.
5. To set an issue enter `gitmoney 'ISSUE TITLE' 'ISSUE DESCRIPTION'`

### Server Installation instructions
1. Install npm and jpeg dev library: `sudo apt-get install libjpeg-dev npm`
2. Use pip to install the required modules: `sudo pip3 install -r requirements.txt`
3. Install BitGo Express following the readme at the link above.
4. From your copy of the BitGo Express repo run: `nodejs bin/bitgo-express`
5. Start the gitmoney server from your git-money repo: `python3 startserver.py`

### Questions? Comments?

Please join [slack.21.co](https://slack.21.co/) or open an issue.
