# Contributing

Thank you for taking the time to learn how to contribute! Not only reading this help your contribution to get more likely accepted, it'll help you in the future for all projects made from the [ThatXliner/Pytemplate](https://github.com/ThatXliner/Pytemplate) template!

## Styles

All kinds of styles (e.g. code style, git commit style, comment style, etc) will be discussed here.

### Python

#### General code style

Most of the code style is covered by our preferred formatter, black (<sub><a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a></sub>).

The hard line limit (in characters) is `90`. The soft limit is `80` to `88`. But it is recommended to set your editor's soft wrap at 88 characters.

Tab size 4 spaces, spaces style.

### Git commit messages

I must admit, I personally don't like to write detailed commit messages. But now, I find a need to. So, here is the `git` commit message writing guidelines.

#### General convention

For git commit messages, it is recommended to write them in past tense (e.g. `Added`, `Updated`) and with `Title Case`.

Also, try to add emojis as needed. See [below](#commit-message-emojis-and-meaning). After that, you'd want to seperate the emojis with the actual commit message. You can do so like this (where you replace `*example emoji*` with the emojis required):

```
*example emoji*: Added Example_file.txt

Why and where. [skip ci]
```

OR

```
*example emoji* -> Added Example_file.txt

Why and where. [skip ci]
```

OR

```
*example emoji* - Added Example_file.txt

Why and where. [skip ci]
```

If the commit was made by a robot, you should prefix it with a <code>:robot:|:some_other_emoji:</code>

#### Commit message emojis and meaning

NOTICE: Any emoji specified here _are **not**_ only limited to only one skin tone: This list just includes one for simplicity. Also, **it is preferred to use Github flavored markdown emoji shortcuts for it will automatically take care of different encoding schemes et cetera. If there are more shortcuts not listed here, let me know.** [Contact me](#owner-thatxliner-bryan-hu).

It is recommended to stick to one constuct in a commit message: either completely use [**GFM emoji shortcuts**](https://gist.github.com/rxaviers/7360908 "Complete list of github markdown emoji markup") or use Unicode emojis.

TODO: Add GFM emoji shortcuts

**Dependency related emojis:**

- :arrow_up:(`:arrow_up`): Increased dependencies
- :arrow_down:(`:arrow_down`): Decreased dependencies

**File related emojis:**

- :fire:(`:fire:`): Removed files
- :memo: (`:memo:` or `:pencil:`): Added files
- :pencil2: (`:pencil2:`): Edited files
- :art:(`:art:`) or :sparkles:(`:sparkles:`) or :star2:(`:star2:`) or :star:(`:star`): Beautified file
  - ⚫️: Beautified with black

**OS dependent emojis:**

- :apple:(`:apple:`): MacOS related commit
- :penguin:(`:penguin:`): Linux related commit
- :computer:(`:computer:`) or :desktop_computer:(`:desktop_computer:`): Windows related commit

**Bug related emojis:**

- :white_check_mark:(`:white_check_mark:`) or :bug:(`:bug:`): Fixed a bug
- :x:(`:x:`): Introduced a bug
  Possibilities:
- :warning: (`:warning:`) or :grimacing:(`:grimacing:`): Possibly introduced a bug
- :cyclone:(`:cyclone:`): Possibly *fixed* a bug

**Language-related emojis:**

- :snake:(`:snake:`): Edited a python (or Python related) file. Required if it isn’t the default language
- 🦪 or :turtle:(`:turtle:`) or :green_circle:(`:green_circle:`): Edited a shell/bash (or shell/bash related) file. Required if it isn’t the default language

**Efficiency, speed, etc:**

- :battery:(`:battery:`) or ⚡️ or 🏃‍♀️ or 🏃 or 🏃‍♂️: Increased speed

**Idea related emojis:**

- :thinking:(`:thinking:`): Possible idea
- 💡: Idea
- :zany_face:(`:zany_face:`): Crazy idea

**General emojis:**

- :+1:(`:+1:` or `:thumbsup:`): Good or yes or accept
- :-1:(`:-1:` or `:thumbsdown:`): Bad or no or object
- :handshake:(`:handshake:`): Agreement or compromise

**Miscellaneous emojis:**

- :robot:(`:robot:`): Bot-created commit
- 👨 or 🧔: Travis CI related commit
- :octocat: (`:octocat:`): GitHub-related commit
Example Git commit message:

```
:memo: :art: :black_circle: : Added __main__.py
```

### Pull request messages

TK.


### Files and folders

Try to keep the file names and folder names `lowercase`. This is because **some systems treat folder/filenames case insensitively**.

## Contacts

Contact contributors' here.

**Contributors:**

Don't see you contact info here? Submit a pull request adding your contact info to this section.

### [OWNER] ThatXliner (Bryan Hu)

Contact ThatXliner (Bryan Hu) at

- Email: [`bryan.hu.2020@gmail.com`](mailto:bryan.hu.2020@gmail.com "Email ThatXliner")
- Discord username: `ThatXliner#1995`
