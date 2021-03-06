from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('P09ndUaX/cr0SJ/I1IXWzFfMEaF+BFYqqhOQLJBNZv7ns4CDxxF51drFub4h3NLArMb5leqJg3qCr+/+Wh+dsTDxslN0CVxSZ7eAsPY9tjf34SWrS0ldwJPZlpWaVEuN9akPBGI8kUEd2VVkeQizSgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0756deb9a91a508295cd005a9e50647b')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text

    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID
    elif(text=="你好"):
        reply_text = "哈囉"
    elif(text=="機器人"):
        reply_text = "叫我嗎"
    else:
        reply_text = text

if __name__ == "__main__":
    app.run()