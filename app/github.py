import json, os, io, datetime
import urllib.request
from commonregex import CommonRegex
from two1.lib.wallet.hd_account import HDAccount
from two1.lib.wallet.two1_wallet import Two1Wallet

config_path = os.path.dirname(os.path.realpath(__file__)) + '/../config/repos.json'
repository = json.loads(io.open(config_path, 'r').read())

class github(object):
    def _decorate_issue_params(issue_title, description):

        bitcoin_address = repository['address']
        bounty_image = 'http://git-money-badge.mybluemix.net/badge/' + bitcoin_address
        issue_title = "Testing: " + str(datetime.datetime.now())
        description = "<h6>Reward  (" + bitcoin_address + ")</h>\n\n![BOUNTY](" + bounty_image + ")"

        params = { "title": issue_title, "body": description }
        params = json.dumps(params).encode('utf8')
        return params
    
    @staticmethod
    def create_issue(issue_title, description):

        params = github._decorate_issue_params(issue_title, description)

        github_url = "https://api.github.com/repos/" + repository['path'] + "/issues"
        headers = { "Authorization": "token " + repository['token'], "Content-Type": "application/json" }

        # Setup the request
        req = urllib.request.Request(github_url, data=params, headers=headers)

        # Make the request, capture the response
        res = urllib.request.urlopen(req).read()
        res = json.loads(res.decode())

        # TODO: Take the response and check for an ACK, then return true, else handle error
        print(res)

    @staticmethod
    def get_address_from_issue(issue_number):

        github_url = "https://api.github.com/repos/" + repository['path'] + '/issues/' + issue_number
        headers = { "Authorization": "token " + repository['token'], "Content-Type": "application/json" }

        # Setup the request
        req = urllib.request.Request(github_url, headers=headers)

        # Make the request, capture the response
        res = urllib.request.urlopen(req).read()
        res = json.loads(res.decode())

        body = res['body']
        address = CommonRegex(body).btc_addresses[0]

        return address

