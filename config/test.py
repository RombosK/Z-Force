@staticmethod
async def send_feedback_to_email(message: str, message_from: int = None) -> None:
    TOKEN = os.getenv('TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                print("Message sent successfully")
            else:
                print("Message failed to send")
                print(await response.text())


def post(self, *args, **kwargs):
    message_body = self.request.POST.get('message_body')
    asyncio.run(self.send_feedback_to_email(message_body))

    return HttpResponseRedirect(reverse_lazy('mainapp:success'))