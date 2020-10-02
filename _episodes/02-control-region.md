---
title: "Control regions"
teaching: 10
exercises: 10
questions:
- "What is a control region? How should we select our control region C?"
objectives:
- "Understand the concept of control region"
- "Learn the required features for a good control region"
- "See how the control region is defined in Higgs to tau tau analysis example"
keypoints:
- "Data-driven background estimates are a must in situations where you cannot get a reliable estimate from simulation"
- "They are also useful to validate predictions from simulations"
- "The ABCD method is a common background estimated concept, based on four different regions in phase space"
- "In this method, background shape in the signal region is estimated using a control region"
- "Differences between the control region and signal region are accounted for by event weights called transfer factors"
---

## Control regions

FIXME

## Role of control region C

![](assets/img/abcd_diagram.png)

FIXME


## Definition of control region C in the Higgs to tau tau analysis example

https://github.com/cms-opendata-analyses/HiggsTauTauNanoAODOutreachAnalysis/blob/master/histograms.py#L120

~~~
        # Book histograms for the signal region
        df1 = df.Filter("q_1*q_2<0", "Require opposited charge for signal region")
        df1 = filterGenMatch(df1, label)
        hists = {}
        for variable in variables:
            hists[variable] = bookHistogram(df1, variable, ranges[variable])
        report1 = df1.Report()

        # Book histograms for the control region used to estimate the QCD contribution
        df2 = df.Filter("q_1*q_2>0", "Control region for QCD estimation")
        df2 = filterGenMatch(df2, label)
        hists_cr = {}
        for variable in variables:
            hists_cr[variable] = bookHistogram(df2, variable, ranges[variable])
        report2 = df2.Report()
~~~
{: .python}

Task: run histograms.py and inspect the histograms with ROOT TBrowser.

{% include links.md %}

