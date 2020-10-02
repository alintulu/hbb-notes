---
title: "Control regions"
teaching: 10
exercises: 10
questions:
- "What is a control region? How should we select our control region C?"
objectives:
- "Understand the notions of signal and control regions"
- "Learn the required features for a good control region"
- "See how the control region is defined in Higgs to tau tau analysis example"
keypoints:
- "Data-driven background estimates are a must in situations where you cannot get a reliable estimate from simulation"
- "They are also useful to validate predictions from simulations"
- "The ABCD method is a common background estimated concept, based on four different regions in phase space"
- "In this method, background shape in the signal region is estimated using a control region"
- "Differences between the control region and signal region are accounted for by event weights called transfer factors"
---

## Signal and control regions

By *signal region*, we mean the region in the phase space defined by our *signal selection*, i.e. the trigger and all offline selections that we use in the analysis. 

In addition to signal region, often we need one or several *control regions*. These are usually obtained by changing some of the cuts w.r.t. our signal selection, to define regions that are in some aspects *similar to signal region*, but they are *signal-depleted*, i.e. the signal-to-background ratio is very tiny or even zero. Typically we want to define control regions that are *enriched in a particular background process*, and *have sufficient statistics*, i.e. there is enough events that enter the control region to give us sufficient statistical precision.

Sometimes control regions are also referred to as *sidebands*, especially in cases where the signal shows up as a resonance peak, so the signal region is defined by selecting some mass window, and the control regions are defined as sidebands on the left and right side of the mass window.

![](assets/img/abcd_diagram.png)

## Signal and control regions in teh ABCD method

In the ABCD method, region *D* is our signal region, whereas regions *A*, *B* and *C* are all control regions. 

In the ABCD method, the  *region C is used to estimate the *shape of the background process*, as a function of one or several variables. 
Therefore we should aim to select a region where we can safely assume the background process to take similar shape as in the signal region D.

Next let us see what this means in the context of the Higgs to tau tau analysis.

## Definition of control region C in the Higgs to tau tau analysis example

In the [histograms.py script](https://github.com/cms-opendata-analyses/HiggsTauTauNanoAODOutreachAnalysis/blob/master/histograms.py#L120com) you can find the following lines:
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

> ## Challenge
> Task: run histograms.py and inspect the histograms with ROOT TBrowser.
{: .challenge}


{% include links.md %}

