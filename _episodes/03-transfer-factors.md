---
title: "Transfer factors"
teaching: 10
exercises: 10
questions:
- "What is a transfr factor? How can we derive our transfer factors?"
objectives:
- "Understand the concept of transfer factors"
- "Learn the role of transfer factors in the ABCD method"
- "See how the transfer factor is derived and applied in the in Higgs to tau tau analysis example"

keypoints:
- "Data-driven background estimates are a must in situations where you cannot get a reliable estimate from simulation"
- "They are also useful to validate predictions from simulations"
- "The ABCD method is a common background estimated concept, based on four different regions in phase space"
- "In this method, background shape in the signal region is estimated using a control region"
- "Differences between the control region and signal region are accounted for by event weights called transfer factors"
---

## Transfer factors

FIXME

## Transfer factors in the ABCD method

![](assets/img/abcd_diagram.png)

FIXME


## Application of a transfer factor in the Higgs to tau tau analysis example

In the [plot.py script](https://github.com/cms-opendata-analyses/HiggsTauTauNanoAODOutreachAnalysis/blob/master/plot.py#L155) you can find the following lines:
~~~
    # Data-driven QCD estimation
    QCD = getHistogram(tfile, "dataRunB", variable, "_cr")
    QCDRunC = getHistogram(tfile, "dataRunC", variable, "_cr")
    QCD.Add(QCDRunC)
    for name in ["W1J", "W2J", "W3J", "TT", "ZLL", "ZTT"]:
        ss = getHistogram(tfile, name, variable, "_cr")
        QCD.Add(ss, -1.0)
    for i in range(1, QCD.GetNbinsX() + 1):
        if QCD.GetBinContent(i) < 0.0:
            QCD.SetBinContent(i, 0.0)
    QCDScaleFactor = 0.80
    QCD.Scale(QCDScaleFactor)
~~~
{: .python}

> ## Challenge
> Task: try changing the value of QCDScaleFactor e.g. to 0.5 or 1.0, re-run plot.py and inspect the resulting plots.
{: .challenge}

## Derivation of a transfer factor in the Higgs to tau tau analysis example

Make a copy of the histograms file:
~~~
cp hisrograms.py histograms_antiiso.py
~~~
{: .language-bash}

Modify the file so that the output file is called histograms_antiiso.root. 
Invert the muon isolation to be iso_1>0.1.

Download a file to derive transfer factors:
~~~
wget https://raw.githubusercontent.com/cms-opendata-workshop/workshop-lesson-abcd-method/gh-pages/code/transfer_factors.py
~~~
{: .language-bash}

Run it
~~~
python transfer_factors.py
~~~
{: .language-bash}

{% include links.md %}
