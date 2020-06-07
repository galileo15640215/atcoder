class BrowserHistory:
    stack = []
    pre = []
    home = ""
    def __init__(self, homepage: str):
        self.stack = []
        self.pre = []
        self.stack.append(homepage)
        self.home = homepage

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.pre = []

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.stack) == 1:
                return self.home
            self.pre.append(self.stack.pop(-1))
        return self.stack[-1]

    def forward(self, steps: int) -> str:
        if steps > len(self.pre):
            steps = len(self.pre)
        for i in range(steps):
            self.stack.append(self.pre.pop(-1))
        return self.stack[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)