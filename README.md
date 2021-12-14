# SSH-Attack-Detection-Using-Machine-Learning
For Detection of SSH Attacks on Linux Machine, Read provided research paper for more details about methodology.
Paper > https://1drv.ms/b/s!AlxwyurlqSWO7RlxZ01mJsaCyG3S
## Requirements 
- Python 3.X
- Pytail <code>python -m pip install pygtail</code>

1. Install the requirements
2. run main_ssh.py using <code>python main.py</code>
3. If everything is working convert it into executable service using pyInstaller

## Dataset
Dataset was collected inhouse, using server ssh log files.
feature extractor is embedded within the program, review <code>ssh_on_demand_data_collection.py</code> code to understand it's working
