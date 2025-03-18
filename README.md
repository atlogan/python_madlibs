Challenges Completed
1. Replay Feature
Implemented a loop that asks users if they want to play again after each round.
If the user types “yes,” the game restarts; otherwise, it displays a farewell message and exits.
This feature was developed on a separate feature branch (replay_feature) before being merged into main.
2. Function Refactoring
Broke down the script into modular functions:
get_user_input(): Handles input collection.
build_story(): Constructs the Mad Libs story.
play_mad_libs(): Runs a single instance of the game.
main(): Manages the replay loop.
This makes the code easier to maintain and extend in the future.

Why I Chose These Challenges
Replay Feature: I wanted to make the game more interactive and user-friendly. Without it, the game would require restarting the script manually after each round.
Function Refactoring: Writing modular code improves readability, makes debugging easier, and allows future enhancements without breaking existing functionality.

Reflection Questions & Answers
1. What was the most interesting or surprising part of implementing your chosen feature(s)?
The most interesting part was seeing how small improvements, like refactoring code into functions, made the program much more structured. The replay feature also made the game feel more interactive, which was fun to implement.
2. What was the greatest obstacle or bug you faced, and how did you overcome it?
One challenge was handling user input properly, ensuring that unexpected inputs (like empty strings or extra spaces) didn’t break the story. I solved this by using .strip() to clean inputs and making sure they weren’t left blank before proceeding.
3. How did the feature branch and merge workflow help in organizing your code changes?
Creating a separate branch (replay_feature) allowed me to develop and test the replay feature without affecting the main branch. After verifying it worked correctly, merging it back into main ensured that the final version was stable. This approach helped me track progress and avoid breaking the working code.
4. What Python concepts (e.g., conditionals, loops, functions, file I/O) do you feel more confident in after completing this assignment?
I feel more confident in functions and loops after structuring the code into modular functions and implementing the replay loop. Additionally, working with string formatting (f-strings) and user input handling improved my understanding of building interactive scripts.

How to Run the Program
Clone this repository:
 git clone https://github.com/atlogan/python_madlibs.git
cd python_madlibs


Run the script:
 python mad_libs.py
