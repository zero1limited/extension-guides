# CSS critical path



## Pitch
All CSS styles in core Magento are loaded from external files and considered render-blocking. This means that a web page will not be displayed properly until these files are loaded. By using ‘CSS critical path’, we deliver critical CSS in the page, this can significantly improve the time to first render. 

Please note, this is not a Silver Bullet solution and in many cases the estimated time is usually spent focussed on achieving fast loading of the predominant mobile header UX. This can some-times cause an initial stepped loading under certain circumstances (Ie. you have 3rd party fonts or services also causing render blocking) which might require furtherwork depending on the complexity of your theme. We ask that you take a very active role in reviewing our work before it is deployed. This will almost certainly lead to further work but ultimately will improve core web vitals scores and also lead to other recommendations around optimisation of 3rd party modules/assets.


## Estimation MINIMUM 1 day


## Instructions

Pauline Foxley has done this previously for Divine Trash
https://devdocs.magento.com/guides/v2.4/frontend-dev-guide/css-topics/css-critical-path.html

Notes to be developed, probably not a task which can be delegated or documented to much.

Key considerations on setting estimations and client expectations

- Do we just concentrate on homepage?
- Do we concentrate on mobile?

Are the above questions valid or is Arron misunderstanding?
