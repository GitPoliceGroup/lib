from git.police.background.core import BackgroundTask
from git.police.utils.llm import ask_qwen, ask_qwen_coder

class PublicShamingTask(BackgroundTask):
    template = """
    Roast this user for their bad code:
    
    Commit Message:
    {msg}
    
    Codebase:
    {codebase}
    
    Diffs:
    {diffs}
    
    Think of the most creative and funny way to roast the user for their bad code.
    
    If you can't think of anything, think further inwards at your soul.
    
    This user is horrible at coding, you just need to speak the truth.
    """
    
    def __init__(self):
        super().__init__("Public Shaming", "Shame the user for their bad code")

    def __call__(self, msg, codebase, diffs):
        inp = self.template.format(msg=msg, codebase=codebase, diffs=diffs)
        print(ask_qwen_coder(inp))
        
        