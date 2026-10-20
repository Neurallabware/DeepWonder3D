# Data contracts

The 2D script handles planar/projection data. The 3D script adds view merging and calibrated localization. Keep view ordering, pixel size in micrometres, frame rate in Hz, and calibration provenance with each input.

The PSF fit matrix describes source/target view IDs and linear x/y shift coefficients and intercepts. Its coefficient units must agree with the calibration and localization code.

Processing stages are DENO, TR, SR, RMBG, SEG, MN, and VM. Outputs are organized under `STEP_1_DENO` through `STEP_7_VM`, where applicable, together with timing records. Module selection controls which stages run.

Before consuming exported neuronal traces, check their component IDs, output fields, time sampling after TR, spatial scaling after SR, and any multi-view merging. Filenames or array sizes alone do not establish correspondence.
