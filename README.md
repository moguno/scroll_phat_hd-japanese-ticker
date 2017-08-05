# scroll_phat_hd-japanese-ticker

Raspberry PiのScroll pHat HDで、日本語のメッセージを流すやつ

## 使い方

misaki.pyをいつものPythonスクリプトとおんなじ感じで起動してください。
デフォルトでは時計が流れます。

時計に物足りなさを感じたら、weather.pyやexchange.pyを起動してみてください。
天気やドル円の情報が流れ出すと思います。

それにも飽きたらこんなコマンドを打ってみてください。

```
echo -e "test\tてすと" | nc localhost 39114
```

チャンネル名とメッセージをタブ区切りする感じです。

メッセージを書き換えたい場合は、同じチャンネル名で新しいメッセージを投げてください。

メッセージを消したい場合は、チャンネル名とタブだけを渡してください。
