# ansible_twitter_module

## command example

```
# ansible-playbook -c local -e"tweet=This tweet posted by ansible module" -i hosts tweet_playbook.yml
```

## Feature

This module post tweet to twitter.

# Requirements

python version: 3
This module needs python twitter module.

```
# pip install twitter
```

need to generated twitter access token.

# Use Case
receive notification via twitter.