# Simple measurement of the QCD scale factor
#
# The input file "histograms_antiiso.root" is produces with the "histograms.py" script
# from the original analysis but with an inverted muon isolation (iso_1>0.1). You can
# change this easily in the baseline selection next to the cut on the transverse mass.
# This allows us to measure the difference of the yield for the QCD estimate
# in the same-sign vs opposite-sign region and we can use the ratio as
# extrapolation factor in the actual analysis.


import ROOT
ROOT.gROOT.SetBatch(True)


# Retrieve a histogram from the input file based on the process and the variable
# name
def getHistogram(tfile, name, variable, tag=""):
    name = "{}_{}{}".format(name, variable, tag)
    h = tfile.Get(name)
    if not h:
        raise Exception("Failed to load histogram {}.".format(name))
    return h


def main(variable):
    tfile = ROOT.TFile("histograms_antiiso.root", "READ")

    # Data in the opposite-sign region
    data_os = getHistogram(tfile, "dataRunB", variable)
    dataRunC = getHistogram(tfile, "dataRunC", variable)
    data_os.Add(dataRunC)

    # Data in the same-sign region
    data_ss = getHistogram(tfile, "dataRunB", variable, "_cr")
    dataRunC = getHistogram(tfile, "dataRunC", variable, "_cr")
    data_ss.Add(dataRunC)

    # Subtract from each histogram all known processes
    for name in ["W1J", "W2J", "W3J", "TT", "ZLL", "ZTT"]:
        # Opposite-sign region
        os = getHistogram(tfile, name, variable)
        data_os.Add(os, -1.0)

        # Same-sign region
        ss = getHistogram(tfile, name, variable, "_cr")
        data_ss.Add(ss, -1.0)

    # Get sum of all events of the resulting histograms
    events_os = data_os.Integral()
    events_ss = data_ss.Integral()

    # Get extrapolation factor by dividing the counts
    print("Sum of QCD events in anti-isolated opposite-sign region: {:.2f}".format(events_os))
    print("Sum of QCD events in anti-isolated same-sign region: {:.2f}".format(events_ss))
    print("QCD extrapolation factor from same-sign to opposite-sign region: {:.2f}".format(events_ss / events_os))


# Perform the QCD extrapolation measurement inclusively along the given variable
if __name__ == "__main__":
    main("m_vis")
