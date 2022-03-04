# Программирование
## mkalinin
### Markdown
Markdown is a way to style text on the web. You control the display of the document
### Examples 
It's very easy to make some words **bold** and other words *italic* with Markdown. You can even [link to Google!](http://google.com)
### Syntax guide
Here’s an overview of Markdown syntax that you can use anywhere on GitHub.com or in your own text files.
#### Headers
# This is an <h1> tag
## This is an <h2> tag
###### This is an <h6> tag
#### Emphasis 
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_
#### Lists
##### Unordered
* Item 1
* Item 2
  * Item 2a
  * Item 2b
##### Ordered
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
#### Images 
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
#### Links
http://github.com - automatic!
[GitHub](http://github.com)
#### Blockquotes
As Kanye West said:

> We're living the future so
> the present is our past.
#### Inline code
I think you should use an
`<addr>` element here instead.
### GitHub Flavored Markdown
GitHub.com uses its own version of the Markdown syntax that provides an additional set of useful features, many of which make it easier to work with content on GitHub.com.
#### Syntax highlighting
Here’s an example of how you can use syntax highlighting with GitHub Flavored Markdown:
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```
#### Tasks Lists
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
If you include a task list in the first comment of an Issue, you will get a handy progress indicator in your issue list. It also works in Pull Requests!
#### Tables
You can create tables by assembling a list of words and dividing them with hyphens - (for the first row), and then separating each column with a pipe |:
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
#### Username @mentions
Typing an @ symbol, followed by a username, will notify that person to come and view the comment. This is called an “@mention”, because you’re mentioning the individual. You can also @mention teams within an organization.
#### Automatic linking for URLs
Any URL (like http://www.github.com/) will be automatically converted into a clickable link.
#### Strikethrough
Any word wrapped with two tildes (like ~~this~~) will appear crossed out.
#### Emoji
GitHub supports emoji!

To see a list of every image we support, check out the Emoji Cheat Sheet.