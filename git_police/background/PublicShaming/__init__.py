from git_police.background.core import BackgroundTask
from git_police.utils.llm import ask_qwen, ask_qwen_coder
from git_police.utils.telegram_bot import send_telegram_message
import subprocess

class PublicShamingTask(BackgroundTask):
    template = """
    You are an intelligent and highly experience programmer. You are in charge of giving harsh code reviews to interns who keep coding stuff that is highly useless and horrible.
    
    You are to make a lighthearted jab at the intern for their horrible code, in a creative and funny manner to encourage them to improve their code, since they only respond to lighthearted jabs. 
    
    This intern is horrible at coding so make sure to be as savage as possible.
    
    Provide your insult in Markdown format. Something I can send in a Telegram message with relative ease.
    
    EXAMPLE: Your code is so bad, I thought AI wrote it...
    
    Edit the example above to make a lighthearted roast at the person. Address the person directly.
    
    DO NOT INCLUDE CODE IN YOUR RESPONSE. SIMPLY INSULT THE INTERN. KEEP YOUR RESPONSE SHORT, MAXIMUM NUMBER OF WORDS SHOULD BE 20!

    Below are the changes that the intern made to the codebase:
    
    {diffs}
    
    If there is no context, just generate a random insult on the code! Please generate only the insult
    """
    
    def __init__(self):
        super().__init__("Public Shaming", "Shame the user for their bad code")

    def __call__(self, msg = "", codebase = "", diffs = ""):
        try:
            res = subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE)
            username = res.stdout.strip().decode()
        except:
            username = "Anonymous"

        print("Commencing Public Shaming...")
        inp = self.template.format(codebase=codebase, diffs=diffs).strip()
        reply = ask_qwen(inp)

        # start = reply.find("<begin_insult>")
        # end = reply.find("</begin_insult>")
        # reply = reply[start+len("<begin_insult>"):end]

        send_telegram_message(f"Hey {username}! We analyzed your code\n" + reply)