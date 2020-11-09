#!/usr/bin/python
"""tweet module for ansible
 Copyright: (c) 2020, Daisuke Matsui <dmatsui@redhat.com>
"""

import sys
from ansible.module_utils.basic import AnsibleModule
from twitter import Twitter, OAuth


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
    tweet: "nya-n"
    consumer_key: "{{ consumer_key }}"
    consumer_secret_key: "{{ consumer_secret_key }}"
    access_token: "{{ access_token }}"
    access_token_secret: "{{ access_token_secret }}"
'''

RETURN = '''
'''


def tweet():
    """tweet post method
    """
    module = AnsibleModule(
        argument_spec={
            'state': {'required': False, 'default': 'present'},
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
        )
    )
#    try:
#        tweet_handle = tweet_result.statuses.update(status=tweet_text)
#        changed = True
#    except:
#        print("error!", file=sys.stderr)
#        changed = False
#        module.exit_json(changed=changed, item={'tweet': tweet_text})
    tweet_handle = tweet_result.statuses.update(status=tweet_text)
    print("DEBUG: tweet_handle", file=sys.stderr)
    print(vars(tweet_handle), file=sys.stderr)
    print("DEBUG: tweet_handle.headers", file=sys.stderr)
    print(vars(tweet_handle.headers), file=sys.stderr)
    changed = True
    module.exit_json(changed=changed, item={'tweet': tweet_text})


def main():
    """main method
    """
    tweet()


if __name__ == '__main__':
    main()
