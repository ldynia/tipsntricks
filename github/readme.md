# Question

I have a question regarding data being send to Copilot for training. According to what-data-does-github-copilot-collect it says that:

> Depending on your preferred telemetry settings, GitHub Copilot may also collect and retain the following, collectively referred to as “code snippets”: source code that you are editing, related files and other files open in the same IDE or editor, URLs of repositories and files pat

So if my Visual Studio Code workspace has opened 20 projects that are mixed between private, enterprise or open-source repositories then, above sentence would indicate that the data from my IDE would be sent to Copilot for training?

# Answer

As mentioned, I asked my team about this and this was their reply:

> Yes, files visible to the editor may become part of the prompt which is used to compute the completion. If the customer is concern about this they may disable collection of that telemetry which will not prevent it being sent to copilot for construction of a prompt, but it will not be retained.

Let me know if you have any follow-up questions.
