import sklearn
from sklearn.ensemble import RandomForestRegressor
import joblib
import pickle
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
class SSHPerdiction:
    http_model = RandomForestRegressor()
    def __init__(self):
        #TODO check if model exist other wise create a model first by calling nsl_kdd_*.py files and using the model.
        # loading all three flooding models
        print("Loading Models:")
        ssh_fname = "models/ssh_rfr.pkl"
        print("Loading " + ssh_fname + "...")
        self.ssh_model = pickle.load(open(ssh_fname, 'rb'))
    def prepareDict(self,dict):
        list=[dict['is_private'],dict['is_failure'],dict['is_root'],dict['is_valid'],dict['not_valid_count'],dict['ip_failure'],dict['ip_success'],dict['no_failure'],dict['first']]
        return list
    def predictSSH(self,instance):
        perdict = self.ssh_model.predict([instance])
        return perdict[0]

