# ansible_twitter_module

## command example

```
# ansible-playbook -c local -e"tweet=このTweetはansible-playbookで行っています。" -i hosts tweet_playbook.yml
```

## 機能など

つぶやき投稿する以外の機能はないです。そのうち実装するかも

# 動作要件

python 3 でしか動きません。
python twitter モジュールを前提にしてます。

```
# pip install twitter
```

twitterのアクセストークンなどは各自取得が必要です。sample playbookのvarsに記載されている各変数を設定してください。

# 冪等性

実装してないけど、同じTweetをすでにしてたらつぶやかない、または古いのを消してつぶやき直すなどを検討。
リツイートでこれやって、定期ポストの支援に使うのも良いね。
