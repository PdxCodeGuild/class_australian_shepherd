# Class australian shepherd

Evening Python Fullstack bootcamp.
Aug 01 - Dec 12

![australian shepherd](auzzie.png)

Instructor:

- [Matthew Chimenti](http://www.github.com/ChimentiMatt)
- matt@pdxcodeguild.com

TAs:

- [Michael Broetje](http://www.github.com/cdmichaelb)
- broetjem+pdxcodeguild@gmail.com

- Timothy

<hr>

## Rough Timeline

- ~~Weeks 1, 2, 3, 4, 5: Python~~
- Weeks 6, 7: HTML/CSS/Flask
- Weeks 8, 9, 10, 11: Django
- Weeks 12, 13, 14, 15: Javascript
- Weeks 16, 17, 18: Capstone project

<hr>

## Scheduled Holidays (no class) To be confirmed

- ~~Sept 5 - Labor Day~~
- Oct 10 - Indigenous People's Day
- Nov 24 - Thanksgiving
- Nov 25 - Day after Thankgiving

<hr>

## Assigned Labs:

<details>
  <summary>Python</summary>

| Lab Number | Title                                                                                                                              | Due Date |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Lab 01     | Code Folder                                                                                                                        | 07 Aug   |
| Lab 02a    | [Mad Lib](1%20Python/labs/02a%20Mad%20Lib.md)                                                                                      | 08 Aug   |
| Lab 02b    | [Average Num](1%20Python/labs/03b%20AverageNum.md)                                                                                 | 08 Aug   |
| Lab 05     | [Palindrome Checker](1%20Python/labs/05a%20Palindrome%20Checker.md)                                                                | 10 Aug   |
| Lab 06b    | [Credit Card Validation](1%20Python/labs/06b%20Credit%20Card%20Validation.md)                                                      | 14 Aug   |
| Lab 08     | [Pick 6](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/08%20Pick6.md)                        | 15 Aug   |
| Lab 09     | [Blackjack Advice](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/09%20Blackjack%20Advice.md) | 21 Aug   |
| Lab 14     | [ARI](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/14%20ARI.md)                             | 22 Aug   |
| Lab 07     | [Rot 13](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/11%20Rot%20Cipher.md)                 | 22 Aug   |
| Lab 11     | [Contact List](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/17%20Contact%20List.md)         | 22 Aug   |
| Lab 14     | [ATM](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/14%20ATM.md)                             | 28 Aug   |
| Lab 19     | [Dad Joke API](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/10%20Dad%20Joke%20API.md)       | 29 Aug   |
| Lab 15     | [Quotes API](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/18%20Quotes%20API.md)             | 30 Aug   |
| Final      | [Mini Capstone](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/1%20Python/labs/MiniCapstone.md)               | 12 Sep   |

</details>

<details open>
  <summary>HTML/CSS/Flask</summary>

| Lab Number | Title                                                                                                                                                          | Due Date |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Lab 01     | [Bio](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/labs/01%20Bio.md)                                 | 19 Sep   |
| Lab 02     | [Blog](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/labs/02%20Blog.md)                               | 21 Sep   |
| Lab 03     | [Company](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/labs/03%20Company.md)                         | 25 Sep   |
| Lab 04     | [Personal Portfolio](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/labs/04%20Personal%20Portfolio.md) | 29 Sep   |
| Lab 06     | [Flask Redo](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/2%20Flask%20%2B%20HTML%20%2B%20CSS/labs/06%20Flask%20Redo.md)                 | 31 Sep   |

</details>

<details>
  <summary>Django</summary>

| Lab Number | Title                                                                                                                    | Due Date |
| ---------- | ------------------------------------------------------------------------------------------------------------------------ | -------- |
| Lab 01     | [Django Redo](https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/3%20Django/labs/01%20Django%20Redo.md) | 27 JUL   |

</details>

<hr>

## Submitting your work

Make sure all labs are located within `class_australian_shepherd/code/<YOUR_NAME>`, where `<YOUR_NAME>` is your first name in all lowercase letters.

To emulate a more professional Git workflow, we're going to start creating new branches for each lab starting in the HTML/CSS section.

<h2>Creating a new branch:</h2>
<details>
<summary>Click to expand</summary>

- `git branch` to check that you're on the main branch, use `git checkout main` to go to the main branch if needed.

- `git status` to check if your local main branch is up to date with origin/main on Github.
- `git pull` if needed to pull any recent changes to your local repository

- Create a new branch and switch to it.

  - Option 1:

    - `git branch <YOUR_NAME-SECTION-LAB_NUMBER>`
    - `git checkout <YOUR_NAME-SECTION-LAB_NUMBER>`

  - Option 2:

    The `-b` flag can be used after the `checkout` command to combine these two steps:

    `git checkout -b <YOUR_NAME-SECTION-LAB_NUMBER>`

  **e.g.** My branch for the **"Lab 01 - Bio"** in the **HTML/CSS** section would be named: `matt-htmlcss-lab01`. The name can vary a bit from this example, but please keep the chosen formatting consistent from one lab to another.

- `git add <FILENAME>` to add a specific file or `git add .` to add everything in the current dicrectory
- `git commit -m "your commit message"` to commit your work

- A remote branch will need to be created for each new local branch. Git will usually display the proper command to do this when a new branch is pushed for the first time.

  The command is:

  `git push --set-upstream origin <BRANCH_NAME>`

  **OR**

  `git push -u origin <BRANCH_NAME>`

  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/set_upstream_message.png" width=800>
  </details>

- After successfully pushing your new branch to Github, you should see the option to create a Pull Request for your branch on the main repo page.

  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/pull_request_button.png" width=800>
  </details>

- If you don't see that message, you'll have to navigate to your new remote branch
  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/switch_branch.gif" width=800>
  </details>

- Once you've navigated to your individual branch, you'll find the option to create a Pull Request in the "Contribute" dropdown.
  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/open_pull_request_alternative.gif" width=800>
  </details>

- Click the "Open Pull Request" button. Add a comment to your Pull Request like "Submitting Lab 00" and click "Create Pull request"
  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/create_pull_request.png" width=800>
  </details>
</details>

## Updating a branch

<details>
<summary>Click to expand</summary>
After a Pull Request is submitted, the code on that branch will be checked.

Necessary corrections or adjustments will be posted as comments on the Pull Request on Github and the Pull Request will be closed. When the corrections are made, submit the Pull Request again for checking.

Corrections will be made only to that particular branch.

- `git checkout <YOUR_NAME-SECTION-LAB_NUMBER>`

- Add and commit updated files.

- `git push` to push your changes up to the remote repository on GitHub

- Only one Pull Request is allowed per branch.

  - If a Pull Request is already open for the branch, a message will be added to the current Pull Request for the new commits.
  - If a Pull Request is not already open for the branch a new Pull Request will need to be created.

- Once a lab is complete, its branch will be merged into the `main` branch.
</details>

---
