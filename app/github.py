import json, os, io, datetime
import urllib.request
#ACCESS_TOKEN = app.config['ACCESS_TOKEN']
repository = json.loads(io.open(os.environ['REPOS_JSON_PATH'], 'r').read())

class github(object):
    
    @staticmethod
    def create_issue(issue_params):

        github_url = "https://api.github.com/repos/" + repository['path'] + "/issues"
        headers = { "Authorization": "token " + repository['token'], "Content-Type": "application/json" }

        # Setup the request
        req = urllib.request.Request(github_url, data=issue_params, headers=headers)

        # Make the request, capture the response
        res = urllib.request.urlopen(req).read()
        res = json.loads(res.decode())

        # TODO: Take the response and check for an ACK, then return true, else handle error
        print(res)

    def _set_issue_params(bitcoin_address, bounty_image):

        issue_title = "Testing: " + str(datetime.datetime.now())
        description = "<h6>Reward  (" + bitcoin_address + ")</h>\n\n![BOUNTY](" + bounty_image + ")"

        params = { "title": issue_title, "body": description }
        params = json.dumps(params).encode('utf8')

        return params
