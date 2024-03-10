# Building the console
Scrapbook to organize thoughts as we build out the AirBnB command line interpreteter.

## [cmd](https://docs.python.org/3.8/library/cmd.html#module-cmd) — Support for line-oriented command interpreters

The `Cmd` class provides a simple framework for writing line-oriented command interpreters. These are often useful for test harnesses, administrative tools, and prototypes that will later be wrapped in a more sophisticated interface.

A `Cmd` instance or subclass instance is a line-oriented interpreter framework. There is no good reason to instantiate `Cmd` itself; rather, it’s useful as a superclass of an interpreter class you define yourself in order to inherit `Cmd`’s methods and encapsulate action methods.

## Important concepts 🎓

Cmd.cmdloop(intro=None) stands ready to initiate a continuous cycle of actions:

Displays an optional welcome message: If you provide an intro string, it'll greet the user before starting the interaction.
Engages in conversation: It repeatedly presents a prompt, eagerly awaiting your input.
Scrutinizes your input: It diligently breaks down your commands, focusing on the first word as the key action.
Dispatches tasks to dedicated specialists: It calls upon specific methods (do_something()) to handle each command, passing along any additional words as instructions.
Here are some helpful insights for crafting command-driven conversations:

Help is always at hand: Every Cmd subclass inherits a built-in do_help() method. It's ready to provide guidance for specific commands or offer a comprehensive overview of available commands.
Deciding when to wrap up: The conversation gracefully concludes when postcmd() signals its approval by returning True.
Handling unexpected endings: If the conversation comes to an abrupt halt (like encountering an end-of-file), Cmd.cmdloop() remains composed and passes back the string 'EOF'.
Recognizing familiar faces: Cmd interpreters are remarkably perceptive. They'll recognize a command named "foo" only if they have a corresponding "do_foo()" method.
Always eager to assist: Cmd interpreters are exceptionally helpful. They’ll prioritize any line starting with '?' as a request for do_help(), and they’ll eagerly pass requests beginning with '!' to do_shell() (if it exists).
Learning to anticipate unexpected events: It’s wise to implement a do_EOF() method for graceful error handling.
Respecting silence: To override the default behavior when an empty line is entered, implement the emptyline() method.
