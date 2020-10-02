---
layout: lesson
root: .  # Is the only page that doesn't follow the pattern /:path/index.html
permalink: index.html  # Is the only page that doesn't follow the pattern /:path/index.html
---
![](assets/img/abcd_letters.png)

> ## Prerequisites
> In order to complete this lesson you need
> - [ROOT CERN](https://root.cern/) 6.16 or later installed. You can set up ROOT as recommended [here](https://cms-opendata-workshop.github.io/workshop-lesson-root/02-get-root/index.html).
> - The [Higgs to tau tau analysis example code](https://github.com/cms-opendata-analyses/HiggsTauTauNanoAODOutreachAnalysis) installed and running.
> A stable internet connection to access the input data.
{: .prereq}

> ## Helpline
> Instructions written by **Santeri Laurila** (CERN). All example code we use is written by **Stefan Wunsch** (CERN). You can reach us by email (firstname.lastname@cern.ch).
{: .callout}

Welcome! This lesson will teach you the basics of a commonly used background estimation known as the ABCD method.

We will apply this method to estimate the QCD background in the Higgs to tau tau analysis example.

<!-- this is an html comment -->

{% comment %} This is a comment in Liquid {% endcomment %}

{% include links.md %}

> ## Input data 
> The data used in this lesson are in pre-processed "NanoAOD" datasets, which are listed [here](http://opendata.web.cern.ch/record/12350). 
> The code will access this data automatically, so you don't need to download it manually.
{: .callout}
