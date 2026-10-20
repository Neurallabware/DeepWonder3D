# Getting started

## Prepare the scientific runtime

The source README records an Ubuntu 20.04 environment with Python 3.8, PyTorch 2.0.1, CUDA 11.8, cuDNN 8.9.0, and TensorRT 8.6.1. Follow its installation steps for the application; the Python 3.12 docs build is independent of this runtime.

From `DeepWonder3D_pytorch/`, check the model folders `pth/DENO_pth`, `pth/RMBG_pth`, `pth/SEG_pth`, and `pth/SR_pth`. Inspect whether each required asset is present and whether Git LFS retrieval is needed.

## Calibrate before 3D localization

The 3D pipeline requires `pth/psffit_matrix.mat`. Use `get_PSFfit_matrix.py` with calibration data appropriate for your optical setup; the supplied calibration is not automatically transferable to another microscope.

## Configure and run

Edit the parameter block in the selected script: input/output paths, `now_pixel_size`, `target_pixel_size`, `t_resolution`, `GPU_index`, and module selection.

```bash
cd DeepWonder3D_pytorch
python main_pipeline_2d.py
# Or, after checking multi-view calibration:
python main_pipeline_3d.py
```

These scripts use parameter blocks rather than the Hydra CLI of other lab tools. The docs build does not execute either script.
