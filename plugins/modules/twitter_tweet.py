#!/usr/bin/python
"""tweet module for ansible
 Copyright: (c) 2020, Daisuke Matsui <dmatsui@redhat.com>
"""

from ansible.module_utils.basic import AnsibleModule
from twitter import Twitter, OAuth
from twitter.api import TwitterHTTPError


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
module: twitter_tweet
short_description: tweet
description: post tweet from ansible to twitter
options:
  TBD
'''

EXAMPLES = '''
- name: tweet
  twitter_tweet:
    state: present
    consumer_key: "{{ consumer_key }}"
    consumer_secret_key: "{{ consumer_secret_key }}"
    access_token: "{{ access_token }}"
    access_token_secret: "{{ access_token_secret }}"
    tweet: "this tweet posted by ansible module"
'''

RETURN = '''
'''


def tweet():
    """tweet post method
    """
    changed = None
    module = AnsibleModule(
        argument_spec={
            'state': {'required': False, 'default': 'present'},
            'server': {'required': False, 'default': 'api.twitter.com'},
            'https': {'required': False, 'type': 'bool', 'default': True},
            'consumer_key': {'required': True},
            'consumer_secret_key': {'required': True},
            'access_token': {'required': True},
            'access_token_secret': {'required': True},
            'tweet': {'required': True}
        },
    )
    tweet_text = module.params.get('tweet')
    tweet_result = Twitter(
        auth=OAuth(
            module.params.get('access_token'),
            module.params.get('access_token_secret'),
            module.params.get('consumer_key'),
            module.params.get('consumer_secret_key')
        ),
        domain=module.params.get('server'),
        secure=module.params.get('https')
    )
    try:
        tweet_result.statuses.update(status=tweet_text)
        changed = True
        module.exit_json(changed=changed, item={'tweet': tweet_text})
    except TwitterHTTPError as debug_info:
        for error in debug_info.response_data.get("errors"):
            if error.get("code") == 187:
                changed = False
                module.exit_json(
                    changed=changed,
                    item={
                        'tweet': tweet_text,
                        'debug_info': debug_info.response_data
                    }
                )
        failed = True
        module.exit_json(
            changed=changed,
            failed=failed,
            item={
                'tweet': tweet_text,
                'debug_info': debug_info.response_data
            }
        )


def main():
    """main method
    """
    tweet()


if __name__ == '__main__':
    main()
