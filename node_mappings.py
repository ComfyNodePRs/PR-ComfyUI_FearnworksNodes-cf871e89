try:
    from .nodes.loading_utils import *
    from .nodes.token_utils import *
except ImportError:
    print("\033[34mFearnworks Custom Nodes: \033[92mFailed to load nodes\033[0m")
    pass


NODE_CLASS_MAPPINGS = {
    "CountTokens": CountTokens,
    "FileCountInDirectory": FileCountInDirectory,
    "TokenCountRanker": TokenCountRanker,
    "TrimToTokens": TrimToTokens,
    "LoadRandomImageFromDirectory": LoadRandomImageFromDirectory
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CountTokens": "🔍 FW Count Tokens",
    "FileCountInDirectory": "📜 FW File Count In Directory",
    "TokenCountRanker": "🔍 FW Token Count Ranker",
    "TrimToTokens": "✂️ FW Trim To Tokens",
    "LoadRandomImageFromDirectory": "📸 FW Load Random Image (Directory)"
}