Quiz
====

Play a kahoot-like trivia game with questions from Open Trivia Database.
Originally by Keane for Red v2

<<<<<<< HEAD
# <@1275521742961508432>quiz
=======
# ,quiz
>>>>>>> 9e308722 (Revamped and Fixed)
Play a kahoot-like trivia game.<br/>
Questions from the Open Trivia Database.<br/>

In this game, you will compete with other players to correctly answer each<br/>
question as quickly as you can. You have 10 seconds to type the answer<br/>
choice before time runs out. The longer you take to say the right answer,<br/>
the fewer points you get. If you get it wrong, you get no points. Only the<br/>
first valid answer (A, B, C, or D) will be recorded - be sure of the<br/>
answer before replying!<br/>

To end the game, stop responding to the questions and the game will time out.<br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>quiz`
 - Checks: `server_only`


## <@1275521742961508432>quiz play
Create or join a quiz game.<br/>
Specify a category name or ID number, otherwise it will be random.<br/>
Use <@1275521742961508432>quiz categories to list category names or id numbers.<br/>
 - Usage: `<@1275521742961508432>quiz play [category_name_or_id]`
=======
 - Usage: `,quiz`
 - Checks: `server_only`


## ,quiz categories
List quiz categories.<br/>
 - Usage: `,quiz categories`


## ,quiz play
Create or join a quiz game.<br/>
Specify a category name or ID number, otherwise it will be random.<br/>
Use ,quiz categories to list category names or id numbers.<br/>
 - Usage: `,quiz play [category_name_or_id]`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### category_name_or_id=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```


<<<<<<< HEAD
## <@1275521742961508432>quiz categories
List quiz categories.<br/>
 - Usage: `<@1275521742961508432>quiz categories`


# <@1275521742961508432>quizset
Quiz settings.<br/>
 - Usage: `<@1275521742961508432>quizset`
=======
# ,quizset
Quiz settings.<br/>
 - Usage: `,quizset`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Restricted to: `MOD`
 - Checks: `server_only`


<<<<<<< HEAD
## <@1275521742961508432>quizset afk
Set number of questions before the game ends due to non-answers.<br/>
 - Usage: `<@1275521742961508432>quizset afk <questions>`
Extended Arg Info
> ### questions: int
> ```
> A number without decimal places.
> ```


## <@1275521742961508432>quizset questions
Set number of questions per game.<br/>
 - Usage: `<@1275521742961508432>quizset questions <questions>`
=======
## ,quizset questions
Set number of questions per game.<br/>
 - Usage: `,quizset questions <questions>`
>>>>>>> 9e308722 (Revamped and Fixed)
Extended Arg Info
> ### questions: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
## <@1275521742961508432>quizset show
Toggle revealing the answers.<br/>
 - Usage: `<@1275521742961508432>quizset show`


## <@1275521742961508432>quizset multiplier
=======
## ,quizset show
Toggle revealing the answers.<br/>
 - Usage: `,quizset show`


## ,quizset multiplier
>>>>>>> 9e308722 (Revamped and Fixed)
Set the credit multiplier.<br/>
The accepted range is 0 - 10000.<br/>
0 will turn credit gain off.<br/>
Credit gain will be based on the number of questions set and user speed.<br/>
1x = A small amount of credits like 1-10.<br/>
100x = A handful of credits: 100-500.<br/>
10000x = Quite a lot of credits, around 10k to 50k.<br/>
        <br/>
<<<<<<< HEAD
 - Usage: `<@1275521742961508432>quizset multiplier <multiplier>`
=======
 - Usage: `,quizset multiplier <multiplier>`
>>>>>>> 9e308722 (Revamped and Fixed)
 - Checks: `check_global_setting_admin`
Extended Arg Info
> ### multiplier: int
> ```
> A number without decimal places.
> ```


<<<<<<< HEAD
=======
## ,quizset afk
Set number of questions before the game ends due to non-answers.<br/>
 - Usage: `,quizset afk <questions>`
Extended Arg Info
> ### questions: int
> ```
> A number without decimal places.
> ```


>>>>>>> 9e308722 (Revamped and Fixed)
