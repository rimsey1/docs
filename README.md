## Cyclr Documentation v2

You can use the [editor on GitHub](https://github.com/cyclr/docs/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing.

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Setting up your GitHub Pages site locally with Jekyll

1. If you don't have Docker installed, install [Docker](https://docs.docker.com/install/).
2. Open the terminal.
3. On your local computer, clone the Git repository for Cyclr Documentation:
```Shell
$ git clone https://github.com/cyclr/docs.git
```
4. Start up the application:
```Shell
$ docker-compose up
```

### Gems and plugins
See the Gemfile and \_config.yml for plugins.

Refer to the gem git repo README files for installation and usage.

| plugin | github |
| --- | --- |
| jekyll-seo-tag | https://github.com/jekyll/jekyll-seo-tag |
| jekyll-redirect-from | https://github.com/jekyll/jekyll-redirect-from |
| jekyll-toc | https://github.com/toshimaru/jekyll-toc |
| jekyll-menus | https://github.com/forestryio/jekyll-menus |


### Sidebar Menu
The sidebar menu is implemented with the jekyll-menus plugin. This relies on front matter, any pages which don't have the required front matter are omitted from the menu.

See https://github.com/forestryio/jekyll-menus for details.

This implementation includes customisations :
| customisation | where | description |
| --- | --- | --- |
| externalurl | front matter | Use externalurl instead of url to open the page in a new tab or window |
| toggleonly | front matter | Add toggleonly: true if the front matter is used to provide a toggle to control a nested menu. For those items, the md file includes front matter only, with no other content  |
| menu object parse | \_includes/generic/menu.html | Renders a link with no href to provide the toggle for the submenu display |


### Pages and front matter
All v2 pages are defined in the pages/v2 folder.
The pages should be organised in sub folders which reflect the relationship between pages and group them logically. In practice the folder structure reflects the sidebar menu structure.

Note that the menu struture is managed via the front matter in each md file, not via the page/v2 structure. #


This allows for the displayed menu options - the menu text, behaviour ( toggle submenu or go to a page) , link type ( same browser window or new window) - to be managed via front matter. 

The numeric prefix is used to control the order in which the options are displayed. The jekyll-menus plugin builds the data object from the md front matter, appending the relevant data from each file to its arrays. Amend the numeric prefixes to achieve the required menu option order.

#### Omit page from menu
To prevent a page appearing as a menu item, remove the 'menus' item and its children from the front matter. 

#### index.md
This provides the front matter for each sub menu.

##### No content
When the page md is defined to provide a submenu toggle

| item | description |
| --- | --- |
| [parentmenuid] | child of the menus front matter item - this defines the immediate parent of this page |
| title | The menu item text  |
| identifier | this menu id - to be used as the [parentmenuid] in any child pages |
| togglonly | must be used to render a link with no href |
| weight | can be used to control menu item order |


### Application Connector Guides
 