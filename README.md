# P1-data-combination-code
Code accompanying the manuscript "Changing Sea Level, Changing Shorelines: Comparison of Remote Sensing Observations at the Terschelling Barrier Island"

Notebooks are related to the following data/methods sections and can be run in this order if not otherwise specified:

Section 1.4 Linking shoreline change to sea level changes
- data_overview.ipynb (overview figure, requires output from the following notebooks)

Section 2.2 Sea level heights from tide gauges
- IB_correction.ipynb
- tidal_correction_EOT_FES.ipynb
- ttide.ipynb

Section 2.3 Vertical land motion from GNSS
- VLM_from_GNSS.ipynb

Section 3.1 Comparison of altimetry and tide gauges
- compare_altimetry_vs_TG.ipynb
- DAC_Terschelling.ipynb (not used)

Section 3.2 Cross-shore changes from the intersection of land elevation data (JARKUS with sea level)
- jarkus_shoreline.ipynb

Section 3.3 Cross-shore changes from satellite-derived shorelines
Section 3.4 Sensitivity analysis of cross-shore changes from CASSIE
- cassie_sensitivity_analysis.ipynb
- cassie_file_for_reuse.ipynb

Section 3.5 Validation of cross-shore changes from CASSIE
- cassie-vs-coastsat.ipynb
- cassie_vs_jarkus.ipynb



