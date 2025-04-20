# Hitkadmut (התקדמות)

> In Hebrew, "התקדמות" means "progress".

Hitkadmut is a very simple Python package for effective progress bars. The main advantage over other progress bars is when you need your progress bar to quickly display, such as with jobs in Slurm clusters, where `flush=True` is required to print immediately to the log files.

Other popular progress bars unfortunately make it complicated, as far as I know, to work properly in such environments. ProgIter works with `verbose=3` but has limited visual customization.

---

This page is WIP. More info to come soon, along with the upload to PyPi.
