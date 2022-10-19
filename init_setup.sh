echo [$(date)]: "START"
echo [$(date)]: "CREATING CONDA ENV WITH PYTHON VERSION 3.8"
conda create --prefix ./venv python=3.8 -y
echo [$(date)]: "ACTIVATING VENV "
source activate ./venv
echo [$(date)]: "INSTALLING REQUIREMENTS IN REQUIREMENTS_DEV.TXT"
pip install -r requirements_dev.txt 
echo [$(date)]: "END"