# graspnetAPI
Forked from [original repo](https://github.com/graspnet/graspnetAPI) on `28/11/2024`.

## Install
1. Download repo.
```bash
git clone https://github.com/alk15/graspnetAPI.git
cd graspnetAPI
```

2. The repo has been tested with python3.8.
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
```

3. Create an environment.
```bash
virtualenv -p python3.8 ./venv
source venv/bin/activate
```

4. Install from source.

```bash
pip install .
```

## Document

Refer to [online document](https://graspnetapi.readthedocs.io/en/latest/index.html) for more details.  
[PDF Document](https://graspnetapi.readthedocs.io/_/downloads/en/latest/pdf/) is available, too. 


## Examples
```bash
cd examples

# change the path of graspnet root

# How to load labels from graspnet.
python3 exam_loadGrasp.py

# How to convert between 6d and rectangle grasps.
python3 exam_convert.py

# Check the completeness of the data.
python3 exam_check_data.py

# you can also run other examples
```

Please refer to our document for more examples.

## Citation
Please cite these papers in your publications if it helps your research:
```
@article{fang2023robust,
  title={Robust grasping across diverse sensor qualities: The GraspNet-1Billion dataset},
  author={Fang, Hao-Shu and Gou, Minghao and Wang, Chenxi and Lu, Cewu},
  journal={The International Journal of Robotics Research},
  year={2023},
  publisher={SAGE Publications Sage UK: London, England}
}

@inproceedings{fang2020graspnet,
  title={GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping},
  author={Fang, Hao-Shu and Wang, Chenxi and Gou, Minghao and Lu, Cewu},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition(CVPR)},
  pages={11444--11453},
  year={2020}
}
```