
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

line_bot_api = LineBotApi('MUiwk2cGpSoGhU6BTnzFv8EOrI1cw996zC9P8JMbWKlP7ZXGYLzeitb9I1KGjOHO6x3YWMJXtEOi60kYLlH0WKFNzZgEmmUpSU4cAhm8d6QzJeSM4g2VTUsRC/eHvZQ2GEirReomnrKmcl4Jkx6/7wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cffb51c3dbb368a9cacb97b60fa36663')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()