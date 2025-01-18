from git_police.background.core import BackgroundTask
from git_police.utils.llm import ask_qwen, ask_qwen_coder

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
    
    Insult begins here: <begin_insult>
    """
    
    def __init__(self):
        super().__init__("Public Shaming", "Shame the user for their bad code")

    def __call__(self, msg, codebase, diffs):
        print("Codebase")
        print(codebase)
        print()
        print("Diffs")
        print(diffs)
        print()
        inp = self.template.format(codebase=codebase, diffs=diffs).strip()
        print(ask_qwen(inp))
        
        