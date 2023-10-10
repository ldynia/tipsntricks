
https://documentation.mailgun.com/en/latest/quickstart-sending.html#send-via-smtp

```bash
$ curl -s --user 'api:<API Key>' \
    https://api.mailgun.net/v3/<DOMAIN>.mailgun.org/messages \
    -F from='noreply@food.dtu.com' \
    -F to=ludd@food.dtu.dk \
    -F subject='Hello' \
    -F text='Testing some Mailgun awesomeness!'

$ ./swaks --auth \
      --server smtp.mailgun.org:587 \
      --au <Default SMTP Login> \
      --ap <Default Password> \
      --from noreply@food.dtu.dk \
      --to ludd@food.dtu.dk \
      --h-Subject: "Hello" \
      --body 'Testing some Mailgun awesomness!'
```
